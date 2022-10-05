from .db_manager import *

class DBDelete(DBManager):

    # Delete table
    def table(db_name, tbl_name):

        sql = f'''
            DROP TABLE {tbl_name}
        '''

        con = DBManager.connect()
        DBManager.commit(con, sql)

    # 해당 테이블의 전체 데이터 삭제
    def table_allInfo(self, db_name, tbl_name):

        sql = f'''
        DELETE FROM {tbl_name}
        '''

        # sqlite
        if self.opt == 'sqlite':
            con = sqlite3.connect(db_name)
            cur = con.cursor()
            cur.execute(sql)

            con.commit()
        
        # maria
        elif self.opt == 'maria':
            con = pymysql.connect(host = mariaIP, user = mariaUser, password = mariaPWD, 
                                  db = mariaDB, charset = 'utf8')             

        cur = con.cursor()
        cur.execute(sql)
        con.commit()
        con.close()

    # Use one delete key to delete
    def one_delete_key(self, db_name, tbl_name, delete_key, delete_data):
        sql =f"""
        DELETE FROM {tbl_name}
        WHERE
        {delete_key} = '{delete_data}'
        """

        # sqlite
        if self.opt == 'sqlite':
            con = sqlite3.connect(db_name)

        # maria 
        elif self.opt == 'maria':
            con = pymysql.connect(host = mariaIP, user = mariaUser, password = mariaPWD, 
                                  db = mariaDB, charset = 'utf8') 
        cur = con.cursor()
        cur.execute(sql)
        con.commit()
        con.close()

    # Use two delete keys to delete
    def two_delete_keys(self, db_name, tbl_name, delete_key, delete_data):
        """
        delete_key = [delete_key1, delete_key2]
        delete_data = [delete_data1, delete_data2]
        """

        sql = f"""
        DELETE FROM {tbl_name}
        WHERE
        {delete_key[0]} = '{delete_data[0]}'
        AND
        {delete_key[1]} = '{delete_data[1]}'
        """

        # sqlite
        if self.opt == 'sqlite':
            con = sqlite3.connect(db_name)

        # maria
        elif self.opt == 'maria':
            con = pymysql.connect(host = mariaIP, user = mariaUser, password = mariaPWD, 
                                  db = mariaDB, charset = 'utf8') 
        cur = con.cursor()
        cur.execute(sql)
        con.commit()
        con.close()

    # Use three delete keys to delete
    def three_delete_keys(self, db_name, tbl_name, delete_key, delete_data):
        """
        delete_key = [delete_key1, delete_key2, delete_key3]
        delete_data = [delete_data1, delete_data2, delete_data3]
        """

        sql = f"""
        DELETE FROM {tbl_name}
        WHERE
        {delete_key[0]} = '{delete_data[0]}'
        AND
        {delete_key[1]} = '{delete_data[1]}'
        AND
        {delete_key[2]} = '{delete_data[2]}'
        """
        # sqlite
        if self.opt == 'sqlite':
            con = sqlite3.connect(db_name)

        # maria
        elif self.opt == 'maria':
            con = pymysql.connect(host = mariaIP, user = mariaUser, password = mariaPWD, 
                                  db = mariaDB, charset = 'utf8') 
        cur = con.cursor()
        cur.execute(sql)
        con.commit()
        con.close()


    # Use four delete keys to delete
    def four_delete_keys(self, db_name, tbl_name, delete_key, delete_data):
        """
        delete_key = [delete_key1, delete_key2, delete_key3, delete_key4]
        delete_data = [delete_data1, delete_data2, delete_data3, delete_data4]
        """

        sql = f"""
        DELETE FROM {tbl_name}
        WHERE
        {delete_key[0]} = '{delete_data[0]}'
        AND
        {delete_key[1]} = '{delete_data[1]}'
        AND
        {delete_key[2]} = '{delete_data[2]}'
        AND
        {delete_key[3]} = '{delete_data[3]}'
        """
        
        # sqlite
        if self.opt == 'sqlite':
            con = sqlite3.connect(db_name)

        # maria
        elif self.opt == 'maria':
            con = pymysql.connect(host = mariaIP, user = mariaUser, password = mariaPWD, 
                                  db = mariaDB, charset = 'utf8') 
        cur = con.cursor()
        cur.execute(sql)
        con.commit()
        con.close()