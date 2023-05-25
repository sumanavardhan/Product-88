from flask import Flask, request, jsonify
from connection import create_connection
import query_data as db
import create_data as create

app = Flask(__name__)

@app.route("/")
def home(name):
    return f"_"


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
    
    
if __name__ == "__main__":
    app.run(debug=True)