function submitForm(event) {
    event.preventDefault();

    var formData = new FormData(document.getElementById('contact-form'));

    fetch('submit_form.php', {
        method: 'POST',
        body: formData
    })
    .then(response => response.text())
    .then(data => {
        document.getElementById('form-details').innerHTML = data;
        openPopup();
    })
    .catch(error => console.error('Error:', error));
}

function openPopup() {
    document.getElementById('popup').style.display = 'flex';
}

function closePopup() {
    document.getElementById('popup').style.display = 'none';
}
