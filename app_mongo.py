from flask import Flask, request, jsonify
from pymongo import MongoClient
from bson.objectid import ObjectId

app = Flask(__name__)


def db_connection(mongo_ip):
    client = MongoClient(f'mongodb://{mongo_ip}:27017/')
    db = client['bookstore']
    books_collection = db['books']
    return books_collection


NOT_FOUND_RESP = "Book Not Found!"


@app.route('/')
def welcome():
    return f"This app is working, ip is {request.args.get('ip')}", 200


@app.route('/books', methods=['GET', 'POST'])
def books():
    if request.method == 'GET':
        books_collection = db_connection(request.args.get('ip'))
        books_ = [
            {**book, '_id': str(book.get('_id'))}
            for book in books_collection.find()
        ]

        if books_:
            limit = int(request.args.get('limit')) if request.args.get('limit') else None
            books_ = books_[:limit]
            return jsonify(books_), 200

        else:
            return NOT_FOUND_RESP, 404

    if request.method == 'POST':
        books_collection = db_connection(request.args.get('ip'))
        new_author = request.form.get('author', '')
        new_lang = request.form.get('language', '')
        new_title = request.form.get('title', '')

        new_book = {"author": new_author, "language": new_lang, "title": new_title}
        result = books_collection.insert_one(new_book)

        return f"Book with id {result.inserted_id} has been created successfully", 200


@app.route('/book/<string:id_>', methods=['GET', 'PUT', 'DELETE'])
def book_operations(id_):
    if request.method == 'GET':
        books_collection = db_connection(request.args.get('ip'))
        book = books_collection.find_one({"_id": ObjectId(id_)})

        if book:
            book['_id'] = str(book['_id'])  # Convert ObjectId to string
            return jsonify(book), 200
        else:
            return NOT_FOUND_RESP, 404

    if request.method == 'PUT':
        books_collection = db_connection(request.args.get('ip'))
        author = request.form.get('author', '')
        language = request.form.get('language', '')
        title = request.form.get('title', '')

        result = books_collection.update_one(
            {"_id": ObjectId(id_)},
            {"$set": {"author": author, "language": language, "title": title}}
        )

        if result.matched_count == 0:
            return NOT_FOUND_RESP, 404

        book = books_collection.find_one({"_id": ObjectId(id_)})
        book['_id'] = str(book['_id'])  # Convert ObjectId to string
        return jsonify(book), 200

    if request.method == 'DELETE':
        books_collection = db_connection(request.args.get('ip'))
        result = books_collection.delete_one({"_id": ObjectId(id_)})

        if result.deleted_count == 0:
            return NOT_FOUND_RESP, 404

        return f"The book with id {id_} has been deleted", 200


@app.route('/bulk_load', methods=['POST'])
def bulk_insert():
    books_collection = db_connection(request.args.get('ip'))
    data = request.get_json()
    result = books_collection.insert_many(data)

    return f"{len(result.inserted_ids)} books have been uploaded to the DB", 201


if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0')
