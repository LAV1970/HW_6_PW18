from faker import Faker
import mysql.connector

# Создайте подключение к базе данных
db_connection = mysql.connector.connect(
    host="localhost",
    user="root",
    password="MasooR_1924",
    database="uni",  # Замените на имя вашей базы данных
)

# Создайте курсор для выполнения SQL-запросов
cursor = db_connection.cursor()

# Создайте генератор фальшивых данных
fake = Faker()

# Определите количество записей, которые вы хотите добавить
num_records = 100

# Создайте и выполните SQL-запрос для добавления данных
for _ in range(num_records):
    name = fake.name()
    age = fake.random_int(min=18, max=99)
    cursor.execute("INSERT INTO student (name, age) VALUES (%s, %s)", (name, age))

# Сделайте фиксацию изменений
db_connection.commit()

# Закройте курсор и соединение
cursor.close()
db_connection.close()
