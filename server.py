from flask import Flask, request
import pywhatkit as kit

app = Flask(__name__)

@app.route('/send_message', methods=['POST'])
def send_message():
    data = request.json
    phone_number = data['phone']
    message = data['message']
    kit.sendwhatmsg_instantly(phone_number, message)
    return {"status": "Message sent"}

if __name__ == '__main__':
    app.run(debug=True)
