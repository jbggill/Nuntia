chrome.runtime.onMessage.addListener((message, sender, sendResponse) => {
  if (message.action === "sendDOM") {
    setTimeout(() => sendResponse({message : "processed"}), 1000)
    return true
  }
});
chrome.runtime.sendMessage({ something: 'to be sent' }, (response) => {
  return true
});