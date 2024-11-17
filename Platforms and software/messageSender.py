import pyautogui as auto
import time

print("Welcome to Hitarth's Auto Messenger!")
print("Instructions:")
print("1. Answer the prompts below.")
print("2. After starting, click on the typing area in a messaging app where you want the messages to be sent.")
print("3. The script will automatically send the messages as per your input.\n")

rep = int(input("How many times should the message be sent? "))
text = input("What message should be sent? ")

print("\nStarting in 5 seconds. Get ready!")
time.sleep(5)

for i in range(rep):
    auto.write(text)
    auto.press('enter')
    time.sleep(1)

input("\nMessages sent! Press Enter to exit.")
