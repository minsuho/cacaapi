from flask import Flask, render_template, request, jsonify
from flask_cors import CORS
import json


app = Flask(__name__)
CORS(app)

@app.route('/api/1')
def api1():
    file_path = "cadata2.json"
    with open(file_path, "r") as json_file:
        json_data = json.load(json_file)

    return jsonify(json_data)

@app.route('/api/2')
def api2():
    file_path = "cadata1.json"
    with open(file_path, "r") as json_file:
        json_data = json.load(json_file)

    return jsonify(json_data)


if __name__ == "__main__":
    app.run(debug=True)
