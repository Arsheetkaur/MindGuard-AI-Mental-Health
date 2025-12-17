function sendMessage() {
    const input = document.getElementById("userInput");
    const chatBox = document.getElementById("chatBox");

    const userText = input.value.trim();
    if (userText === "") return;

    // User message
    const userMessage = document.createElement("div");
    userMessage.className = "user-message";
    userMessage.innerText = userText;
    chatBox.appendChild(userMessage);

    input.value = "";

    // Temporary bot reply
    setTimeout(() => {
        const botMessage = document.createElement("div");
        botMessage.className = "bot-message";
        botMessage.innerText = "I hear you. Tell me more 💙";
        chatBox.appendChild(botMessage);

        chatBox.scrollTop = chatBox.scrollHeight;
    }, 800);
}
