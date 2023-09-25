
document.addEventListener("DOMContentLoaded", function () {
    const popupOverlay = document.getElementById("popup-overlay");
    const okButton = document.getElementById("welcome-ok");

    
    const hasPopupBeenShown = localStorage.getItem("hasPopupBeenShown");

    if (!hasPopupBeenShown) {
        
    
        popupOverlay.style.display = "flex";
    }


    okButton.addEventListener("click", function () {
        popupOverlay.style.display = "none";

       
        localStorage.setItem("hasPopupBeenShown", "true");
    });
});
