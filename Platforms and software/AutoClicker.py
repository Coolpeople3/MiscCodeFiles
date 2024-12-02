import pyautogui
import time
delay = float(input("How long delay? Enter in seconds, decimals accepted.  "))
print("Welcome to Hitarth's autoclicker!")

try:
    print("Press Ctrl+C to stop the script.")
    while True:
        pyautogui.click()
        time.sleep(delay)  # Delay
except KeyboardInterrupt:
    print("Autoclicker Stopped")
