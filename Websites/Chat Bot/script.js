// Function to send message by pressing Enter button
document.getElementById("user-input").addEventListener("keyup", function(event) {
    event.preventDefault();
    if (event.keyCode === 13) {
        sendMessage();
    }
});

function sendMessage() {
    var userInput = document.getElementById("user-input").value;
    if (userInput !== "") {
        var chatBox = document.getElementById("chat-box");
        var userMessage = document.createElement("div");
        userMessage.className = "chat-message user";
        userMessage.textContent = userInput;
        chatBox.appendChild(userMessage);
        document.getElementById("user-input").value = "";
        
        // Bot response
        setTimeout(function() {
            var botMessage = document.createElement("div");
            botMessage.className = "chat-message bot";
            var response = getBotResponse(userInput);
            botMessage.textContent = response;
            chatBox.appendChild(botMessage);
            chatBox.scrollTop = chatBox.scrollHeight;
        }, 500);
    }
}

function getBotResponse(userInput) {
    // Predefined responses
    var responses = {
        "hello": "Hello there!",
        "how are you": "I'm just a bot, but thanks for asking!",
        "goodbye": "Goodbye! Have a great day!",
        "default": "Sorry, I'm not sure how to respond to that."
    };

    // Check if the user's message matches any predefined responses
    userInput = userInput.toLowerCase();
    for (var key in responses) {
        if (userInput.includes(key)) {
            return responses[key];
        }
    }

    // If no match is found, return a default response
    return responses["default"];
}
