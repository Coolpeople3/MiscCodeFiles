import pywhatkit as kit
import time
from datetime import datetime

# Get the current time
now = datetime.now()
current_hour = now.hour
current_minute = now.minute

# Add a small delay (e.g., 2 seconds)
current_minute += 0.1  # Adjust the minute by adding 1 minute, or you can use current time + few seconds

# Phone number and message
phone_number = input("recipient's phone number (including country code and + sign) ")
message = "Hello, this is an instant message from Python!"

# Send the message
sendRepeat = int(input("How many times? "))

for i in range (sendRepeat):
  kit.sendwhatmsg(phone_number, message, current_hour, current_minute)
