import pywhatkit as kit
import time
from datetime import datetime

# Get the current time
now = datetime.now()
current_hour = now.hour
current_minute = now.minute

# Add a small delay (e.g., 1 minute) to ensure the browser has time to load
current_minute += 1

# Phone number and message
phone_number = input("recipient's phone number (including country code and + sign): ")
message = input("What shall we send, sir? ")

# Ask how many times to send the message
sendRepeat = int(input("How many times, sir? "))

# Send the message multiple times
for i in range(sendRepeat):
    kit.sendwhatmsg(phone_number, message, current_hour, current_minute)

# Wait for a few seconds to ensure the browser can complete the action
time.sleep(60)  # This waits for 10 seconds, which might be needed to ensure the message is sent
