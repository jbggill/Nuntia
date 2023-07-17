document.getElementById('read-content').addEventListener('click', () => {
  chrome.tabs.query({ active: true, currentWindow: true }, (tabs) => {
    const tab = tabs[0];
    console.log(tabs)
    function sendBody() {
      const contents = document.body.innerHTML;
      console.log(contents);

      // Send the body to the background script
      chrome.runtime.sendMessage({ action:'submit', body: contents}, (response) => {
        console.log(response);
      });
    }

    chrome.scripting.executeScript({
      target: { tabId: tab.id },
      func: sendBody,
    }).then(() => console.log('Injected a sendBody()'));
  });
});
