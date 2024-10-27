# chatbox.py 
# plan to implement this in the main backend code and give suggestions


from flask import Flask, request, jsonify
from flask_cors import CORS
from text_generator import process_question  # Import the process_question function from chatbot.py

app = Flask(__name__)
CORS(app)  # Enable CORS for all routes

@app.route('/chat', methods=['POST'])
def ask_question():
    data = request.json
    question = data.get("question", "")
    # Generate a response using the process_question function from chatbot.py
    answer = process_question(question)
    return jsonify({"answer": answer})

if __name__ == '__main__':
    app.run(debug=True)
