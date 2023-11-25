# Nuntia - Web Content Sharing and Political Bias Analysis

Nuntia is a browser extension and server application that allows users to read web content and analyze its political bias. The extension can extract the text from the currently active tab or take a URL as input and send it to the server for analysis. The server performs the analysis using a pre-trained model and returns the results back to the extension.

## Features

- Read web content from the currently active tab or using a URL.
- Analyze the political bias of the extracted content.
- Supports various Chromium-based browsers.
- Provides a user-friendly interface for interaction.

## Architecture

The Nuntia application is divided into two main components:

1. **Frontend (Browser Extension)**: The frontend is a browser extension that users can install and interact with while browsing web content. It provides a popup window and a button to trigger the content reading and submission process.

2. **Backend (Server Application)**: The backend is a server-side application that handles the content parsing and political bias analysis. It receives requests from the frontend, processes the content, and sends back the analysis results.

## Technologies Used

- **Frontend**: HTML, CSS, JavaScript, and the Chrome Extension API.
- **Backend**: Python, Flask (a lightweight web framework), Transformers library from Hugging Face, and PyTorch.

## Installation

To use the Nuntia browser extension, follow these steps:

1. Clone this repository to your local machine.
2. Install the required packages for the backend as mentioned in the backend README.
3. Open a terminal or command prompt and navigate to the root folder of the backend application.
4. Run the backend server using the command: `python app.py`.
5. Load the extension in your browser:
   - For Google Chrome or Chromium-based browsers:
     1. Open the browser and navigate to `chrome://extensions/`.
     2. Enable Developer Mode by toggling the switch in the top right corner.
     3. Click on "Load unpacked" and select the folder containing the frontend files.
   - For Microsoft Edge or other supported browsers, follow similar steps as in Chrome.

## Usage

Once the Nuntia extension is installed and the backend server is running, you can use the extension as follows:

1. Click on the extension icon in your browser's toolbar to open the extension popup.
2. Click the "Read content" button to extract the content from the currently active tab or use the "Read URL" option to provide a URL for content extraction.
3. The extension will send the content to the backend server for political bias analysis.
4. The server will process the content and respond with the political bias analysis results.
5. The extension will display the analysis results as a percentage distribution across 'left', 'center', and 'right' biases.

## Testing

The backend application includes test cases to ensure its functionality. To run the tests, execute the following command:
```{bash}
python BE-test.py
```

## Contributions

