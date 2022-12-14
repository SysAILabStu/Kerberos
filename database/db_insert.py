from .db_manager import DBManager

class DBInsert(DBManager):
    def table(tb_name, tbl_cols, values, setEstrous = False, setPregnent = False):
        """
        tb_cols = (device_id, device_sno...)
        values = (device_id.data, ...)
        """

        arg = [f"{x}" for x in tbl_cols]

        if setEstrous == False:
            if 'cow_estrous' in arg:
                del arg[arg.index('cow_estrous')]

        if setPregnent == False:
            if 'cow_pregnent' in arg:
                del arg[arg.index('cow_pregnent')]
        
        sql_q = ",".join(arg)
        
        data = []


        for i in values:
            v = "'" + str(i) + "'"
            data.append(v)

        sql_data = ",".join(data)

        sql = f"""
        INSERT INTO
        {tb_name}({sql_q})
        VALUES ({sql_data})
        """


        con = DBManager.connect()
        DBManager.commit(con, sql)



