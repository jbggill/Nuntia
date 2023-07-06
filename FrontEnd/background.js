chrome.runtime.onMessage.addListener(async function (msg, sender, sendResponse) {
  // ...check the URL of the active tab against our pattern and...
  if (msg.action === 'submit') {
    console.log("body: ", msg.body);
    
    // Send the body to localhost:3001
    fetch('http://localhost:3001', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
      body: msg.body,
    })
      .then(response => response.json())
      .then(data => {
        console.log('Response from server:', data);
        sendResponse('received');
      })
      .catch(error => {
        console.error('Error sending body to server:', error);
        sendResponse('error');
      });
      
    // Indicate that the message is being handled asynchronously
    return true;
  }
});
