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
num_records = 5

# Определите звания преподавателей
degrees = ["Профессор", "Доцент", "Старший преподаватель", "Ассистент"]

# Создайте и выполните SQL-запрос для добавления данных
for _ in range(num_records):
    name = fake.name()
    degree = fake.random_element(elements=degrees)
    cursor.execute(
        "INSERT INTO professor (name, degree) VALUES (%s, %s)",
        (name, degree),
    )

# Сделайте фиксацию изменений
db_connection.commit()

# Закройте курсор и соединение
cursor.close()
db_connection.close()
