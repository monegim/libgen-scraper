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


def sql_insert(conn, record):
    cursorObj = conn.cursor()
    cursorObj.execute("""INSERT INTO BOOKS (NAME ,YEAR ,EDITION ,LANG ,PAGES,IMAGE_URL,DOWNLOAD_URL ,BOOK_ID ,EXTENTION, SIZE_IN_B, CREATED_AT)
                        VALUES(?, ?, ?, ?, ?, ?, ?, ?,?,?,DATETIME('now','localtime'))""",
                      (record['name'], record['year'], record['edition'], record['lang'], record['pages'],
                       record['image_url'], record['download_url'],
                       record['id'], record['extention'], record['size_in_b'],))
    conn.commit()
    print("RECORD INSERTED")

def sql_check_if_record_exists(conn, id):
    cursorObj = conn.cursor()
    rows = cursorObj.execute("""SELECT 1 
                        FROM BOOKS
                        WHERE BOOK_ID = ?;""",(id,))
    
    return True if rows.fetchall() else False
