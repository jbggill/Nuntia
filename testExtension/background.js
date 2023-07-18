window.onload = function() {
  chrome.storage.sync.get('wordCount', function(data) {
    document.getElementById('wordCount').textContent = "Wordcount: " + (data.wordCount || 'Error: Could not get word count');
  });
}
