from flask import Flask, request, jsonify
from flask_pymongo import PyMongo

app = Flask(__name__)
app.config['MONGO_URI'] = 'mongodb://localhost:27017/web_app_db'
mongo = PyMongo(app)


@app.route('/submit', methods=['POST'])
def submit_data():
    data = request.get_json()
    if data:
        name = data.get('name')
        email = data.get('email')
        if name and email:
            db = mongo.db.users
            db.insert_one({'name': name, 'email': email})
            return jsonify({'message': 'Data submitted successfully!'}), 200
        else:
            return jsonify({'error': 'Name and email fields are required.'}), 400
    else:
        return jsonify({'error': 'Invalid request format.'}), 400

# Route to retrieve data from the database


@app.route('/users', methods=['GET'])
def get_users():
    db = mongo.db.users
    # Exclude _id field from the response
    users_list = list(db.find({}, {'_id': 0}))
    return jsonify(users_list), 200


if __name__ == '__main__':
    app.run(debug=True)
