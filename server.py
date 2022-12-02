from MESA.main import generate_data
from flask import Flask, jsonify, request 
import math

app = Flask(__name__)

data = []
num_agents = 5 
steps = 0


@app.route("/steps")
def get_steps():
    return jsonify({"steps":steps})

@app.route("/cars")
def get_cars():
    return jsonify({"cars":num_agents})

@app.route('/data', methods=['GET'])
def get_data():
    return jsonify(data)


@app.route('/data/<int:id>', methods=['GET'])
def get_data_by_id(id):
    dato = []
    for data_item in data:
        if data_item['id'] == id:
            dato.append(data_item)
    return jsonify(dato) if len(dato) > 0 else jsonify({'message': 'data not found'})

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
    data = generate_data()
    steps = len([i for i in data if i['id'] == 0])
    app.run(port=3000, debug=True)







