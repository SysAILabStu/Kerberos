import pymysql
import sqlite3
<<<<<<< HEAD
from .config import *
=======
from config import *
>>>>>>> 4f3b6b69ecd2e1e4e119872031bf1e7c1ca6b75f

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

