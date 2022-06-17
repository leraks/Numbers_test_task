def update_offline(post_cur,data,usd):  # Если кто то работал в файле в offline то изменения при запуске
    # будут автоматическими все данныые которых нет в таблице удаляются
    post_cur.delete_table(insert_query="DELETE FROM item;", item_query=())  # Удаляю из бд значения
    for i in data:
        try:
            item_id = list(post_cur.SELECT_table("SELECT item_id FROM item WHERE item_id = %s;" % i[0]))
        except:  # В случае если в offline будут добавлены новые данные то мы их ловим и добовляем в бд
            tuple = (i[0], i[1], i[2], usd * int(i[2]), str(i[3]))
            post_cur.insert_table(tuple)