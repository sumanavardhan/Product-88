from connection import create_connection

""" ==========  GET All QUERIES  =========== """

def all_books(conn):
    sql = "SELECT * FROM book"
    cursor = conn.cursor()
    cursor.execute(sql)
    return cursor.fetchall()

def all_authors(conn):
    sql = "SELECT * FROM author"
    cursor = conn.cursor()
    cursor.execute(sql)
    return cursor.fetchall()

def all_categories(conn):
    sql = "SELECT * FROM category"
    cursor = conn.cursor()
    cursor.execute(sql)
    return cursor.fetchall()

""" ========== GET ONE QUERIES  =========== """

def select_book(conn, book_id):
    sql = "SELECT * FROM book WHERE id = ?"
    cursor = conn.cursor()
    cursor.execute(sql, [book_id])
    return cursor.fetchone()

def select_book_id(conn,value=None):
    cursor = conn.cursor()
    sql = "SELECT * from book where id = ?"
    cursor.execute(sql, [value])
    return cursor.fetchall()

def select_author_id(conn,value=None):
    cursor = conn.cursor()
    sql = "SELECT * from bookauthor where book_id = ?"
    cursor.execute(sql, [value])
    return cursor.fetchall()

def select_author(conn, value=None, column=None):
    cursor = conn.cursor()

    if column == "name":
        sql = "SELECT id, name FROM author WHERE name = ?"
        cursor.execute(sql, [value])

    elif column == "id":
        sql = "SELECT id, name FROM author WHERE id = ?"
        cursor.execute(sql, [value])

    else:
        sql = "SELECT id, name FROM author"
        cursor.execute(sql)

    return cursor.fetchone()


def select_category(conn, value=None, column=None):
    cursor = conn.cursor()

    if column == "name":
        sql = "SELECT id, name FROM category WHERE name = ?"
        cursor.execute(sql, [value])

    elif column == "id":
        sql = "SELECT id, name FROM category WHERE id = ?"
        cursor.execute(sql, [value])

    else:
        sql = "SELECT id, name FROM category"
        cursor.execute(sql)

    return cursor.fetchone()


""" ==========  UPDATE QUERIES  =========== """

def update_author(conn, value=None, author_id=None):
    cursor = conn.cursor()
    sql = "UPDATE author SET name = ? WHERE id = ?"
    cursor.execute(sql, [value, author_id])
    conn.commit()
    return cursor.fetchone()

def update_category(conn, value=None, category_id=None):
    cursor = conn.cursor()
    sql = "UPDATE category SET name = ? WHERE id = ?"
    cursor.execute(sql, [value, category_id])
    conn.commit()
    return cursor.fetchone()

"""def update_bookauthor(conn, value=None, column=None):
    cursor = conn.cursor()
    sql = "UPDATE bookauthor SET column = value WHERE column = ?"
    cursor.execute(sql, [value])
    conn.commit()
    return cursor.fetchone()"""

def update_book(conn, value=None, book_id=None,col=None):
    cursor = conn.cursor()
    match col:
        case 1:#Title
            sql = "UPDATE book SET title = ? WHERE id = ?"
            cursor.execute(sql, [value,book_id])
            conn.commit()
        case 2:#price
            sql = "UPDATE book SET price = ? WHERE id = ?"
            cursor.execute(sql, [value,book_id])
            conn.commit()
        case 3:#year
            sql = "UPDATE book SET year = ? WHERE id = ?"
            cursor.execute(sql, [value,book_id])
            conn.commit()
        case 4:#quantity
            sql = "UPDATE book SET quantity = ? WHERE id = ?"
            cursor.execute(sql, [value,book_id])
            conn.commit()
        case 5:#rating
            sql = "UPDATE book SET rating = ? WHERE id = ?"
            cursor.execute(sql, [value,book_id])
            conn.commit()
        case 6:#category_id
            sql = "UPDATE book SET category_id = ? WHERE id = ?"
            cursor.execute(sql, [value,book_id])
            conn.commit()            
    return cursor.fetchone()

""" ==========  DELETE QUERIES  =========== """

def delete_author(conn, value=None):
    cursor = conn.cursor()
    """sql = "DELETE FROM book WHERE id = ?"
    cursor.execute(sql, [book_id])
    conn.commit()"""

    sql = "DELETE FROM author WHERE id = ?"
    cursor.execute(sql, [value])
    conn.commit()

    sql = "DELETE FROM bookauthor WHERE author_id = ?"
    cursor.execute(sql, [value])
    conn.commit()

    return cursor.fetchone()


def delete_category(conn, value=None):
    cursor = conn.cursor()
    sql = "DELETE FROM category WHERE id = ?"
    cursor.execute(sql, [value])
    conn.commit()
    return cursor.fetchone()

"""def delete_bookauthor(conn, value=None, column=None):
    cursor = conn.cursor()
    sql = "DELETE FROM bookauthor WHERE column = ?"
    cursor.execute(sql, [value])
    conn.commit()
    return cursor.fetchone()"""

def delete_book(conn, value=None):
    cursor = conn.cursor()
    sql = "DELETE FROM book WHERE id = ?"
    cursor.execute(sql, [value])
    conn.commit()
    return cursor.fetchone()