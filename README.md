# Product-88 📚

a small bookstore with BIG API capabilities 🦾

## Installation/Requirements 🔩

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install requirements. Virtual environment recommended.

```bash
pip install -r requirements.txt
```

## Demo/Usage 👤

```
-- start the server, that listen for HTTP requests on localhost --

py ./db/server.py


-- create new sqlite database (optional) --

# delete bookstore.db
py ./db/create_tables.py
#run all cells in populate_tables.ipynb

```

## Documentation (refer to images for additional) 🏫

- Books
    * **GET** 
    * **POST** - JSON Object ("title": str, "author": {str}, "year": int, "category": str, "rating": int, "price": int, "quantity": int 
- Books_By_id
    * **GET** - `/id`
    * **PUT** - - `/id`+ JSON Object ("title": str, "author": {str}, "year": int, "category": str, "rating": int, "price": int, "quantity": int
    * **DELETE** - `/id`
- Authors
    * **GET**
    * **POST**
- Authors_by_id
    * **GET** - `/id`
    * **PUT**
    * **DELETE** - `/id`
- Categories
    * **GET** 
    * **POST**
- Categories_by_id
    * **GET** - `/id`
    * **PUT**
    * **DELETE** - `/id`

## Contributing 🆘

Forks and Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.
