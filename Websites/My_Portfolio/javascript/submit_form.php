<?php
if ($_SERVER["REQUEST_METHOD"] == "POST") {
    // Sanitize form inputs
    $name = htmlspecialchars($_POST['name']);
    $email = htmlspecialchars($_POST['email']);
    $phone = htmlspecialchars($_POST['phone']);
    $subject = htmlspecialchars($_POST['subject']);
    $message = htmlspecialchars($_POST['message']);

    // Set recipient email address
    $to = "akvr000@gmail.com";

    // Compose email message
    $subject = "New Form Submission";
    $message_body = "Name: $name\n";
    $message_body .= "Email: $email\n";
    $message_body .= "Phone: $phone\n";
    $message_body .= "Subject: $subject\n";
    $message_body .= "Message: $message\n";

    // Set SMTP server settings
    ini_set("SMTP", "smtp.google.com");
    ini_set("smtp_port", "587"); // Use the appropriate port for your SMTP server

    // Send email
    

    // Set additional headers
    $headers = "From: $email" . "\r\n" .
               "Reply-To: $email" . "\r\n" .
               "X-Mailer: PHP/" . phpversion();

    // Send email
    if (mail($to, $subject, $message_body, $headers)) {
        // Email sent successfully
        echo "Thank you for contacting us!";
    } else {
        // Error sending email
        echo "Oops! Something went wrong. Please try again later.";
    }
} else {
    // No form data received
    echo "No data received.";
}
?>

