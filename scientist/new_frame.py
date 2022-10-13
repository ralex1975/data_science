from aifc import Error
import psycopg2

try:
    # Подключиться к существующей базе данных
    connection = psycopg2.connect(database='TEST',
                       user='postgres',
                       password='Quasar3',
                       host='127.0.0.1')

    cursor = connection.cursor()
    postgreSQL_select_Query = "SELECT * FROM Пон"

    cursor.execute(postgreSQL_select_Query)
    print("Выбор строк из таблицы mobile с помощью cursor.fetchall")
    mobile_records = cursor.fetchall()
    row = []
    print("Вывод каждой строки и ее столбцов")
    print(mobile_records)
    for i in mobile_records:
        print("Id =", row[i], )

except (Exception, Error) as error:
    print("Ошибка при работе с PostgreSQL", error)
finally:
    if connection:
        cursor.close()
        connection.close()
        print("Соединение с PostgreSQL закрыто")