from db_manager import DBManager

class DBInsert(DBManager):
    def table(tb_name, tb_cols, values, setDate):
        """
        tb_cols = (device_id, device_sno...)
        values = (device_id.data, ...)
        """

        arg = [f"{x}" for x in tb_cols]
        print(arg)

        if 'idx' in arg:
            del arg[arg.index('idx')]
        
        if 'date' in arg:
            del arg[arg.index('date')]

        if setDate == False:
            if 'cow_estrous' in arg:
                del arg[arg.index('cow_estrous')]

            if 'cow_pregnent' in arg:
                del arg[arg.index('cow_pregnent')]
        
        sql_q = ",".join(arg)
        
        data = []

        print(values)

        for i in values:
            v = "'" + str(i) + "'"
            data.append(v)

        sql_data = ",".join(data)

        sql = f"""
        INSERT INTO
        {tb_name}({sql_q})
        VALUES ({sql_data})
        """

        print(sql)



        con = DBManager.connect()
        DBManager.insert(con, sql)



