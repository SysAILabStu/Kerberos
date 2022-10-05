import pymysql
import sqlite3
from .config import *

class DBManager:
    """
    Super Class
    """
    def connect():
        if opt == 'sqlite':
            con = sqlite3.connect(database)

        elif opt == 'maria':
            con = pymysql.connect(host = ip, user = user, password = pwd, db = database, charset = 'utf8')

        elif opt == 'mongo':
            print("mongo is not ready!")
            con = ''

        return con

    def commit(con, sql):
        print(sql)
        cur = con.cursor()
        cur.execute(sql)
        con.commit()
        con.close

    def fetchall(con, sql):
        print(sql)
        cur = con.cursor()
        cur.execute(sql)
        rows = cur.fetchall()
        for i in rows:
            print(i)
        return rows

