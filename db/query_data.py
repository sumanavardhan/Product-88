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
    sql = "UPDATE category SET name = value WHERE id = ?"
    cursor.execute(sql, [value, category_id])
    conn.commit()
    return cursor.fetchone()

def update_bookauthor(conn, value=None, column=None):
    cursor = conn.cursor()
    sql = "UPDATE bookauthor SET column = value WHERE column = ?"
    cursor.execute(sql, [value])
    conn.commit()
    return cursor.fetchone()

def update_book(conn, value=None, column=None):
    cursor = conn.cursor()
    sql = "UPDATE book SET column = value WHERE column = ?"
    cursor.execute(sql, [value])
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

def delete_bookauthor(conn, value=None, column=None):
    cursor = conn.cursor()
    sql = "DELETE FROM bookauthor WHERE column = ?"
    cursor.execute(sql, [value])
    conn.commit()
    return cursor.fetchone()

def delete_book(conn, value=None, column=None):
    cursor = conn.cursor()
    sql = "DELETE FROM book WHERE column = ?"
    cursor.execute(sql, [value])
    conn.commit()
    return cursor.fetchone()


def main():
    database = "bookstore.db"
    conn = create_connection(database)

    # print(select_book_id(conn, 517576600))

    # books = all_books(conn)
    # results = []
    
    # for book in books:
    #     """
    #     book:
    #         - book_id
    #         - title
    #         - price
    #         - year
    #         - quantity
    #         - rating
    #         - category_id
    #     """

    #     # TODO: get author name
    #     # by going to bookauthor -> finding author_id next to book_id
    #     # go to author table -> get author_name next by querying with author_id
    #     authors = []
    #     for author in select_book_id(conn, book[0]): 
    #         author_names = select_author(conn, author[1], id)[1]
    #         authors.append()
            
    #     category = select_category(conn, book[6], id)

    #     results.append({
    #         "name": book[1],
    #         "published": book[3],
    #         "author": authors,
    #         "category": category[1]
    #     })
    # print(results)

    print(select_author(conn, 81, "id"))

    conn.close()

    


if __name__ == "__main__":
    main()
