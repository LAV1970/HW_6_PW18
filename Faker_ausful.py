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
num_records = 50

# Создайте и выполните SQL-запрос для добавления данных
for _ in range(num_records):
    student_id = None  # Замените на значение student_id
    name = fake.name()
    age = fake.random_int(min=18, max=45)
    cursor.execute(
        "INSERT INTO student (student_id, name, age) VALUES (%s, %s, %s)",
        (student_id, name, age),
    )

# Сделайте фиксацию изменений
db_connection.commit()

# Закройте курсор и соединение
cursor.close()
db_connection.close()
