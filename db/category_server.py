from flask import Flask, request, jsonify
from connection import create_connection
import query_data as db
import create_data as create


app = Flask(__name__)

@app.route("/")
def home(name):
    return f"_"

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