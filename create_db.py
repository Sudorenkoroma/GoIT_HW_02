import psycopg2

# Ваші параметри підключення до бази даних
db_params = {
    'database': 'postgres',
    'user': 'postgres',
    'password': '7777777',
    'host': 'localhost',
    'port': 5432
}

# Шлях до вашого SQL файлу
sql_file_path = 'task_system.sql'

def execute_sql_from_file(file_path, connection_params):
    # Підключення до бази даних
    conn = psycopg2.connect(**connection_params)
    cursor = conn.cursor()

    # Відкриття файлу SQL та виконання його вмісту
    with open(file_path, 'r') as file:
        sql_script = file.read()
    cursor.execute(sql_script)

    # Закриття курсору та з'єднання
    conn.commit()
    cursor.close()
    conn.close()

    print("Таблиці були успішно створені відповідно до скрипта.")

# Виконання функції
execute_sql_from_file(sql_file_path, db_params)
