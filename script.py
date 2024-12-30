#
# import pywhatkit as kit
#
# # Replace with the recipient's phone number (with country code)
# phone_number = "+917033384974"
# message = "Hello! This message is automated using Pywhatkit."
#
# # Send the message instantly
# kit.sendwhatmsg_instantly(phone_number, message)
#
#
#

# import sys
# import pywhatkit as kit
#
# def send_whatsapp_message(phone_number, message):
#     try:
#         # Send the WhatsApp message instantly
#         kit.sendwhatmsg_instantly(phone_number, message)
#         print("Message sent successfully!")
#     except Exception as e:
#         print(f"Failed to send message: {str(e)}")
#
# if __name__ == "__main__":
#     # Get the phone number and message from command-line arguments
#     if len(sys.argv) < 2:
#         print("Usage: python script.py <phone_number>")
#         sys.exit(1)
#
#     phone_number = sys.argv[1]
#     message = "Hello! This message is automated using Pywhatkit."
#     send_whatsapp_message(phone_number, message)
#


# import sys
# import pywhatkit as kit
#
# if len(sys.argv) < 2:
#     print("Phone number argument missing!")
#     sys.exit(1)
#
# phone_number = sys.argv[1]
# message = "Hello! This is an automated message sent via Pywhatkit."
#
# try:
#     kit.sendwhatmsg_instantly(phone_number, message)
#     print("Message sent successfully!")
# except Exception as e:
#     print(f"Error: {str(e)}")


import sys
import pywhatkit as kit

if len(sys.argv) < 2:
    print("Phone number argument missing!")
    sys.exit(1)

phone_number = sys.argv[1]
message = "Hello! This is an automated message sent via Pywhatkit."

try:
    # Send the WhatsApp message instantly
    kit.sendwhatmsg_instantly(phone_number, message)
    print("Message sent successfully!")
except Exception as e:
    print(f"Error: {str(e)}")
    sys.exit(1)

