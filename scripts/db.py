import sqlite3

# cursor = sqliteConnection.cursor()
# s = "SELECT sqlite_version();"
# cursor.execute(s)
# record = cursor.fetchall()
# print("SQLite Database Version is: ", record)
#

# finally:
#     if sqliteConnection:
#         sqliteConnection.close()
#         print("The SQLite connection is closed")
database_path = 'files/database.db'


def sql_connection(database_path):
    try:
        sqliteConnection = sqlite3.connect(database_path)
        print("Database created and Successfully Connected to SQLite")
        return sqliteConnection
    except sqlite3.Error as error:
        print("Error while connecting to sqlite", error)


def sql_close_connection(conn):
    if conn:
        conn.close()
        print("The SQLite connection is closed")


def sql_create_table(conn):
    cursorObj = conn.cursor()
    cursorObj.execute("""CREATE TABLE IF NOT EXISTS BOOKS
                        (ID INTEGER PRIMARY KEY AUTOINCREMENT, 
                        NAME TEXT,
                        YEAR TEXT,
                        EDITION TEXT,
                        LANG TEXT,
                        PAGES TEXT,
                        IMAGE_URL TEXT,
                        DOWNLOAD_URL TEXT,
                        BOOK_ID INTEGER,
                        EXTENTION TEXT,
                        SIZE_IN_B INTEGER,
                        CREATED_AT TEXT)""")
    conn.commit()


def sql_insert(conn, record) -> bool:
    # Check record exists
    if not sql_check_if_record_exists(conn, record['book_id']):
        cursorObj = conn.cursor()
        cursorObj.execute("""INSERT INTO BOOKS (NAME ,YEAR ,EDITION ,LANG ,PAGES,IMAGE_URL,DOWNLOAD_URL ,BOOK_ID ,EXTENTION, SIZE_IN_B, CREATED_AT)
                            VALUES(?, ?, ?, ?, ?, ?, ?, ?,?,?,DATETIME('now','localtime'))""",
                          (record['name'], record['year'], record['edition'], record['lang'], record['pages'],
                           record['image_url'], record['download_url'],
                           record['book_id'], record['extention'], record['size_in_b'],))
        conn.commit()
        return True
    else:
        return False


def sql_check_if_record_exists(conn, id):
    cursorObj = conn.cursor()
    rows = cursorObj.execute("""SELECT 1 
                        FROM BOOKS
                        WHERE BOOK_ID = ?;""", (id,))

    return True if rows.fetchall() else False


def sql_read_query(conn, attr, value):
    cursorObj = conn.cursor()
    rows = cursorObj.execute(
        f"SELECT * FROM BOOKS WHERE {attr} = ? ;", (value,))
    qs = rows.fetchall()
    res = []
    for q in qs:
        res.append(
            {'id': q[0],
             'name': q[1],
             'year': q[2],
             'edition': q[3],
             'lang': q[4],
             'pages': q[5],
             'image_url': q[6],
             'download_url': q[7],
             'book_id': q[8],
             'extention': q[9],
             'size_in_b': q[10],
             'crated_at': q[11],
             }
        )
    return res
