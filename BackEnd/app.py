from flask import Flask, request, jsonify
from article_processor import ArticleParser
from political_bias import BiasAnalyzer

app = Flask(__name__)
bias_analyzer = BiasAnalyzer()

@app.route('/', methods=['POST'])
def handle_post():
    data = request.get_json()

    # Check if 'html' or 'url' exists in the received data
    if 'html' in data:
        print('recieved html data')
        # If 'html' exists, set the HTML content in the parser
        parser = ArticleParser('')
        parser.set_html(data['html'])
    elif 'url' in data:
        print('recieved url data')
        # If 'url' exists, set the URL in the parser and download the article
        parser = ArticleParser(data['url'])
        parser.download()
    else:
        print('did not receive valid data')
        # If neither 'html' nor 'url' exists, return an error response
        error = {'error': 'insufficient information to parse the article'}
        return jsonify(error)

    parser.parse()  # Parse the article
    contents = parser.get_text()  # Get the parsed text content of the article

    # Process the contents using BiasAnalyzer
    bias = bias_analyzer.analyze(contents[len(contents) // 2])
    print(bias)

    # Prepare the response
    response = {"message": bias}
    return jsonify(response)

if __name__ == '__main__':
    app.run(port=3001)
