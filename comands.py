import psycopg2

# Параметри підключення до бази даних
conn_params = {
    'database': 'postgres',
    'user': 'postgres',
    'password': '7777777',
    'host': 'localhost',
    'port': 5432
}

# Встановлення з'єднання з базою даних
conn = psycopg2.connect(**conn_params)
cursor = conn.cursor()

# 1. Отримати всі завдання певного користувача
def get_tasks_by_user(user_id):
    cursor.execute("SELECT * FROM tasks WHERE user_id = %s", (user_id,))
    tasks = cursor.fetchall()
    for task in tasks:
        print(task)

# 2. Вибрати завдання за певним статусом
def get_tasks_by_status(status_name):
    cursor.execute("SELECT * FROM tasks WHERE status_id = (SELECT id FROM status WHERE name = %s)", (status_name,))
    tasks = cursor.fetchall()
    for task in tasks:
        print(task)

# 3. Оновити статус конкретного завдання
def update_task_status(task_id, new_status):
    cursor.execute("UPDATE tasks SET status_id = (SELECT id FROM status WHERE name = %s) WHERE id = %s", (new_status, task_id))
    conn.commit()

# 4. Отримати список користувачів, які не мають жодного завдання
def get_users_without_tasks():
    cursor.execute("SELECT * FROM users WHERE id NOT IN (SELECT user_id FROM tasks)")
    users = cursor.fetchall()
    for user in users:
        print(user)

# 5. Додати нове завдання для конкретного користувача
def add_new_task(title, description, status_id, user_id):
    cursor.execute("INSERT INTO tasks (title, description, status_id, user_id) VALUES (%s, %s, %s, %s)", (title, description, status_id, user_id))
    conn.commit()

# 6. Отримати всі завдання, які ще не завершено
def get_uncompleted_tasks():
    cursor.execute("SELECT * FROM tasks WHERE status_id != (SELECT id FROM status WHERE name = 'completed')")
    tasks = cursor.fetchall()
    for task in tasks:
        print(task)

# 7. Видалити конкретне завдання
def delete_task(task_id):
    cursor.execute("DELETE FROM tasks WHERE id = %s", (task_id,))
    conn.commit()

# 8. Знайти користувачів з певною електронною поштою
def find_users_by_email(email_pattern):
    cursor.execute("SELECT * FROM users WHERE email LIKE %s", (email_pattern,))
    users = cursor.fetchall()
    for user in users:
        print(user)

# 9 Оновити ім'я користувача
def update_user_name(user_id, new_name):
    cursor.execute("UPDATE users SET fullname = %s WHERE id = %s", (new_name, user_id))
    conn.commit()

# 10 Отримати кількість завдань для кожного статусу
def get_tasks_count_by_status():
    cursor.execute("SELECT s.name, COUNT(t.id) FROM status s LEFT JOIN tasks t ON s.id = t.status_id GROUP BY s.name")
    counts = cursor.fetchall()
    for count in counts:
        print(count)

# 11 Отримати завдання, які призначені користувачам з певною доменною частиною електронної пошти
def get_tasks_for_email_domain(domain):
    cursor.execute("SELECT t.* FROM tasks t JOIN users u ON t.user_id = u.id WHERE u.email LIKE %s", ('%' + domain,))
    tasks = cursor.fetchall()
    for task in tasks:
        print(task)

# 12 Отримати список завдань, що не мають опису
def get_tasks_without_description():
    cursor.execute("SELECT * FROM tasks WHERE description IS NULL OR description = ''")
    tasks = cursor.fetchall()
    for task in tasks:
        print(task)

# 13 Вибрати користувачів та їхні завдання, які є у статусі 'in progress'
def get_users_with_tasks_in_progress():
    cursor.execute("SELECT u.fullname, t.title FROM users u INNER JOIN tasks t ON u.id = t.user_id INNER JOIN status s ON t.status_id = s.id WHERE s.name = 'in progress'")
    results = cursor.fetchall()
    for result in results:
        print(result)

# 14 Отримати користувачів та кількість їхніх завдань
def get_users_and_tasks_count():
    cursor.execute("SELECT u.fullname, COUNT(t.id) FROM users u LEFT JOIN tasks t ON u.id = t.user_id GROUP BY u.fullname")
    results = cursor.fetchall()
    for result in results:
        print(result)


if __name__ == "__main__":
    get_users_and_tasks_count()
    cursor.close()
    conn.close()

