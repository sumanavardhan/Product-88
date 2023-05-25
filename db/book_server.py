from flask import Flask, request, jsonify
from connection import create_connection
import query_data as db
import create_data as create

app = Flask(__name__)
app.config['JSON_SORT_KEYS'] = False

@app.route("/")
def home(name):
    return f"_"


@app.route("/book", methods=["GET", "POST"])
def books():
    if request.method == "GET":
        conn = create_connection("bookstore.db")
        books = db.all_books(conn)
        results = []
        
        for book in books:
            """
            book:
                - book_id
                - title
                - price
                - year
                - quantity
                - rating
                - category_id
            """

            authors = []
            for author in db.select_book_id(conn, book[0]): 
                authors.append(db.select_author(conn, author[1], "id")[1])
            category = db.select_category(conn, book[6], id)

            results.append({
                "name": book[1],
                "published": book[3],
                "author": authors,
                "category": category[1],
                "id": book[0]
            })
        conn.close()
        return results, 200
    
    elif request.method == "POST":
        conn = create_connection("bookstore.db")
        if request.form:
            book = create.insert_book(conn,{
                "name":request.form["name"],
                "author":request.form["author"],
                "category":request.form["category"],
                "published":request.form["published"],
            })
            conn.close()
            return render_template("index.html"), 201
        else:
            book = create.insert_book(conn, request.json)
            conn.close()
            return jsonify(book), 201

@app.route("/api/book/<book_id>", methods=["GET", "PUT", "DELETE"])
def book_by_id(book_id):
    if request.method == "GET":
        conn = create_connection("bims.db")
        book = qd.select_book(conn, book_id)
        if book:
            author = qd.select_author(conn, book[3], "id")
            category = qd.select_category(conn, book[4], id)
            result = {
                    "name":book[1],
                    "published": book[2],
                    "author": author[1],
                    "category": category[1]
            }
            conn.close()
            return result, 200
        else:
            return f"book with id {book_id} not found", 204
    elif request.method == "PUT":
       # TODO: implement book query
       # book = request.json()
       # update_book(book_id, book)
       return f"Updated book with id: {book_id}"
    elif request == "DELETE":
        # TODO: implement delete book
        # delete_book(book_id)
        return f"deleted book with id {book_id}"

if __name__ == "__main__":
    app.run(debug=True)
    
    
if __name__ == "__main__":
    app.run(debug=True)