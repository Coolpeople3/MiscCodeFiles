import pyautogui
import keyboard
import time

print("Welcome to Hitarth's autoclicker!")
print("Press 'K' to toggle the autoclicker on/off.")
print("Press 'Ctrl+C' to stop the script.")

running = False  # Tracks if the autoclicker is active

try:
    while True:
        # Toggle autoclicker state with spacebar
        if keyboard.is_pressed('k'):
            running = not running
            print(f"{'Started' if running else 'Paused'} autoclicker!")
            time.sleep(0.2)  # Prevent rapid toggling

        # Perform clicking when active
        if running:
            pyautogui.click()
except KeyboardInterrupt:
    print("Autoclicker stopped.")
