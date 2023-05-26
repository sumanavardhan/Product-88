from flask import Flask, request, jsonify
from connection import create_connection
import query_data as db
import create_data as create

app = Flask(__name__)
app.config['JSON_SORT_KEYS'] = False

@app.route("/")
def home(name):
    return f"_"


""" ---  BOOK REST API CALLS --- """

@app.route("/book", methods=["GET", "POST"])
def books():
    #GET BOOK
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
            for author in db.select_author_id(conn, book[0]): 
                authors.append(db.select_author(conn, author[1], "id")[1])
            category = db.select_category(conn, book[6], 'id')

            results.append({
                "name": book[1],
                "published": book[3],
                "author": authors,
                "category": category[1],
                "id": book[0]
            })
        conn.close()
        return results, 200
    
    #CREATE BOOK
    elif request.method == "POST":
        # Pipeline:
        # 1) Accept a dictionary to get title, price, year, quantity, authors, rating, category
        # 2) Check for category in category table, if exists assign as id, else create category
        # 3) Create book into table with above id
        # 4) Authors should be accepted as a JSON Object and a Dict
        # 5) Check for authors in Author Table, if they don't exist create them
        # 6) Create bookauthor records by querying for book_id and author id, inserting that as a new record

        # Accepts:
        """
        request.form["title"]: string,
        request.form["price"]: int,
        request.form["year"]: int,
        request.form["quantity"]: int,
        request.form["rating"]: string,
        request.form["category"]: int,

        request.form["author"]: dict,
        """

        conn = create_connection("bookstore.db")
        if request.form:
            book = create.insert_book(conn,{
                "title": request.form["title"],
                "author": request.form["author"], # can be a dict
                "year": request.form["year"],
                "category": request.form["category"],
                "rating": request.form["rating"],
                "price": request.form["price"],
                "quantity": request.form["quantity"]
            })

        else: # accounts for JSON
            book = create.insert_book(conn, request.json)
            
        """ --- BOOKAUTHOR ENTRY --- """

        book_id = book[0]
        author_ids = book[1]
        for id in author_ids :
            create.insert_bookauthor(conn, {
                "book_id": book_id,
                "author_id": id
            })
        
        conn.close()
        return jsonify(book_id), 201
        

@app.route("/api/book/<book_id>", methods=["GET", "PUT", "DELETE"])
def book_by_id(book_id):
    #READ BOOK
    if request.method == "GET":
        conn = create_connection("bookstore.db")
        book = db.select_book_id(conn, book_id)
        if book:
            result = {
                    "id": book[0][0],
                    "title":book[0][1],
                    "price":book[0][2],
                    "year":book[0][3],
                    "quantity":book[0][4],
                    "rating":book[0][5],
                    "category_id":book[0][6]
            }
            conn.close()
            return jsonify(result), 200
        else:
            return f"author with id {book_id} not found", 204

    
    # UPDATE BOOK
    elif request.method == "PUT":
        conn = create_connection("bookstore.db")
        book = db.select_book(conn, book_id)
        if book:
            if "title" in request.json:
                title = request.json["title"]
                db.update_book(conn,title,book_id,1)
            if "price" in request.json:
                price = request.json["price"]
                db.update_book(conn,price,book_id,2)
            if "year" in request.json:
                year = request.json["year"]
                db.update_book(conn,year,book_id,3)
            if "quantity" in request.json:
                quantity = request.json["quantity"]
                db.update_book(conn,quantity,book_id,4)
            if "rating" in request.json:
                rating = request.json["rating"]
                db.update_book(conn,rating,book_id,5)
            if "category_id" in request.json:
                category_id = request.json["category_id"]
                db.update_book(conn,category_id,book_id,6)
            conn.close()
            return f"Updated Book with id: {book_id}",202
        else:
            return f"Book with id {book_id} not found", 204
   
    # DELETE BOOK
    elif request.method == "DELETE":
        conn = create_connection("bookstore.db")
        book = db.select_book(conn, book_id)
        if book:
            db.delete_book(conn,book_id)
            conn.close()
            return f"Deleted Book with id: {book_id}",202
        else:
            return f"Book with id {book_id} not found", 204


