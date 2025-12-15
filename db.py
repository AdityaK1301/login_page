import mysql.connector
from mysql.connector import Error

def get_db_connection():
    try:
        conn = mysql.connector.connect(
            host='localhost',
            username='root',
            password='',
            database='flask_project'
        )
        if conn.is_connected():
            return conn
        
    except mysql.connector.Error as e:
        print(f"Error : {e}")
        return None