from flask import Flask, request
import json
# import political_bias
app = Flask(__name__)

@app.route('/', methods=['POST'])
def log_data():
    data = request.get_json()
    # Do whatever you want with the data
    # Here, we simply print it to the console
    print("Received data:", data)
    response = {
        "data recieved"
    }
    return json.dump(response)

@app.route("/",methods=['GET'])
def hello_world():
    return "<p>Hello World!</p>"

if __name__ == '__main__':
    app.run(port=3001)
