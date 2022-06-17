from secondary_functions.data_sheets import data_sheets
from main_logic.core import run_full_def_app
from db_tools.PostgresDBEdit import PostgresDBEdit
from secondary_functions.usd import usd_found
from secondary_functions.table_existence_check import table_existence_check
from secondary_functions.update_offline import update_offline



if __name__ == '__main__':
    data = data_sheets()  # Данные с листа
    USD = usd_found()  # Курс $ от центра банка
    post_cur = PostgresDBEdit(database="test_db", host='db',user="test_user",
                              password="test_db")  # Класс с методами для взаимодействия с бд
    table_existence_check(post_cur, data, USD)  # проверка на сушествования таблицы
    # первоначальное заполнение таблицы данными
    update_offline(post_cur,data,USD)  # Если кто то работал в offline, то изменения при запуске будут автоматическими



    #Полный запуск все функций
    run_full_def_app(post_cur, data, USD)



