function sendMessage() {
    var userInput = document.getElementById('user-input').value;
    if (userInput.trim() !== '') {
      displayMessage('user', userInput);
      // Add logic to send userInput to your backend for processing
      // Receive the chatbot's response and call displayMessage('bot', response);
      document.getElementById('user-input').value = ''; // Clear input field
    }
  }
  
  function displayMessage(role, content) {
    var chatDisplay = document.getElementById('chat-display');
    var messageDiv = document.createElement('div');
    messageDiv.className = role + '-message';
    messageDiv.innerHTML = '<strong>' + role.toUpperCase() + ':</strong> ' + content;
    chatDisplay.appendChild(messageDiv);
    chatDisplay.scrollTop = chatDisplay.scrollHeight; // Auto-scroll to the latest message
  }
  