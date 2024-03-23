import psycopg2
from faker import Faker
import random

fake = Faker()

db_params = {
    'database': 'postgres',
    'user': 'postgres',
    'password': '7777777',
    'host': 'localhost',
    'port': 5432
}

def create_users(conn, n=10):
    with conn.cursor() as cur:
        for _ in range(n):
            fullname = fake.name()
            email = fake.email()
            cur.execute("INSERT INTO users (fullname, email) VALUES (%s, %s)", (fullname, email))
        conn.commit()

def create_statuses(conn):
    statuses = ['new', 'in progress', 'completed']
    with conn.cursor() as cur:
        for status in statuses:
            cur.execute("INSERT INTO status (name) VALUES (%s) ON CONFLICT (name) DO NOTHING", (status,))
        conn.commit()

def create_tasks(conn, n=30):
    with conn.cursor() as cur:
        cur.execute("SELECT id FROM users")
        user_ids = [row[0] for row in cur.fetchall()]
        cur.execute("SELECT id FROM status")
        status_ids = [row[0] for row in cur.fetchall()]

        for _ in range(n):
            title = fake.sentence(nb_words=6)
            description = fake.text(max_nb_chars=200)
            status_id = random.choice(status_ids)
            user_id = random.choice(user_ids)
            cur.execute("INSERT INTO tasks (title, description, status_id, user_id) VALUES (%s, %s, %s, %s)", (title, description, status_id, user_id))
        conn.commit()

def main():
    conn = psycopg2.connect(**db_params)

    create_statuses(conn)
    create_users(conn, 10)
    create_tasks(conn, 30)

    conn.close()
    print("База даних успішно заповнена випадковими даними.")

if __name__ == "__main__":
    main()
