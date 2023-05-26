from connection import create_connection
import query_data as qd


def insert_author(conn, author: dict):
    sql = "INSERT INTO author (name) VALUES (?)"
    cursor = conn.cursor()
    cursor.execute(sql, [author['name']])
    conn.commit()
    return cursor.lastrowid


def insert_category(conn, category: dict):
    sql = "INSERT INTO category (name) VALUES (?)"
    cursor = conn.cursor()
    cursor.execute(sql, [category["name"]])
    conn.commit()
    return cursor.lastrowid

def insert_bookauthor(conn, bookauthor: dict):
    """
    bookauthor:
        - book_id
        - author_id
    """

    sql = "INSERT INTO bookauthor (author_id, book_id) VALUES (?,?)"
    cursor = conn.cursor()
    cursor.execute(sql, [bookauthor["author_id"], bookauthor["book_id"]])

    conn.commit()
    return cursor.lastrowid

def insert_user(conn, user: dict):
    sql = "INSERT INTO user (name, email, password) VALUES (?,?,?)"
    cursor = conn.cursor()
    cursor.execute(sql, [user["name"],user["name"]])
    conn.commit()
    return cursor.lastrowid


def insert_book(conn, book: dict):
    sql = "INSERT INTO book (title, price, year, quantity, rating, category_id) VALUES (?, ?, ? ,?, ?, ?)"
    cursor = conn.cursor()

    """ --- 1. CATEGORY ENTRY --- """
    category = qd.select_category(conn, book["category"], "name")
    if category:
        category_id = category[0]
    else:
        category_id = insert_category(conn, {"name": book["category"]})


    """ --- 2. AUTHOR ENTRY --- """
    # TODO: Make sure to skip authors that already exist
    author_ids = [] # will need author_ids to create bookauthor record
    for author in book["author"]: # loop here, authors can now accept a dict of authors
        author_name = book["author"][author]
        exists = qd.select_author(conn, author_name, "name")

        if exists is None:
            author_ids.append(insert_author(conn, {'name': author_name}))
        else:
            author_ids.append(exists[0])
        
    """ --- 3. BOOKAUTHOR ENTRY --- """ # DONE IN BOOK_SERVER

    cursor.execute( sql, [
                    book["title"],
                    book["price"],
                    book["year"],
                    book["quantity"],
                    book["rating"],
                    category_id
                ])
    
    conn.commit()
    print("We made it to the end!")
    return (cursor.lastrowid, author_ids)

