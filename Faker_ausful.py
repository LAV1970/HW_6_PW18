from faker import Faker
import mysql.connector

# подключение к базе данных
db_connection = mysql.connector.connect(
    host="localhost",
    user="root",
    password="MasooR_1924",
    database="uni",  # имя базы данных
)

# курсор для выполнения SQL-запросов
cursor = db_connection.cursor()

# генератор фальшивых данных
fake = Faker()

# количество записей, которые надо добавить
num_records = 50

# SQL-запрос для добавления данных
for _ in range(num_records):
    name = fake.name()
    age = fake.random_int(min=18, max=99)
    cursor.execute("INSERT INTO student (name, age) VALUES (%s, %s)", (name, age))

# фиксация изменений
db_connection.commit()

# Закройте курсор и соединение
cursor.close()
db_connection.close()
