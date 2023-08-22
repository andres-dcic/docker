from flask import Flask
from flask import jsonify

app = Flask(__name__)

@app.route('/books', methods=["GET"])
def get_books():
    Books = [
        {
            "title": "Harry Potter",
            "author": "JK Rowling"
        },
        {
            "title": "Animal Farm",
            "author": "George Orwell"
        },
        {
            "title": "Animal Farm2",
            "author": "George Orwell2"
        }
    ]
    return jsonify(Books)


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
