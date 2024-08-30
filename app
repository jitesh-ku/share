from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

# A function to generate a response from the chatbot
def generate_response(user_input):
    # Replace this with your actual chatbot logic or API call
    return f"You said: {user_input}"

@app.route('/')
def index():
    return render_template('chat.html')

@app.route('/chat', methods=['POST'])
def chat():
    user_input = request.form['message']
    response = generate_response(user_input)
    return jsonify({'response': response})

if __name__ == '__main__':
    app.run(debug=True)
