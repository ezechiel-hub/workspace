"""the program create a db for the given data
   and then run the given query"""
import sqlite3
# Define the database name and table schema
db_name = "etudiant.db"
table_schema = """
CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    age INTEGER NOT NULL
);
"""

# Connect to the database and create the table
try:
    conn = sqlite3.connect(db_name)
except sqlite3.Error as e:
    print(f"An error occurred: {e}")
cursor = conn.cursor()
try:
    conn = sqlite3.connect(db_name)
    cursor = conn.cursor()
    cursor.execute(table_schema)
except sqlite3.Error as e:
    print(f"An error occurred: {e}")
conn.commit()
conn.close()