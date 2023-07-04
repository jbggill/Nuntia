window.onload = function() {
  var submitButton = document.getElementById("submitButton");
  submitButton.addEventListener("click", function() {
    chrome.runtime.sendMessage({ action: "submit" });
  });
}
