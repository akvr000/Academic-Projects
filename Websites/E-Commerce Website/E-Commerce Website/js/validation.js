// Validation.js (javascript)

function validateForm() {
    var sellerName = document.getElementById("sellerName").value;
    var phoneNumber = document.getElementById("phoneNumber").value;
    var address = document.getElementById("address").value;

    if (sellerName.trim() === "" || phoneNumber.trim() === "" || address.trim() === "") {
        alert("Please fill in all fields.");
        return false;
    }
    return true;
}


