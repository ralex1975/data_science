from sqlite3 import OperationalError
import psycopg2
from sqlalchemy import select

# Подключиться к существующей базе данных
connection = psycopg2.connect(database='BigData',
                       user='postgres',
                       password='Quasar3',
                       host='127.0.0.1')

def execute_read_query(connection, query):
    cursor = connection.cursor()
    result = None
    try:
        cursor.execute(query)
        result = cursor.fetchall()
        return result
    except OperationalError as e:
        print(f"The error '{e}' occurred")

select_users = "id"
users = execute_read_query(connection, select_users)

for user in users:
    print(user)