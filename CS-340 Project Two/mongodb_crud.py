#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Feb  4 05:10:02 2024

@author: janncymota_snhu
"""

import pymongo

class MongoDBCRUD:
    def __init__(self, username, password, host, port, database_name, authSource='admin'):
        connection_uri = f"mongodb://{username}:{password}@{host}:{port}/{database_name}?authSource={authSource}"
        self.client = pymongo.MongoClient(connection_uri)
        self.database = self.client[database_name]

    def create(self, collection_name, document):
        try:
            self.database[collection_name].insert_one(document)
            return True
        except Exception as error:
            return str(error)

    def read(self, collection_name, query):
        try:
            cursor = self.database[collection_name].find(query)
            return list(cursor)
        except Exception as error:
            return str(error)

    def update(self, collection_name, query, update_data):
        try:
            result = self.database[collection_name].update_many(query, {"$set": update_data})
            return f"Modified {result.modified_count} documents"
        except Exception as error:
            return str(error)

    def delete(self, collection_name, query):
        try:
            result = self.database[collection_name].delete_many(query)
            return f"Deleted {result.deleted_count} documents"
        except Exception as error:
            return str(error)

    def find_one(self, collection_name, query):
        try:
            document = self.database[collection_name].find_one(query)
            return document
        except Exception as error:
            return str(error)