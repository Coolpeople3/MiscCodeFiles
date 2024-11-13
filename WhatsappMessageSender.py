import pywhatkit as kit
import time
from datetime import datetime

# Get the current time
now = datetime.now()
current_hour = now.hour
current_minute = now.minute

# Phone number and message
phone_number = input("Recipient's phone number (including country code and + sign): ")
message = input("What shall we send, sir? ")

# Ask for the time to send the message
time_hour = int(input(f"Enter the hour to send the message (0-23): "))
time_minute = int(input(f"Enter the minute to send the message (0-59): "))

# Ask how many times to send the message
sendRepeat = int(input("How many times, sir? "))

# Send the message multiple times
for i in range(sendRepeat):
    kit.sendwhatmsg(phone_number, message, time_hour, time_minute)

    # Wait for a few seconds before sending again
    time.sleep(10)  # Optional: Adjust this if you want to wait more or less between messages
