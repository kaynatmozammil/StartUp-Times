from flask import Flask, render_template, redirect, url_for
import firebase_admin
from firebase_admin import credentials, firestore
from twilio.rest import Client

# Initialize Firebase
cred = credentials.Certificate("path/to/your/firebase-adminsdk.json")
firebase_admin.initialize_app(cred)
db = firestore.client()

# Twilio Configuration
TWILIO_ACCOUNT_SID = "your_twilio_account_sid"
TWILIO_AUTH_TOKEN = "your_twilio_auth_token"
TWILIO_WHATSAPP_NUMBER = "whatsapp:+14155238886"  # Twilio WhatsApp sandbox number

# Initialize Twilio client
twilio_client = Client(TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN)

# Flask app
app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/send_message', methods=['POST'])
def send_message():
    # Fetch a WhatsApp number from Firebase
    docs = db.collection('whatsapp_numbers').stream()
    for doc in docs:
        whatsapp_number = doc.to_dict().get('number')
        if whatsapp_number:
            # Send WhatsApp message
            message = twilio_client.messages.create(
                from_=TWILIO_WHATSAPP_NUMBER,
                body="Hello! This is an automated message.",
                to=f"whatsapp:{whatsapp_number}"
            )
            print(f"Message sent to {whatsapp_number}: {message.sid}")
            return redirect(url_for('home'))
    return "No numbers found in Firebase", 404

if __name__ == '__main__':
    app.run(debug=True)









# import pywhatkit as kit
# from datetime import datetime
#
# # Take input from the user
# phone_number = input("Enter the recipient's WhatsApp number (with country code, e.g., +1xxxxxxxxxx): ")
# message = input("Enter the message you want to send: ")
#
# # Get the current time
# # current_time = datetime.now()
# # hour = current_time.hour
# # minute = current_time.minute + 2  # Schedule the message 2 minutes ahead
#
# # Send the message
#
#
# # Replace with the recipient's phone number (with country code)
# # phone_number = "+1234567890"
# # message = "Hello! This message is automated using Pywhatkit."
#
# # Send the message instantly
# kit.sendwhatmsg_instantly(phone_number, message)