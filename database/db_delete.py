from .db_manager import *

class DBDelete(DBManager):

    # Delete table
    def table(tbl_name):

        sql = f'''
            DROP TABLE {tbl_name}
        '''

        con = DBManager.connect()
        DBManager.commit(con, sql)

    # 해당 테이블의 전체 데이터 삭제
    def table_allInfo(tbl_name):

        sql = f'''
        DELETE FROM {tbl_name}
        '''

        con = DBManager.connect()
        DBManager.commit(con, sql)

    # Use one delete key to delete
    def one_delete_key(tbl_name, delete_key, delete_data):
        sql =f"""
        DELETE FROM {tbl_name}
        WHERE
        {delete_key} = '{delete_data}'
        """

        con = DBManager.connect()
        DBManager.commit(con, sql)

    # Use two delete keys to delete
    def two_delete_keys(tbl_name, delete_key, delete_data):
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

        con = DBManager.connect()
        DBManager.commit(con, sql)

    # Use three delete keys to delete
    def three_delete_keys(tbl_name, delete_key, delete_data):
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

        con = DBManager.connect()
        DBManager.commit(con, sql)


    # Use four delete keys to delete
    def four_delete_keys(tbl_name, delete_key, delete_data):
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
        
        con = DBManager.connect()
        DBManager.commit(con, sql)