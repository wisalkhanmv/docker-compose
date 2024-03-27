from flask import Flask, render_template, request, jsonify
from flask_pymongo import PyMongo

app = Flask(__name__)
app.config['MONGO_URI'] = 'mongodb://localhost:27017/web_app_db'
mongo = PyMongo(app)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/submit', methods=['POST'])
def submit_data():
    # Get the JSON data from the request
    data = request.get_json()

    # Process the data (example: store it in the database)
    if data:
        # Assuming 'name' and 'email' are keys in the JSON data
        name = data.get('name')
        email = data.get('email')
        # Perform any necessary validation
        if name and email:
            # Store the data in the MongoDB database
            db = mongo.db.users
            db.insert_one({'name': name, 'email': email})
            return jsonify({'message': 'Data submitted successfully!'}), 200
        else:
            return jsonify({'error': 'Name and email fields are required.'}), 400
    else:
        return jsonify({'error': 'Invalid request format.'}), 400


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8081, debug=True)
