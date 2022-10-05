from .db_manager import DBManager

class DBUpdate(DBManager):
    def update(tbl_name, set_key, set_value, update_key, update_value):
        """
        sey_key = ['set_key1', 'set_key2'...]
        set_value = ['set_value1', 'set_value2'...]
        update_key = ['update_key1', 'update_key2'...]
        update_value = ['update_value1', 'update_value2'...]
        """
        sql_s = ""
        for i in range(len(set_key)):
            sql_s += f"{set_key[i]} = {set_value[i]}, "   
        sql_s = sql_s[:-2]

        sql_w = ""
        for i in range(len(update_key)):
            sql_w += f"{update_key[i]} = '{update_value[i]}' AND "
        sql_w = sql_w[:-5]

        sql = f"""
        UPDATE {tbl_name}
        SET {sql_s}
        WHERE {sql_w}
        """

        con = DBManager.connect()

        DBManager.commit(con, sql)