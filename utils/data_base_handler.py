# -*- coding: utf-8 -*-
import psycopg2
from pymongo import MongoClient


class Postgresql:

    def __init__(self, database="wallet", user="app_jr",
                 password="bzUCpCnMVspNg7Dp", host="127.0.0.1", platform="plt"):
        self.database = database
        self.user = user
        self.password = password
        self.host = host
        port = None
        if platform == "plt":
            port = "5432"
        elif platform == "cs":
            port = "5431"
        else:
            raise "platform Error"
        self.db = psycopg2.connect(
            database=database, user=user, password=password, host=host, port=port)

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
    pass
