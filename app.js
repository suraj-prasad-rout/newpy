// script.js
document.addEventListener("DOMContentLoaded", function () {
    const popupOverlay = document.getElementById("popup-overlay");
    const okButton = document.getElementById("welcome-ok");

    // Check if the pop-up has been shown before
    const hasPopupBeenShown = localStorage.getItem("hasPopupBeenShown");

    if (!hasPopupBeenShown) {
        // Show the pop-up if it hasn't been shown before
        popupOverlay.style.display = "flex";
    }

    // Add an event listener to the "Ok" button to close the pop-up
    okButton.addEventListener("click", function () {
        popupOverlay.style.display = "none";

        // Set a flag in local storage to indicate that the pop-up has been shown
        localStorage.setItem("hasPopupBeenShown", "true");
    });
});