""" ---  AUTHOR REST API --- """

@app.route("/author", methods=["GET", "POST"])
def author():
    if request.method == "GET":
        conn = create_connection("bookstore.db")
        results = []
        for author in db.all_authors(conn):
            results.append({
                "id":author[0],
                "name": author[1]
            })
        conn.close()
        return results, 200
    
    elif request.method == "POST":
        conn = create_connection("bookstore.db")
        if request.form:
            author = create.insert_author(conn,{
                "name":request.form["name"]
            })
            conn.close()
            return jsonify(author), 201
        else:
        # CREATE AUTHOR
            author = create.insert_author(conn, request.json)
            conn.close()
            return jsonify(author), 201

@app.route("/api/author/<author_id>", methods=["GET", "PUT", "DELETE"])
def author_by_id(author_id):
    #READ AUTHOR
    if request.method == "GET":
        conn = create_connection("bookstore.db")
        author = db.select_author(conn, author_id, "id")
        if author:
            result = {
                    "id": author[0],
                    "name":author[1]
            }
            conn.close()
            return result, 200
        else:
            return f"author with id {author_id} not found", 204
    elif request.method == "PUT":
        # UPDATE AUTHOR
        conn = create_connection("bookstore.db")
        author = db.select_author(conn, author_id, "id")
        if author:
            name = request.json["name"]
            db.update_author(conn,name,author_id)
            conn.close()
            return f"Updated author with id: {author_id}",202
        else:
            return f"author with id {author_id} not found", 204
    elif request.method == "DELETE":
        # DELETE AUTHOR
        conn = create_connection("bookstore.db")
        author = db.select_author(conn, author_id, "id")
        if author:
            db.delete_author(conn,author_id)
            conn.close()
            return f"Deleted author with id: {author_id}",202
        else:
            return f"author with id {author_id} not found", 204

""" ---  CATEGORY REST API --- """

@app.route("/category", methods=["GET", "POST"])
def category():
    if request.method == "GET":
        conn = create_connection("bookstore.db")
        results = []
        for category in db.all_categories(conn):
            results.append({
                "id":category[0],
                "name": category[1]
            })
        conn.close()
        return results, 200
    
    elif request.method == "POST":
        conn = create_connection("bookstore.db")
        if request.form:
            category = create.insert_category(conn,{
                "name":request.form["name"],
            })
            conn.close()
            return jsonify(category), 201
        else:
            # CREATE CATEGORY
            category = create.insert_category(conn, request.json)
            conn.close()
            return jsonify(category), 201

@app.route("/api/category/<category_id>", methods=["GET", "PUT", "DELETE"])
def category_by_id(category_id):
    # READ CATEGORY
    if request.method == "GET":
        conn = create_connection("bookstore.db")
        category = db.select_category(conn, category_id, "id")
        if category:
            result = {
                    "id": category[0],
                    "name":category[1]
            }
            conn.close()
            return result, 200
        else:
            return f"Category with id {category_id} not found", 204
        
    # UPDATE CATEGORY
    elif request.method == "PUT":
        conn = create_connection("bookstore.db")
        category = db.select_category(conn, category_id, "id")
        if category:
            name = request.json["name"]
            db.update_caegory(conn,name,category_id)
            conn.close()
            return f"Updated category with id: {category_id}",202
        else:
            return f"Category with id {category_id} not found", 204
    
    # DELETE CATEGORY
    elif request == "DELETE":
        conn = create_connection("bookstore.db")
        category = db.select_category(conn, category_id, "id")
        if category:
            db.delete_category(conn,category_id)
            conn.close()
            return f"Deleted category with id: {category_id}",202
        else:
            return f"Category with id {category_id} not found", 204


if __name__ == "__main__":
    app.run(debug=True)
