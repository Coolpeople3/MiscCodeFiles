import pywhatkit as kit
import time

print("This is Hitarth's whatsapp message sending service")
# Phone number and message
phone_number = input("Recipient's phone number (including country code and + sign): ")
message = input("What shall we send, sir? ")

# Ask how many times to send the message
sendRepeat = int(input("How many times, sir? "))

# Send the message multiple times instantly
for i in range(sendRepeat):
    kit.sendwhatmsg_instantly(phone_number, message)

    # Wait for 10 seconds between sending messages to ensure WhatsApp has time to process
    time.sleep(10)
