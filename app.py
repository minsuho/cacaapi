from flask import Flask, render_template, request, jsonify
import json
import caapi


app = Flask(__name__)
app.config['JSON_AS_ASCII'] = False

@app.route('/')
def api():
    caapi.api1()
    caapi.api2()
    print('ok')
    return'hi'

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
