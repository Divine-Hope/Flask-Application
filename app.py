import sqlite3

from flask import Flask, request, jsonify
app = Flask(__name__)


def db_connection():
    conn = None
    try:
        conn = sqlite3.connect("books.sqlite")
    except sqlite3.error as e:
        print(e)
    return conn


def get_data_with_id(id_):
    conn = db_connection()
    cursor = conn.cursor()
    cursor.execute(f"SELECT * FROM book WHERE id={id_}")
    return [row for row in cursor.fetchall()]


@app.route('/')
def welcome():
    return "This app is working", 200


@app.route('/books', methods=['GET', 'POST'])
def books():
    conn = db_connection()
    if request.method == 'GET':
        cursor = conn.execute("SELECT * FROM book")
        books_ = [
            dict(
                id=row[0],
                author=row[1],
                language=row[2],
                title=row[3]) for row in cursor.fetchall()]

        if books_:
            return jsonify(books_), 200

        else:
            return "No books found!", 404

    if request.method == 'POST':
        new_author = request.form.get('author', '')
        new_lang = request.form.get('language', '')
        new_title = request.form.get('title', '')

        sql = """
                INSERT INTO book (author, language, title)
                VALUES (?, ?, ?)
        """

        cursor = conn.execute(sql, (new_author, new_lang, new_title))
        conn.commit()
        return f"Book with id {cursor.lastrowid} has been created successfully", 200


@app.route('/book/<int:id_>', methods=['GET', 'PUT', 'DELETE'])
def book_operations(id_):
    conn = db_connection()

    if request.method == 'GET':
        book = get_data_with_id(id_)

        if book:
            return jsonify(book[0]), 200
        else:
            return "Book Not Found!", 404

    if request.method == 'PUT':

        author = request.form.get('author', '')
        language = request.form.get('language', '')
        title = request.form.get('title', '')

        sql = f"""
                UPDATE book
                SET author = "{author}",
                    language = "{language}",
                    title = "{title}"
                WHERE id = {id_}
        """
        conn.execute(sql)
        conn.commit()

        book = get_data_with_id(id_)

        if book:
            return jsonify(book[0]), 200
        else:
            return "Book Not Found!", 404

    if request.method == 'DELETE':
        sql = f"DELETE from book where id = {id_}"
        conn.execute(sql)
        conn.commit()
        return f"The book with id= {id_} has been deleted", 200


@app.route('/bulk_load', methods=['POST'])
def bulk_insert():
    conn = db_connection()
    data = request.get_json()
    for item in data:
        id_ = item.get('id')
        author = item.get('author')
        language = item.get('language')
        title = item.get('title')

        sql = """
            INSERT INTO book (id, author, language, title)
            VALUES (?, ?, ?, ?)
        """
        conn.execute(sql, (id_, author, language, title))

    conn.commit()
    return f"{len(data)} has been uploaded to the DB", 201


if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0')
