#!/usr/bin/python
# Requires  onelogin, csv342 and optparse-pretty
# 
# Script that import users from a csv file into OneLogin.
# It supports roles, groups and custom_roles (works as import UI)

from __future__ import unicode_literals

import csv342 as csv
import io
import json
import os.path

from optparse import OptionParser
from optparse_mooi import CompactColorHelpFormatter

from onelogin.api.client import OneLoginClient


try:
    unicode
except NameError:
    unicode = str


class ImportUsers(object):

    version = "1.0.0"

    # Don't modify it
    API_USER_ATTRIBUTES = ['firstname', 'lastname', 'email', 'username', 'group', 'company', 'department', 'distinguished_name', 'locale_code', 'member_of', 'title', 'phone', 'status']
    REQUIRED_USER_ATTRIBUTES = ['firstname', 'lastname', 'email', 'username']

    def __init__(self, options):
        self.options = options
        self.client = self.get_client()
        self.user_data_list = self.get_user_data_from_csv()
        self.groups = {}
        self.roles = {}
        self.custom_atributes = []

        if self.user_data_list:
            if 'group' in self.user_data_list[0]['data'].keys():
                self.load_groups()
            if 'role' in self.user_data_list[0]['data'].keys():
                self.load_roles()
            if self.user_data_list[0]['custom_data']:
                self.load_custom_attributes()

    def get_client(self):
        client_id = client_secret = None

        if self.options.client_id is not None and self.options.client_secret is not None:
            client_id = self.options.client_id
            client_secret = self.options.client_secret
            region = self.options.region
        else:
            if os.path.isfile('onelogin.sdk.json'):
                json_data = open('onelogin.sdk.json').read()
                data = json.loads(json_data)
                if 'client_id' in data.keys() and 'client_secret' in data.keys():
                    client_id = data['client_id']
                    client_secret = data['client_secret']
                    region = data.get('region', 'us')

        if client_id is None or client_secret is None:
            raise Exception("OneLogin Client ID and Secret are required")

        return OneLoginClient(client_id, client_secret, region)

    def get_user_data_from_csv(self):
        filepath = self.options.file
        if not os.path.isfile(filepath):
            raise Exception("Can't retrieve user data. %s does not exist" % filepath)

        user_data_list = []
        wrong_rows = []
            
        with io.open(filepath, encoding=self.options.encoding, newline='') as csv_file:
            self.log("Reading file %s ......" % filepath, True)
            csv_reader = csv.reader(csv_file, delimiter=',')
            for i, row in enumerate(csv_reader):

                if i == 0:
                    fieldnames = row
                else:                
                    if len(fieldnames) != len(row):
                        self.log("Line %s of the CSV has incomplete data %s fields instead of %s" % (i, len(row), len(fieldnames)))
                        wrong_rows.append(row)
                    else:
                        user_data = {
                            'data': {},
                            'custom_data': {}
                        }
                        for j, value in enumerate(row):
                            fieldname = fieldnames[j]
                            if 'custom_attribute_' in fieldname:
                                custom_attr_name = fieldname.replace('custom_attribute_', '')
                                user_data['custom_data'][custom_attr_name] = value
                            else:
                                user_data['data'][fieldname] = value
                        user_data_list.append(user_data)

        if wrong_rows:
            original_filename = os.path.basename(filepath)
            wrong_rows_filename = 'invalid_%s' % original_filename
            wrong_rows_filepath = filepath.replace(original_filename, wrong_rows_filename)
            wrong_rows_file = open(wrong_rows_filepath, 'w')
            writer = csv.writer(wrong_rows_file, dialect=csv.excel)
            writer.writerow(fieldnames)
            for row in wrong_rows:
                writer.writerow(row)
            wrong_rows_file.close()
            self.log("Found %s wrong rows, will be skipped from the process so they are exported to %s" % (len(wrong_rows), wrong_rows_filepath), True)

        return user_data_list

    def get_users(self, query_parameters):
        users = self.client.get_users(query_parameters)
        return users

    def create_user(self, fieldid_value, user_data):
        user = None
        user_params = {}
        for attr in self.API_USER_ATTRIBUTES:
            if attr in user_data:
                if attr == 'group':
                    group_id = self.retrieve_group_id(user_data['group'])
                    if group_id is None:
                        self.log("Error assigning group. %s is not valid value" % user_data['group'])
                    else:
                        user_params['group_id '] = group_id
                else:
                    user_params[attr] = user_data[attr]
        if not 'status' in user_params:
            user_params['status'] = 1

        if not set(self.REQUIRED_USER_ATTRIBUTES).issubset(user_params.keys()):
            self.log("Error creating user (%s). Required attributes not provided" % fieldid_value)
        else:
            user = self.client.create_user(user_params)
            if self.client.error_description:
                self.log("Error creating user (%s). %s %s" % (fieldid_value, self.client.error, self.client.error_description))
            else:
                self.log("User %s (%s) created" % (user.id, fieldid_value))
        return user

    def update_user(self, user_id, fieldid_value, user_data):
        update_user_params = {}
        for attr in self.API_USER_ATTRIBUTES:
            if attr in user_data:
                if attr == 'group':
                    if user_data['group'] == 'none' or user_data['group'] == 'None':
                        update_user_params['group_id '] = None
                    else:
                        group_id = self.retrieve_group_id(user_data['group'])
                        if user_data['group'] and group_id is None:
                            self.log("Error assigning group to user %s (%s). %s is not valid value" % (user_id, fieldid_value, user_data['group']))
                        else:
                            update_user_params['group_id '] = group_id
                elif attr not in ['username', 'email']:
                    update_user_params[attr] = user_data[attr]

        user = self.client.update_user(user_id, update_user_params)
        if self.client.error_description:
            self.log("Error updating user %s (%s). %s %s" % (user_id, fieldid_value, self.client.error, self.client.error_description))
        else:
            self.log("User %s (%s) updated" % (user_id, fieldid_value))
        return user

    def delete_user(self, user_id, fieldid_value):
        self.client.delete_user(user_id)
        if self.client.error_description:
            self.log("Error deleting user %s (%s). %s %s" % (user_id, fieldid_value, self.client.error, self.client.error_description))
        else:
            self.log("User %s (%s) deleted" % (user_id, fieldid_value))

    def load_groups(self):
        group_data_list = self.client.get_groups()
        for group_data in group_data_list:
            self.groups[group_data.name] = group_data.id

    def retrieve_group_id(self, group_data):
        group_id = None
        if self.groups and group_data:
            if isinstance(group_data, int) or \
                (isinstance(group_data, str) and str.isdigit(group_data)) or \
                (isinstance(group_data, unicode) and str.isdigit(str(group_data))):
                if int(group_data) in self.groups.values():
                    group_id = int(group_data)
            elif group_data in self.groups.keys():
                    group_id = int(self.groups[group_data])
        return group_id

    def load_roles(self):
        role_data_list = self.client.get_roles()
        for role_data in role_data_list:
            self.roles[role_data.name] = int(role_data.id)

    def retrieve_role_id(self, role_data):
        role_id = None
        if self.roles and role_data:
            if isinstance(role_data, int) or \
                (isinstance(role_data, str) and str.isdigit(role_data)) or \
                (isinstance(role_data, unicode) and str.isdigit(str(role_data))):
                if int(role_data) in self.roles.values():
                    role_id = int(role_data)
            else:
                if role_data in self.roles.keys():
                    role_id = int(self.roles[role_data])
        return role_id

    def retrieve_role_info(self, user_data_roles):
        role_info_list = user_data_roles.split(";")
        new_user_roles = []
        for role_info in role_info_list:
            role_id = self.retrieve_role_id(role_info)
            if role_id is not None:
                new_user_roles.append(role_id)
        return new_user_roles

    def load_custom_attributes(self):
        self.custom_attributes = self.client.get_custom_attributes()

    def assign_password(self, user_id, fieldid_value, password):
        self.client.set_password_using_clear_text(user_id, password, password)
        if self.client.error_description:
            self.log("Error assigning password to user %s (%s). %s %s" % (user_id, fieldid_value, self.client.error, self.client.error_description))
        else:
            self.log("Password assigned to user %s (%s)" % (user_id, fieldid_value))

    def assign_custom_attributes(self, user_id, fieldid_value, custom_user_attrs):
        for custom_user_attr_name in custom_user_attrs.keys():
            if not custom_user_attr_name in self.custom_attributes:
                del custom_user_attrs[custom_user_attr_name]
                self.log("Custom attribute %s ignored because does not exist" % custom_user_attr_name)

        self.client.set_custom_attribute_to_user(user_id, custom_user_attrs)

        if self.client.error_description:
            self.log("Error assigning custom attributes to user %s (%s). %s %s" % (user_id, fieldid_value, self.client.error, self.client.error_description))

    def assign_role_info(self, user_id, fieldid_value, user_data_roles, created=True):
        new_user_roles = self.retrieve_role_info(user_data_roles)
        if created:
            if new_user_roles:
                self.client.assign_role_to_user(user_id, new_user_roles)
                if self.client.error_description:
                    self.log("Error assigning roles %s to user %s (%s). %s %s" % (",".join(str(v) for v in new_user_roles), user_id, fieldid_value, self.client.error, self.client.error_description))
                else:
                    self.log("Roles assiged %s to user %s (%s)." % (",".join(str(v) for v in new_user_roles), user_id, fieldid_value))
        else:
            insert_user_roles = []
            remove_user_roles = []
            user_roles = self.client.get_user_roles(user_id)
            for user_role in user_roles:
                if not user_role in new_user_roles:
                    remove_user_roles.append(user_role)
            for user_role in new_user_roles:
                if user_role not in user_roles:
                    insert_user_roles.append(user_role)

            if remove_user_roles:
                self.client.remove_role_from_user(user_id, remove_user_roles)
                if self.client.error_description:
                    self.log("Error removing roles %s from user %s (%s). %s %s" % (",".join(str(v) for v in remove_user_roles), user_id, fieldid_value, self.client.error, self.client.error_description))
                else:
                    self.log("Roles removed %s from user %s (%s)." % (",".join(str(v) for v in remove_user_roles), user_id, fieldid_value))
            if insert_user_roles:
                self.client.assign_role_to_user(user_id, insert_user_roles)
                if self.client.error_description:
                    self.log("Error assigning roles %s to user %s (%s). %s %s" % (",".join(str(v) for v in insert_user_roles), user_id, fieldid_value, self.client.error, self.client.error_description))
                else:
                    self.log("Roles assigned %s to user %s (%s)." % (",".join(str(v) for v in insert_user_roles), user_id, fieldid_value))

    def log(self, message, show=False):
        if show or self.options.verbose:
            print(message)
        self.add_to_history_log(message)

    def add_to_history_log(self, message):
        with open("history.log", "a") as history_log_file:
            history_log_file.write(message + "\n")


