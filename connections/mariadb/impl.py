import mariadb
import os

class DbConnection:
    
    def __init__(
        self,
        db_name:str,
        db_user:str,
        db_password:str,
        db_host:str,
        db_port:int
    ):
        try:
            conn = mariadb.connect(
            user = db_user,
            password = db_password,
            host = db_host,
            port = db_port,
            database = db_name
        )
        except mariadb.Error as e:
            raise e
        
        self.conn = conn
        
    def clear_tables(self, tables:list[str]):
        try:
            cur = self.conn.cursor()
            for table in tables:  
                query = f'DELETE FROM {table}'
                cur.execute(query)

        except:
            self.conn.rollback()
            raise "clear table failed"
        
        else:
            self.conn.commit()
        
       