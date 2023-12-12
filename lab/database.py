import sqlite3
import datetime



def main():
    db_connection = sqlite3.connect('log.db')
    db_cursor = db_connection.cursor()

    db_cursor.execute("SELECT * FROM logs")
    # db_cursor.execute("SELECT name FROM sqlite_schema")
    print(db_cursor.fetchall())

def main2():
    pass

if __name__ == "__main__":
    main()
