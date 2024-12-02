import pyautogui
import time
import keyboard

print("Welcome to Hitarth's autoclicker!")
delay = float(input("How long delay? Enter in seconds (0 for maximum speed): "))
print("Press 'Space' to toggle the autoclicker on/off.")
print("Press 'Ctrl+C' to stop the script.")

running = False  # Tracks if the autoclicker is active

try:
    while True:
        # Toggle autoclicker state with spacebar
        if keyboard.is_pressed('space'):
            running = not running
            print(f"{'Started' if running else 'Paused'} autoclicker!")
            time.sleep(0.5)  # Prevent rapid toggling

        # Perform clicking when active
        if running:
            pyautogui.click()
            if delay > 0:
                time.sleep(delay)  # Apply delay for controlled speed
except KeyboardInterrupt:
    print("Autoclicker stopped.")
