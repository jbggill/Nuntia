chrome.runtime.onMessage.addListener(async function (msg, sender, sendResponse) {
  if (msg.action === 'submit') {
    const currentTab = await chrome.tabs.query({ active: true, currentWindow: true });
    //console.log("body: ", msg.body);
    //console.log("url: ", currentTab[0].url);

    // Convert body to JSON string
    const requestBody = JSON.stringify({
      'html': msg.body
    });

    // Send the body to localhost:3001
    fetch('http://localhost:3001', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
      body: requestBody
    })
      .then(response => response.json())
      .then(bias => {
        console.log('Response from server:', bias);
        chrome.runtime.sendMessage({action: "setBiasScore", data:bias}, function(response) {
          console.log(response);
        });
      })
      .catch(error => {
        console.error('Error sending body to server:', error);
        sendResponse('error');
      });

    return true;
  }
});
