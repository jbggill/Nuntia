from flask import Flask, request
import json
import political_bias
import article_processor
app = Flask(__name__)

@app.route('/', methods=['POST'])
def log_data():
    data = request.get_json()
    print("Received data:", data)
    contents = article_processor.getContents('https://www.foxnews.com/media/democratic-strategist-scolds-biden-not-recognizing-seventh-grandchild-humanity')
    bias = political_bias.BERT(contents[:len(contents)//2])
    print(bias)
    response = {
        "message":bias
    }

    return json.dumps(response)


if __name__ == '__main__':
    app.run(port=3001)
