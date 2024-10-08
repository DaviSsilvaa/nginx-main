from flask import Flask, request
import requests

app = Flask(__name__)

@app.route('/send', methods=['POST'])
def send_message():
    message = request.json.get('message')
    if not message:
        return "Invalid request, 'message' not found", 400
    response = requests.post('http://message-receiver:5000/receive', json={'message': message})
    return response.text, response.status_code

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
