# MySQLServer.py
import os
import sys

try:
    import mysql.connector
    from mysql.connector import Error
except Exception as e:
    print("Error: mysql-connector-python is not installed. Install it with:\n"
          "  pip install mysql-connector-python", file=sys.stderr)
    sys.exit(1)

DB_NAME = "alx_book_store"

def main():
    """
    Creates the MySQL database `alx_book_store` if it does not already exist.
    No SELECT or SHOW statements are used.
    Prints a success message or an error to stderr on failure.
    Ensures the connection is opened and closed properly.
    """
    # Read connection details from environment variables (with sensible defaults)
    config = {
        "host": os.getenv("MYSQL_HOST", "localhost"),
        "port": int(os.getenv("MYSQL_PORT", "3306")),
        "user": os.getenv("MYSQL_USER", "root"),
        "password": os.getenv("MYSQL_PASSWORD", "")
    }

    conn = None
    cursor = None

    try:
        # Connect to the MySQL server (not to a specific database yet)
        conn = mysql.connector.connect(**config)
        conn.autocommit = True  # Ensure CREATE DATABASE is committed immediately
        cursor = conn.cursor()

        # Create the database if it doesn't exist (no SELECT/SHOW)
        cursor.execute(f"CREATE DATABASE IF NOT EXISTS {DB_NAME}")

        print(f"Database '{DB_NAME}' created successfully!")

    except Error as err:
        # Print error message for connection/operation failures
        print(f"Error: {err}", file=sys.stderr)
        sys.exit(1)

    finally:
        # Clean up: close cursor and connection
        try:
            if cursor is not None:
                cursor.close()
        except Exception:
            pass

        try:
            if conn is not None and conn.is_connected():
                conn.close()
        except Exception:
            pass

if __name__ == "__main__":
    main()