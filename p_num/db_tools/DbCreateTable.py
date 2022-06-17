import psycopg2
from psycopg2 import Error
class DbCreateTable:


    def __init__(self,database,user,password,host="db",port="5432"):
        self.connect = psycopg2.connect(
            database=database,
            user=user,
            password=password,
            host=host,
            port=port

        )
        self.cur = self.connect.cursor()

    def create_table(self):
        try:
            create_table_query = '''CREATE TABLE item (
                        item_id serial NOT NULL PRIMARY KEY,
                        N INTEGER NOT NULL,
                            price INTEGER NOT NULL,
                            price_rub REAL NOT NULL,
                        purchase_time VARCHAR NOT NULL
                    );'''

            self.cur.execute(create_table_query)
            print("Table created successfully")
            self.connect.commit()
            self.connect.close()
        except (Exception, Error) as error:
            print("Ошибка при работе с PostgreSQL", error)
            self.connect.close()
