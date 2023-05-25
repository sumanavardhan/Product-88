import sqlite3
from sqlite3 import Error

from connection import create_connection


def create_table(conn, create_table_sql):
    """
    Make a table with the specified statement

    Args:
        conn = Connection Object
        create_table_sql = SQL statement about table creation
    """

    try:
        c = conn.cursor()
        c.execute(create_table_sql)
    except Error as e:
        print(e)


def main():
    database = "bookstore.db"

    make_author_table = """
                        CREATE TABLE IF NOT EXISTS author
                        (
                            id integer PRIMARY KEY,
                            name VARCHAR(255) NOT NULL
                        );
                        """

    make_category_table = """
                        CREATE TABLE IF NOT EXISTS category
                        (
                            id integer PRIMARY KEY,
                            name VARCHAR(255) NOT NULL
                        );
                        """

    make_book_table = """
                    CREATE TABLE IF NOT EXISTS book
                    (
                        id integer PRIMARY KEY,
                        title VARCHAR(255) NOT NULL,
                        price integer NOT NULL,
                        year int NOT NULL,
                        quantity int  NOT NULL,
                        rating VARCHAR(50),
                        category_id integer NOT NULL,
                        FOREIGN KEY (category_id)
                            REFERENCES category (id) ON DELETE CASCADE ON UPDATE CASCADE
                    );
                    """
    
    make_bookauthor_table = """
    
                    CREATE TABLE IF NOT EXISTS bookauthor
                    (
                        id integer PRIMARY KEY,
                        author_id integer NOT NULL,
                        book_id integer NOT NULL,
                        FOREIGN KEY (author_id)
                            REFERENCES author (id) ON DELETE CASCADE ON UPDATE CASCADE,
                        FOREIGN KEY (book_id)
                            REFERENCES book (id) ON DELETE CASCADE ON UPDATE CASCADE
                    );
                    """

    make_user_table = """
                    CREATE TABLE IF NOT EXISTS user
                    (
                        user_id integer PRIMARY KEY,
                        name VARCHAR(50) NOT NULL,
                        email VARCHAR(50) NOT NULL,
                        password VARCHAR(50) NOT NULL
                    );
                    """
    
    conn = create_connection(database)

    if conn is not None:
        create_table(conn, make_author_table)
        create_table(conn, make_category_table)
        create_table(conn, make_book_table)
        create_table(conn, make_bookauthor_table)
        create_table(conn, make_user_table)

    else:
        print("Unnexpected Error, Could not Create Tables")


if __name__ == "__main__":
    main()
