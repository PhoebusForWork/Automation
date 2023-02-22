# -*- coding: utf-8 -*-
import os
import sys

sys.path.append(os.path.abspath('.'))
from utils.data_utils import EnvReader
from elasticsearch import Elasticsearch
import psycopg2
import json

env = EnvReader()
plt_host = env.POSTGRES_PLT_HOST
cs_host = env.POSTGRES_CS_HOST
plt_port = env.POSTGRES_PLT_PORT
cs_port = env.POSTGRES_CS_PORT
plt_password = env.POSTGRES_PLT_PASSWORD
cs_password = env.POSTGRES_CS_PASSWORD


class Postgresql:

    def __init__(self, database="wallet", user="app_jr", platform="plt"):
        self.database = database
        self.user = user
        self.password = None
        self.host = None
        self.port = None
        if platform == "plt":
            self.host = plt_host
            self.port = plt_port
            self.password = plt_password
        elif platform == "cs":
            self.host = cs_host
            self.port = cs_port
            self.password = cs_password
        else:
            raise "platform Error"
        self.db = psycopg2.connect(database=self.database,
                                   user=self.user,
                                   password=self.password,
                                   host=self.host,
                                   port=self.port)

    def select_sql(self, sql):
        self.cursor = self.db.cursor()
        try:
            self.cursor.execute(sql)
            data = self.cursor.fetchall()
            return data
        except:
            print('select Error')
        finally:
            self.cursor.close()

    def run_sql(self, sql):
        self.cursor = self.db.cursor()
        try:
            self.cursor.execute(sql)
            self.db.commit()
            print("SQL Success")
        except:
            print("SQL Fail")
            self.db.rollback()
        finally:
            self.db.close()


class ES:

    def __init__(self):
        self.host = 'localhost'
        self.port = '9200'
        self.user = 'developer'
        self.password = 'sRQV9foYA7cKEUh'

        self.es = Elasticsearch(hosts=self.host,
                                http_auth=(self.user, self.password),
                                port=self.port)

    def get_index(self):
        target = self.es.indices.get_alias().keys()
        return target

    def query(self, index, query_json, scroll='5m', size=100):
        target = self.es.search(index=index,
                                query=query_json,
                                scroll=scroll,
                                size=size)
        return target

    def add_data(self, index, json_data):
        self.es.index(index=index, body=json_data)

    def update_data():
        pass

    def del_data():
        pass


if __name__ == '__main__':
    # database 是指定要查詢的庫
    def printJson(func):
        print(json.dumps(func, sort_keys=True, indent=4,
                         separators=(',', ':')))

    test = ES()
    abc = {"match": {"user_id": "66"}}
    t = test.query(index='vs_wallet_log', query_json=abc)
    printJson(t)
    # a = test.get_index()
    # print(a)
    # print(json.dumps(a,sort_keys=True,indent=4,separators=(',',':')))