def get_options():
    help_formatter = CompactColorHelpFormatter(
        heading_color='white-bold',
        usage_color='yellow',
        shopt_color='yellow-bold',
        lopt_color='yellow-bold',
        metavar_color='white-bold',
        help_color='yellow',
        description_color='white',
        align_long_opts=True
    )
    parser = OptionParser(formatter=help_formatter)

    parser.add_option("-i", "--client_id", dest="client_id", type="string",
                      help="A valid OneLogin API client_id")
    parser.add_option("-s", "--client_secret", dest="client_secret", type="string",
                      help="A valid OneLogin API client_secret")
    parser.add_option("-r", "--region", dest="region", default="us", type="string",
                      help="us or eu  (Default value: us")
    parser.add_option("-f", "--file", dest="file", type="string",
                      help="CSV file with the user data")
    parser.add_option("-x", "--fieldid", dest="fieldid", type="string", default="email",
                      help="CSV file with the user data")
    parser.add_option("-v", "--verbose", dest="verbose", action="store_true",
                      help="Enable verbose mode")
    parser.add_option("-e", "--encoding", dest="encoding", type="string", default="utf-8",
                      help="Encoding, default utf-8")

    (options, args) = parser.parse_args()

    if not options.file:
        raise Exception("CSV file with user data is required")

    return options


