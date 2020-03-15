from flask import Flask, jsonify

app = Flask(__name__)

books = [
    {
        'name': 'Green egges and hams',
        'price': '$3.67',
        'isbn': 78900765478
    },
    {
        'name': 'The cat in the hat',
        'price': '$9.67',
        'isbn': 98765465544
    }
]
@app.route('/')
def welcome():
    return "welcome to book store"

@app.route('/books/')
def books_page():
    return jsonify({'books': books})

#POST /books
#   {
#        'name': 'Green egges and hams',
#        'price': '$3.67',
#        'isbn': 78900765478
#    }

@app.route('/bookss', methods=['POST'])
def add_book():
    pass

#GET /books
@app.route('/books/<int:isbn>')
def get_book_by_isbn(isbn):
    return_value = {}
    for book in books:
        if book['isbn'] == isbn:
            return_value = {
                'name': book['name'],
                'price': book['price'],
                'isbn': book['isbn']
            }
    return jsonify(return_value)

app.run(port=3300)


#JSON=> Javascript object notataion




