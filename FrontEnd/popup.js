window.onload = function() {
  var submitButton = document.getElementById("submitButton");
  submitButton.addEventListener("click", function() {
    console.log('submit clicked -- popup.js')
    chrome.runtime.sendMessage({ action: "submit" });
  });
}
