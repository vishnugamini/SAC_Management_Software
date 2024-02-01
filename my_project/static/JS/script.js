function redirectTo(url) {
    window.location.href = url;
}

// shows court and equipment buttons on submitting
function showHiddenElement() {
    var regNumInput = document.getElementById("reg-num-input").value.trim();

    // Check if the input is empty
    if (regNumInput === "") {
        alert("Please enter a registration number.");
    } else {
        var hiddenElement = document.getElementById("hidden-elements");
        hiddenElement.classList.add("visible");
        hiddenElement.style.display = "block";
    }
}
function clickingSubmit() {
    showHiddenElement();
}
