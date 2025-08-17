# MySQLServer.py
# Create the database 'alx_book_store' without using SELECT/SHOW.

import os
import sys

try:
    import mysql.connector
except Exception as e:
    print(f"Error importing mysql.connector: {e}")
    sys.exit(1)

def main():
    DB_NAME = "alx_book_store"

    # Read connection details from environment variables (with sensible defaults)
    host = os.getenv("MYSQL_HOST", "localhost")
    user = os.getenv("MYSQL_USER", "root")
    password = os.getenv("MYSQL_PASSWORD") or os.getenv("MYSQL_PWD") or ""
    port = int(os.getenv("MYSQL_PORT", "3306"))

    conn = None
    cursor = None

    try:
        # Connect to server (not a specific DB yet)
        conn = mysql.connector.connect(
            host=host,
            user=user,
            password=password,
            port=port,
        )
        cursor = conn.cursor()

        # No SELECT/SHOW; use IF NOT EXISTS so it won't fail if DB exists
        cursor.execute(f"CREATE DATABASE IF NOT EXISTS {DB_NAME}")
        # Optional: commit is not strictly necessary for DDL in MySQL, but harmless
        conn.commit()

        # Required success message
        print(f"Database '{DB_NAME}' created successfully!")

    except mysql.connector.Error as err:
        # Print error message for connection/creation errors
        print(f"Error connecting to the DB or creating database: {err}")
        sys.exit(1)
    finally:
        # Ensure proper cleanup
        if cursor is not None:
            try:
                cursor.close()
            except Exception:
                pass
        if conn is not None:
            try:
                conn.close()
            except Exception:
                pass

if __name__ == "__main__":
    main()
