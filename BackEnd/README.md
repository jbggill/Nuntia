# Backend Application

The Backend Application serves as the server-side component of the Nuntia browser extension. It provides functionalities to parse articles, analyze their political bias, and send the analysis results back to the extension.

## Requirements

To run the Backend Application, you need the following:

- Python 3.x
- Flask
- Transformers library from Hugging Face
- PyTorch

You can install the required packages using the following command:

``` {bash}
pip install flask transformers torch
```

## Getting Started

1. Clone this repository to your local machine.
2. Install the required packages as mentioned in the Requirements section.
3. Open a terminal or command prompt and navigate to the root folder of the backend application.

## Usage

To start the backend server, run the following command:
```{bash}
python app.py
```

The server will start running on `http://localhost:3001/`.

## Endpoints

The backend application provides a single endpoint for the Nuntia extension to interact with:

### POST / (root)

This endpoint handles the parsing and bias analysis of articles. The Nuntia extension can send either HTML content or a URL of the article to this endpoint. The backend will process the input data and respond with the political bias analysis results.

#### Request

The backend expects a JSON payload with either 'html' or 'url' data. Example requests:

Request with HTML data:

```json
{
  "html": "<p>This is the HTML content of the article...</p>"
}
``` 
Request with URL data:
```{json}
{
  "url": "https://example.com/article"
}
```
## Response
The backend will respond with a JSON object containing the political bias analysis results. The result will be a percentage distribution across 'left', 'center', and 'right' biases. Example response:
```{json}
{
  "left": 10.12,
  "center": 67.85,
  "right": 22.03
}
```
## Testing
The backend application includes test cases to ensure its functionality. To run the tests, execute the following command:
``` {bash}
python BE-test.py
```
