document.getElementById('read-content').addEventListener('click', () => {
  // Show the loading message
  document.getElementById('loading-message').style.display = 'block';
  // Hide the results
  document.getElementById('results-container').style.display = 'none';

  chrome.tabs.query({ active: true, currentWindow: true }, (tabs) => {
      const tab = tabs[0];

      function sendBody() {
          const contents = document.body.innerHTML;

          // Send the body to the background script
          chrome.runtime.sendMessage({ action: 'submit', body: contents }, (response) => {
              console.log(response);
              chrome.storage.local.set({ 'pageBias': response }, () => {
              });
          });
      }

      chrome.scripting.executeScript({
          target: { tabId: tab.id },
          func: sendBody,
      }).then(() => console.log('Injected sendBody()'));
  });
});

chrome.runtime.onMessage.addListener(function (request, sender, sendResponse) {
  if (request.action == "setBiasScore"){
      const data = request.data.message;
      if (data != null && data != ''){
          sendResponse('data received');
          console.log(data);
          const biasScoreElementLeft = document.getElementById('bias-score-left');
          biasScoreElementLeft.textContent = `Left: ${data.left}%`;

          const biasScoreElementRight = document.getElementById('bias-score-right');
          biasScoreElementRight.textContent = `Right: ${data.right}%`;

          const biasScoreElementCentre = document.getElementById('bias-score-center');
          biasScoreElementCentre.textContent = `Center: ${data.center}%`;

          // Set the slider values based on the received data
          document.getElementById('bias-slider-left').value = data.left;
          document.getElementById('bias-slider-right').value = data.right;
          document.getElementById('bias-slider-center').value = data.center;

          // Hide the loading message
          document.getElementById('loading-message').style.display = 'none';
          // Show the results
          document.getElementById('results-container').style.display = 'block';
      }
  }
});
