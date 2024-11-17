import pyautogui as auto
import time

rep = int(input("How many times, sir? "))
text = input("What shall we send, sir? ")

for i in range(rep):
    auto.write(text)
    auto.press('enter')
    time.sleep(1)
