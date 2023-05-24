from connection import create_connection
import query_data as qd


def insert_author(conn, author: dict):
    sql = "INSERT INTO author (name) VALUES (?)"
    cursor = conn.cursor()
    cursor.execute(sql, [author["name"]])
    conn.commit()
    return cursor.lastrowid


def insert_category(conn, category: dict):
    sql = "INSERT INTO category (name) VALUES (?)"
    cursor = conn.cursor()
    cursor.execute(sql, [category["name"]])
    conn.commit()
    return cursor.lastrowid


def insert_book(conn, book: dict):
    sql = "INSERT INTO book (name, published, author_id, category_id) VALUES (?, ?, ? ,?)"
    cursor = conn.cursor()
    # TODO: query authors and categories

    author = qd.select_author(conn, book["author"], "name")
    if author:
        author_id = author[0]
    else:
        author_id = insert_author(conn, {"name": book["author"]})

    category = qd.select_category(conn, book["category"], "name")
    if category:
        category_id = category[0]
    else:
        category_id = insert_category(conn, {"name": book["category"]})

    cursor.execute(
        sql, [book["name"], book["published"], author_id, category_id])
    conn.commit()
    return cursor.lastrowid


def main():
    database = "bims.db"
    conn = create_connection(database)

    if conn:

        with conn:
            insert_book(conn, {"name": "The Bee Book",
                               "published": "2016-03-1",
                               "author": "Emma Tennant",
                               "category": "Science"})


if __name__ == "__main__":
    main()