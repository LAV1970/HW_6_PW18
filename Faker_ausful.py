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
num_records = 3

# Создайте и выполните SQL-запрос для добавления данных
for _ in range(num_records):
    name_group = fake.name()
    fach = fake.random_int(min=1, max=8)
    cursor.execute(
        "INSERT INTO groupps (name_group, fach) VALUES (%s, %s)",
        (name_group, fach),
    )

# Сделайте фиксацию изменений
db_connection.commit()

# Закройте курсор и соединение
cursor.close()
db_connection.close()
