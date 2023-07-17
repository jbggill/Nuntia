# Nuntia

Nuntia is a browser extension that allows you to read and submit content from the currently active tab to a specified server. With Nuntia, you can easily share webpage contents with your preferred server for further analysis or processing.

## Installation

1. Clone this repository to your local machine.
2. Open Google Chrome or any Chromium-based browser that supports Manifest V3 extensions.
3. Navigate to `chrome://extensions/` (or `edge://extensions/` for Microsoft Edge).
4. Enable Developer Mode by toggling the switch in the top right corner.
5. Click on "Load unpacked" and select the folder containing this extension's files.

## How to Use

Once the extension is installed, you can use it to read content from the currently active tab and submit it to a server. Here's how to do it:

1. Click on the extension icon in your browser's toolbar to open the extension popup.
2. Click the "Read content" button.

## Technical Details

This extension consists of the following files:

1. `popup.html`: The popup window that appears when you click on the extension icon. It allows you to trigger content reading and submission.

2. `styles.css`: The CSS file that styles the `popup.html`.

3. `manifest.json`: The extension's manifest file, which contains metadata and configurations for the extension. It sets up the `popup.html` as the default popup when the extension icon is clicked, registers a service worker in `background.js`, and defines content scripts to inject the `cs.js` script into all URLs.

4. `background.js`: The background script that listens for messages from the content script (`cs.js`). When it receives a 'submit' action, it extracts the current tab's URL, sends it to a specified server using a POST request, and handles the server's response.

5. `cs.js`: The content script that runs on all webpages and adds an event listener to the "Read content" button in the `popup.html`. When clicked, it extracts the webpage's HTML content and sends it to the background script for submission.

## Permissions

This extension requires the following permissions to function correctly:

- `activeTab`: To access the currently active tab and extract its URL and content.
- `tabs`: To query for tabs and get information about the currently active tab.
- `scripting`: To execute scripts in the context of web pages.

Additionally, the extension has specified "externally_connectable" and "host_permissions" to enable communication with specific servers and access to HTTP/HTTPS URLs.

## Note

Please note that this README provides an overview of the extension and its functionality. Detailed implementation and further customization can be found in the respective source files.

## Contributions

Contributions to this project are welcome. Feel free to submit bug reports, feature requests, or pull requests on the project's GitHub repository.

Thank you for using Nuntia! If you have any questions or encounter any issues, don't hesitate to reach out. Happy browsing and content sharing!
