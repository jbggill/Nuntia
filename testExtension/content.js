function countWords(str) {
    return str.trim().split(/\s+/).length;
  }
  
  chrome.runtime.onMessage.addListener((request, sender, sendResponse) => {
    if (request.action === 'getWordCount') {
      let wordCount = 1000;
      sendResponse({wordCount: wordCount});
    }
  });
  