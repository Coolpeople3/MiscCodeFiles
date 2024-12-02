import pyautogui
import time

def move_cursor_smoothly():
    screen_width, screen_height = pyautogui.size()  # Get screen dimensions
    start_x = screen_width // 4  # Starting position (25% of screen width)
    end_x = 3 * screen_width // 4  # Ending position (75% of screen width)
    y = screen_height // 2  # Fixed vertical position

    try:
        while True:
            # Move right
            for x in range(start_x, end_x, 5):  # Increment cursor position in steps
                pyautogui.moveTo(x, y)
                time.sleep(0.001)  # Short delay for smooth movement

            # Move left
            for x in range(end_x, start_x, -5):  # Decrement cursor position in steps
                pyautogui.moveTo(x, y)
                time.sleep(0.01)  # Short delay for smooth movement

    except KeyboardInterrupt:
        print("Movement stopped by user.")

if __name__ == "__main__":
    print("Press Ctrl+C to stop the cursor movement.")
    move_cursor_smoothly()
