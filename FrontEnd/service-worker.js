chrome.runtime.onMessage.addListener( (sender, message, sendResponse) =>  {
  if (request.action === "submit") {
      console.log("submit stage 1")
      const response_tabs = sendMessageToActiveTab('sendDOM')
      console.log(response_tabs)
      const response_runtime = chrome.runtime.sendMessage({message: 'sendDOM', action: 'sendDOM'})
      console.log(response_runtime)
  }
})


async function getCurrentTab() {
  let queryOptions = { active: true, lastFocusedWindow: true };
  // `tab` will either be a `tabs.Tab` instance or `undefined`.
  let [tab] = await chrome.tabs.query(queryOptions);
  return tab;
}

async function sendMessageToActiveTab(message) {
  const [tab] = await chrome.tabs.query({ active: true, lastFocusedWindow: true });
  const response = await chrome.tabs.sendMessage(tab.id, {message: message, action: 'sendDOM'});
  return response
}