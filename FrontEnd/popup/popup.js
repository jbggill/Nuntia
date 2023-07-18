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
      $('#bias-slider-left').val(data.left);
      $('#bias-slider-right').val(data.right);
      $('#bias-slider-center').val(data.center);
    }
  }
});

// Handle slider input events to update the bias percentages
/** 
$('.slider-container input[type="range"]').on('input', function() {
  const sliderId = this.id;
  const sliderValue = this.value;
  const biasScoreElement = document.getElementById(`bias-score-${sliderId.replace('bias-slider-', '')}`);
  biasScoreElement.textContent = `${sliderId.replace('bias-slider-', '').replace('-', ' ')}: ${sliderValue}%`;

  // Send updated slider values to the background script
  chrome.runtime.sendMessage({
    action: 'updateBiasScore',
    data: {
      left: $('#bias-slider-left').val(),
      right: $('#bias-slider-right').val(),
      center: $('#bias-slider-center').val(),
    }
  }, (response) => {
    console.log(response);
  });
});
*/