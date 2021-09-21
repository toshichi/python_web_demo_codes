# To access a SQLite database

import sqlite3

if __name__ == '__main__':
    db = sqlite3.connect('db_test.sqlite3')
    db.row_factory = sqlite3.Row
    cursor = db.cursor()
    cursor.execute('select * from test_table')
    for row in cursor.fetchall():
        print(row['id'], row['name'])