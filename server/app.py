import uuid
from flask import Flask, jsonify, request
from flask_cors import CORS

STUDENTS = [
    {
        'id': uuid.uuid4().hex,
        'name': 'Harry Potter',
        'description': 'A book about a wizard',
    },
    {
        'id': uuid.uuid4().hex,
        'name': 'The Hobbit',
        'description': 'A book about a hobbit',
    },
]

# configuration
DEBUG = True

# instantiate the app
app = Flask(__name__)
app.config.from_object(__name__)

# enable CORS
CORS(app)


# sanity check route
@app.route('/api/ping', methods=['GET'])
def ping_pong():
    return jsonify('pong!')


@app.route('/api/students', methods=['GET', 'POST'])
def all_books():
    response_object = {'status': 'success'}
    if request.method == 'POST':
        post_data = request.get_json()
        STUDENTS.append({
            'id': uuid.uuid4().hex,
            'name': post_data.get('name'),
            'description': post_data.get('description'),
        })
        response_object['message'] = 'Book added!'
    else:
        response_object['students'] = STUDENTS
    return jsonify(response_object)


@app.route('/api/students/', methods=['PUT'])
def single_book(book_id):
    response_object = {'status': 'success'}
    if request.method == 'PUT':
        post_data = request.get_json()
        remove_book(book_id)
        STUDENTS.append({
            'id': uuid.uuid4().hex,
            'name': post_data.get('name'),
            'description': post_data.get('description'),
        })
        response_object['message'] = 'Book updated!'
    return jsonify(response_object)


def remove_book(book_id):
    for book in STUDENTS:
        if book['id'] == book_id:
            STUDENTS.remove(book)
            return True
    return False


if __name__ == '__main__':
    app.run()
