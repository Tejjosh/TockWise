import pyodbc
import bcrypt
import os

def get_connection():
    conn_str = (
        "Driver={ODBC Driver 17 for SQL Server};"
        "Server=localhost;"
        "Database=TockWise;"
        "Trusted_Connection=yes;"
    )
    return pyodbc.connect(conn_str)

def check_user_credentials(email, password):
    try:
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT password FROM users WHERE email = ?", email)
        row = cursor.fetchone()
        if row and bcrypt.checkpw(password.encode(), row[0].encode()):
            return True
    except Exception as e:
        print(f"Login error: {e}")
    return False
