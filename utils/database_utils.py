# -*- coding: utf-8 -*-
import psycopg2
import configparser
import os
from pymongo import MongoClient


if os.getenv('MODE') is None:
    config = configparser.ConfigParser()
    config.read('config/config.ini')
    plt_host = config['postgres_connection']['plt_host']
    cs_host = config['postgres_connection']['cs_host']
    plt_port = config['postgres_connection']['plt_port']
    cs_port = config['postgres_connection']['cs_port']
    plt_password = config['postgres_connection']['plt_password']
    cs_password = config['postgres_connection']['cs_password']
else:
    plt_host = os.getenv('POSTGRES_PLT_HOST')
    cs_host = os.getenv('POSTGRES_CS_HOST')
    plt_port = os.getenv('POSTGRES_PLT_PORT')
    cs_port = os.getenv('POSTGRES_CS_PORT')
    plt_password = os.getenv('POSTGRES_PLT_PASSWORD')
    cs_password = os.getenv('POSTGRES_CS_PASSWORD')


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
        self.db = psycopg2.connect(
            database=self.database, user=self.user, password=self.password, host=self.host, port=self.port)

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


if __name__ == '__main__':
    # database 是指定要查詢的庫
    dbHandle = Postgresql(database='cs_user', platform="cs")
    data = dbHandle.select_sql(
        "select * from cs_user.vs_user where id = 28;")
    print(data)
    pass
