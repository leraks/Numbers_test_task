import psycopg2
from psycopg2 import Error


class PostgresDBEdit:

    def __init__(self,database,user,password,host="db",port="5432"):
        self.database = database
        self.user = user
        self.password = password
        self.host = host
        self.port = port


        self.connect = psycopg2.connect(
            database=database,
            user=user,
            password=password,
            host=host,
            port=port

        )
        self.cur = self.connect.cursor()


    def restart_blok(self):
        self.connect.close()
        self.cur.close()
        self.connect = psycopg2.connect(
            database= self.database,
            user=self.user,
            password=self.password,
            host=self.host,
            port=self.port

        )
        self.cur = self.connect.cursor()
        print("Blok restart")



    def SELECT_table(self,select_query):
        try:
            self.cur.execute(select_query)
            purchase_datetime = self.cur.fetchone()

            return purchase_datetime
        except (Exception, Error) as error:
            print("Ошибка при работе с PostgreSQL", error)



    def insert_table(self,item_query):
        try:
            insert_query = """INSERT INTO item (item_id, N, price, price_rub , purchase_time)
                                              VALUES (%s, %s, %s, %s ,%s)"""

            self.cur.execute(insert_query,item_query)
            self.connect.commit()
            print("Insert True!")
        except (Exception, Error) as error:
            print("Ошибка при работе с PostgreSQL", error)
            self.restart_blok()




    def update_table(self,item_query):
        try:
            update_query = """UPDATE item SET N = %s, price = %s, price_rub = %s, purchase_time = %s  WHERE item_id = %s"""
            self.cur.execute(update_query,item_query)
            self.connect.commit()
            print("Update True!")
        except (Exception, Error) as error:
            print("Ошибка при работе с PostgreSQL", error)


    def delete_table(self,item_query,insert_query = """DELETE FROM item WHERE item_id = %s"""):
        try:

            self.cur.execute(insert_query, (item_query,))
            self.connect.commit()
            print("Delete True!")
        except (Exception, Error) as error:
            print("Ошибка при работе с PostgreSQL", error)



    def close_db(self):
        self.connect.close()