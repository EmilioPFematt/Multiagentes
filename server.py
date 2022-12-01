
from flask import Flask, jsonify, request 

app = Flask(__name__)

data = [
    {
        'id': 1,
        'x': 3,
        'y': 25,
    },
    {
        'id': 2,
        'x': 5,
        'y': 25,
    },
    {
        'id': 3,
        'x': 15,
        'y': 5,
    },
    {
        'id': 4,
        'x': 1,
        'y': 8,
    },
    {
        'id': 5,
        'x': 5,
        'y': 1,
    }
]

@app.route('/data', methods=['GET'])
def get_data():
    return jsonify({'data': data})


@app.route('/data/<int:id>', methods=['GET'])
def get_data_by_id(id):
    for data_item in data:
        if data_item['id'] == id:
            return jsonify({'data': data_item})
    return jsonify({'message': 'data not found'})

@app.route('/data', methods=['POST'])
def add_data():
    new_data = {
        'id': request.json['id'],
        'name': request.json['name'],
        'age': request.json['age'],
        'occupation': request.json['occupation']
    }
    data.append(new_data)
    return jsonify({'data': data})

@app.route('/data/<int:id>', methods=['PUT'])
def update_data(id):
    for data_item in data:
        if data_item['id'] == id:
            data_item['id'] = request.json['id']
            data_item['name'] = request.json['name']
            data_item['age'] = request.json['age']
            data_item['occupation'] = request.json['occupation']
            return jsonify({'data': data_item})
    return jsonify({'message': 'data not found'})

if __name__ == '__main__':
    app.run(port=3000, debug=True)