def main():
    options = get_options()
    importer = ImportUsers(options)

    if importer.user_data_list:
        importer.log("\nProcessing %s users" % len(importer.user_data_list), True)

        if options.fieldid == 'username':
            fieldid = 'username'
        else:
            fieldid = 'email'

        if not fieldid in importer.user_data_list[0]['data'].keys():
            importer.log("\nAborted, %s is a required column of the csv since you selected it as the field to identify users" % fieldid, True)
        else:
            for user_data in importer.user_data_list:
                query_parameters = {
                    fieldid: user_data['data'][fieldid]
                }
                users = importer.get_users(query_parameters)
                if users:
                    # User already exists so update some of its data
                    user = users[0]
                    fieldid_value = user.email if fieldid == 'email' else user.username

                    # check if user has delete flag
                    if 'delete' in user_data['data'] and user_data['data']['delete'] in ['Yes', 'yes']:
                        importer.delete_user(user.id, fieldid_value)
                        continue
                    else:
                        user = importer.update_user(user.id, fieldid_value, user_data['data'])
                        created = False
                else:
                    # User does not exists, create it
                    fieldid_value = user_data['data']['email'] if fieldid == 'email' else user_data['data']['username']

                    # check if user has delete flag
                    if 'delete' in user_data['data'] and user_data['data']['delete'] in ['Yes', 'yes']:
                        importer.log("Error deleting user %s. Not found" % (fieldid_value))
                        continue
                    else:
                        user = importer.create_user(fieldid_value, user_data['data'])
                        created = True

                if user:
                    if 'password' in user_data['data'].keys() and user_data['data']['password']:
                        importer.assign_password(user.id, fieldid_value, user_data['data']['password'])

                    if user_data['custom_data']:
                        importer.assign_custom_attributes(user.id, fieldid_value, user_data['custom_data'])

                    if 'role' in user_data['data'].keys():
                        importer.assign_role_info(user.id, fieldid_value, user_data['data']['role'], created)
    else:
        importer.log("\nNo users found on CSV", True)


if __name__ == '__main__':
    main()