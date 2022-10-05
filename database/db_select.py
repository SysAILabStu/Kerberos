from .db_manager import DBManager


class DBSelect(DBManager):
    # 조건 하나를 이용하여 테이블 조회
    def one_search_key(tbl_name, select_value, search_key, search_data):
        """
        select_value = ['select_value', ]
        """
        arg = [f"{x}" for x in select_value]
        sql_s = ",".join(arg)

        sql = f"""
        SELECT {sql_s}
        FROM {tbl_name}
        WHERE {search_key} = '{search_data}'
        """
        
        con = DBManager.connect()

        rows = DBManager.fetchall(con, sql)

        return rows
    
    # 조건 두개를 이용하여 테이블 조회
    def two_search_keys(tbl_name, select_value, search_key, search_data):
        """
        select_value = ['select_value',]
        search_key = ['search_key1', 'search_key2']
        search_data = ['search_data1', 'search_data2']
        """

        arg = [f"{x}" for x in select_value]
        sql_s = ",".join(arg)

        sql = f"""
        SELECT {sql_s}
        FROM {tbl_name}
        WHERE
        {search_key[0]} = '{search_data[0]}'
        AND
        {search_key[1]} = '{search_data[1]}'
        """
        con = DBManager.connect()

        rows = DBManager.fetchall(con, sql)

        return rows
    
    # 조건 세개를 이용하여 테이블 조회
    def three_search_keys(tbl_name, select_value, search_key, search_data):
        """
        select_value = ['select_value',]
        search_key = ['search_key1', 'search_key2', 'search_key3']
        search_data = ['search_data1', 'search_data2', 'search_data3']
        """

        arg = [f"{x}" for x in select_value]
        sql_s = ",".join(arg)

        sql = f"""
        SELECT {sql_s}
        FROM {tbl_name}
        WHERE
        {search_key[0]} = '{search_data[0]}'
        AND
        {search_key[1]} = '{search_data[1]}'
        AND
        {search_key[2]} = '{search_data[2]}'
        """

        con = DBManager.connect()

        rows = DBManager.fetchall(con, sql)  

        return rows

    # 테이블의 모든 데이터 조회
    def selectAll(tbl_name, select_value):
        """
        select_value = ['select_value',]
        """
        arg = [f"{x}" for x in select_value]
        sql_s = ",".join(arg)

        sql = f"""
            SELECT {sql_s}
            FROM {tbl_name}
            """
        
        con = DBManager.connect()

        rows = DBManager.fetchall(con, sql)

        return rows