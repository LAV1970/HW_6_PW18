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

# Идентификатор предмета, по которому вы хотите найти студента
subject_id = 8  # Замените X на фактический идентификатор предмета

# SQL-запрос
sql_query = f"""
    SELECT student, AVG(CAST(grade_name AS SIGNED)) AS average_grade
    FROM grade
    WHERE subject_id = {subject_id}
    GROUP BY student
    ORDER BY average_grade DESC
    LIMIT 1;
"""

# Выполните запрос
cursor.execute(sql_query)

# Получите результат
result = cursor.fetchall()
print(result)

# Закройте курсор и соединение
cursor.close()
db_connection.close()
