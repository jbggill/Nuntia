document.getElementById('read-content').addEventListener('click', () => {
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
     const data = request.data.message
     if (data != null && data != ''){
      sendResponse('data recieved')
      console.log(data)
      console.log(data.left)
      const biasScoreElementLeft = document.getElementById('page-bias-value-left');
      biasScoreElementLeft.textContent = `Left: ${data.left}%`;

      const biasScoreElementRight = document.getElementById('page-bias-value-right');
      biasScoreElementRight.textContent = `Right: ${data.right}%`;

      const biasScoreElementCentre = document.getElementById('page-bias-value-center');
      biasScoreElementCentre.textContent = `Center: ${data.center}%`;
     }
    }
})


