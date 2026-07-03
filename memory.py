import sqlite3

DATABASE = "database/memory.db"


def create_database():

    conn = sqlite3.connect(DATABASE)

    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS conversations(

        id INTEGER PRIMARY KEY AUTOINCREMENT,

        customer_name TEXT,

        query TEXT,

        response TEXT

    )
    """)

    conn.commit()

    conn.close()
def save_conversation(customer_name, query, response):

    conn = sqlite3.connect(DATABASE)

    cursor = conn.cursor()

    cursor.execute(
        """
        INSERT INTO conversations(customer_name, query, response)
        VALUES(?,?,?)
        """,
        (customer_name, query, response)
    )

    conn.commit()

    conn.close()
def get_last_query(customer_name):

    conn = sqlite3.connect(DATABASE)

    cursor = conn.cursor()

    cursor.execute(
        """
        SELECT query
        FROM conversations
        WHERE customer_name=?
        ORDER BY id DESC
        LIMIT 1
        """,
        (customer_name,)
    )

    row = cursor.fetchone()

    conn.close()

    if row:
        return row[0]

    return "No previous conversation found."