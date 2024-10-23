// src/components/Chatbot.js
import React, { useState } from 'react';

const Chatbot = () => {
  const [messages, setMessages] = useState([
    { user: 'bot', text: 'Hello! How can I assist you with your stock trading?' },
  ]);
  const [input, setInput] = useState('');

  const sendMessage = () => {
    setMessages([...messages, { user: 'me', text: input }]);
    // Here you'd send 'input' to the LLM API, and get a response
    setInput('');
  };

  return (
    <div style={styles.container}>
      <div style={styles.chatWindow}>
        {messages.map((message, index) => (
          <div key={index} style={message.user === 'me' ? styles.myMessage : styles.botMessage}>
            {message.text}
          </div>
        ))}
      </div>
      <input
        type="text"
        style={styles.input}
        value={input}
        onChange={(e) => setInput(e.target.value)}
        placeholder="Ask me something..."
      />
      <button style={styles.button} onClick={sendMessage}>Send</button>
    </div>
  );
};

const styles = {
  container: { padding: '20px' },
  chatWindow: { border: '1px solid #ddd', height: '400px', padding: '10px', overflowY: 'scroll' },
  myMessage: { textAlign: 'right', padding: '10px', backgroundColor: '#f0f0f0', marginBottom: '5px' },
  botMessage: { textAlign: 'left', padding: '10px', backgroundColor: '#d0d0f0', marginBottom: '5px' },
  input: { padding: '10px', width: '80%', marginRight: '10px' },
  button: { padding: '10px', backgroundColor: '#4CAF50', color: 'white', border: 'none', cursor: 'pointer' },
};

export default Chatbot;
