#!/usr/bin/python

import requests

class Cursor(object):
    def __init__(self, url, model, headers, query_parameters, max_results):
        self.url = url
        self.model = model
        self.headers = headers
        self.query_parameters = {} if query_parameters is None else query_parameters
        self.max_results = max_results
        self.response = None
        self.collection = []
        self.after_cursor = None
        self.error = False

        self.fetch_next_page()
        while (not self.is_last()):
            self.fetch_next_page()

    def fetch_next_page(self):
        if self.response is None or self.after_cursor is not None:
            if self.after_cursor is not None:
                self.query_parameters['after_cursor'] = self.after_cursor

            self.response = requests.get(self.url, headers=self.headers, params=self.query_parameters)

            if self.response.status_code == 200:
                json_data = self.response.json()
                if json_data and json_data.get('data', None):
                    for object_data in json_data['data']:
                        if len(self.collection) < self.max_results:
                            self.collection.append(self.model(object_data))
                        else:
                            break

                self.after_cursor = self.get_after_cursor()
            else:
                self.after_cursor = None

    def get_after_cursor(self):
        after_cursor = None
        if self.response is not None:
            content = self.response.json()
            if content and 'pagination' in content and 'after_cursor' in content['pagination']:
                after_cursor = content['pagination']['after_cursor']
        return after_cursor

    def get_before_cursor(self, response):
        before_cursor = None
        content = response.json()
        if content and 'pagination' in content and 'before_cursor' in content['pagination']:
            before_cursor = content['pagination']['before_cursor']
        return before_cursor

    def objects(self):
        return self.collection

    def is_fetch_completed(self):
        if self.max_results is None:
            return False
        return len(self.collection) >= self.max_results

    def is_last(self):
        return (self.after_cursor is None) or self.is_fetch_completed()