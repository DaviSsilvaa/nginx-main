from flask import Flask, request

app = Flask(__name__)

@app.route('/receive', methods=['POST'])
def receive_message():
    message = request.json.get('message')
    print(f"Received message: {message}")  # Adicione esta linha
    return f"Message received: {message}", 200

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
