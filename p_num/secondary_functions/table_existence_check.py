from db_tools.DbCreateTable import DbCreateTable


def table_existence_check(post_cur, data, usd) -> None:
    name_table = post_cur.SELECT_table("SELECT table_name FROM information_schema.tables WHERE table_schema = 'public'"
                                       " ORDER BY table_name;")

    try:
        if name_table[0] != 'item':  # проверка на сушествования таблицы
            table_cur = DbCreateTable(database="test_db", host='db', user="test_user",
                                      password="test_db")  # Класс для созданий таблиц и только!
            table_cur.create_table()  # Создаем таблицу (в случаи если она есть pass)
    except TypeError:
        table_cur = DbCreateTable(database="test_db", host='db', user="test_user",
                                  password="test_db")  # Класс для созданий таблиц и только!
        table_cur.create_table()  # Создаем таблицу (в случаи если она есть pass)


    count_value_table = post_cur.SELECT_table("SELECT count(n) FROM item;")
    if count_value_table[0] < 1:  # Проверка на заполняемость
        for i in data:
            item_tuple = (i[0], i[1], i[2], usd * int(i[2]), str(i[3]))  # VALUES (%s, %s, %s, %s ,%s)
            post_cur.insert_table(item_tuple)  # первоначальное заполнение таблицы данными
