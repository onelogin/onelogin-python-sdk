#!/usr/bin/python

import requests


class Cursor(object):
    def __init__(self, url, model, headers, query_parameters, max_results):
        self.url = url
        self.model = model
        self.headers = headers
        self.query_parameters = {} if query_parameters is None else query_parameters
        self.max_results = max_results
        self.response_content = None
        self.collection = []
        self.first_unprocessed_item = None
        self.after_cursor = None
        self.error = False

        self.fetch_next_page()
        while (not self.is_last() and not self.error):
            self.fetch_next_page()

    def fetch_next_page(self):
        if self.response_content is None or self.after_cursor is not None:
            if self.after_cursor is not None:
                self.query_parameters['after_cursor'] = self.after_cursor

            response = requests.get(self.url, headers=self.headers, params=self.query_parameters)
            if response.status_code == 200:
                self.response_content = response.json()
                self.process_response()
            else:
                self.error = True

    def process_response(self, start=0):
        if self.response_content and self.response_content.get('data', None):
            self.first_unprocessed_item = None
            for i, object_data in enumerate(self.response_content['data'][start:]):
                if len(self.collection) < self.max_results:
                    self.collection.append(self.model(object_data))
                else:
                    self.first_unprocessed_item = i
                    break

        self.after_cursor = self.get_after_cursor()

    def fetch_again(self, include_unprocessed=False):
        self.collection = []
        if include_unprocessed and self.first_unprocessed_item is not None:
            self.process_response(start=self.first_unprocessed_item)

        self.fetch_next_page()
        while (not self.is_last() and not self.error):
            self.fetch_next_page()
        return self

    def get_after_cursor(self):
        after_cursor = None
        if self.response_content is not None:
            if self.response_content and 'pagination' in self.response_content and 'after_cursor' in self.response_content['pagination']:
                after_cursor = self.response_content['pagination']['after_cursor']
        return after_cursor

    def get_before_cursor(self):
        before_cursor = None
        if self.response_content is not None:
            if self.response_content and 'pagination' in self.response_content and 'before_cursor' in self.response_content['pagination']:
                before_cursor = self.response_content['pagination']['before_cursor']
        return before_cursor

    def objects(self):
        return self.collection

    def is_fetch_completed(self):
        if self.max_results is None:
            return False
        return len(self.collection) >= self.max_results

    def is_last(self):
        return (self.after_cursor is None) or self.is_fetch_completed()
