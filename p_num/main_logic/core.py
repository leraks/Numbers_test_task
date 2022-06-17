from secondary_functions.data_sheets import data_sheets
from collections import Counter
import time

update_position = []
insert_position = []

def update_document(post_cur, data, USD, new_data):
    global update_position
    try:
        if new_data != None:
            if len(new_data) == len(data):
                for i in new_data:
                    if i in data:
                        pass
                    else:
                        update_position.append(i)  # Список даннах на обновления

            for i in update_position:  # обновление данных
                if len(new_data) == len(data):  # Если списки равны по элементом то это точно update

                    flat = [y for x in new_data for y in x]  # Поиск дубликатов
                    c = Counter(flat)
                    print(c[i[0]])
                    if int(c[i[0]]) > 1:
                        print("Есть дубликат Обновлять не могу ")
                        update_position.remove(i)
                        break

                    item_tuple_update = (
                        i[1], i[2], USD * int(i[2]), str(i[3]), i[0])  # VALUES (%s, %s, %s, %s ,%s)
                    post_cur.update_table(item_tuple_update)
                    update_position = []
        else:
            new_data = []
    except Exception as err:
        print(err)



def insert_and_del_document(post_cur, data, USD, new_data):
    global insert_position
    try:
        if new_data != None:
            if len(new_data) != len(data):
                if len(new_data) > len(data):  # Добавление данных в таблицу
                    for i in new_data:
                        if i in data:
                            pass
                        else:
                            insert_position.append(i)

                    if insert_position == []:  # Проверка на дубликат если это повтор то пишем оповешение и не добовляем его в бд
                        print("Вы написали дубликат!")

                    for i in insert_position:  # Ишем новые значения для добавления
                        item_tuple_insert = (i[0], i[1], i[2], USD * int(i[2]), str(i[3]))
                        post_cur.insert_table(item_tuple_insert)
                        insert_position = []

                elif len(new_data) < len(data):  # Удаление данных
                    for i in data:
                        if i in new_data:
                            pass
                        else:
                            flat = [y for x in new_data for y in x]
                            c = Counter(flat)
                            if int(c[i[
                                0]]) > 0:  # В случаи если есть дубликат то блакируем удалаение пока есть дубликаты
                                print("Вы удалили дубликат")
                                break
                            post_cur.delete_table(i[0])
        else:
            post_cur.delete_table(insert_query="DELETE FROM item;",
                                  item_query=())  # если в таблицк 0 значений то полностью чистим бд
    except Exception as err:
        print(err)


def run_full_def_app(post_cur, data, USD):

    while True:
        new_data = data_sheets()
        update_document(post_cur, data, USD, new_data)
        insert_and_del_document(post_cur, data, USD, new_data)
        data = new_data
        time.sleep(3)