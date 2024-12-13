import tkinter as tk
import random
import threading
import win32gui
import win32con
import keyboard  # For global hotkey detection

# Create the main window
root = tk.Tk()
root.attributes('-topmost', True)  # Always on top
root.attributes('-transparentcolor', 'white')  # Transparent background
root.geometry('100x100')  # Small initial size
root.overrideredirect(True)  # Remove title bar

# Configure the window to be transparent and non-intrusive
def make_window_transparent(hwnd):
    # Set the window style to allow transparency
    styles = win32gui.GetWindowLong(hwnd, win32con.GWL_EXSTYLE)
    win32gui.SetWindowLong(hwnd, win32con.GWL_EXSTYLE, styles | win32con.WS_EX_LAYERED | win32con.WS_EX_TRANSPARENT)
    win32gui.SetLayeredWindowAttributes(hwnd, 0x00FFFFFF, 255, win32con.LWA_COLORKEY)

# Get the window handle and apply transparency
hwnd = win32gui.FindWindow(None, root.title())
make_window_transparent(hwnd)

# Create the coin
coin = tk.Label(root, text="💰", font=("Arial", 30), bg="white")
coin.place(x=0, y=0)

# Animation variables
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

def move_coin():
    # Random start position
    y_pos = random.randint(0, screen_height - 50)
    coin.place(x=0, y=y_pos)
    
    # Drift across the screen
    for x_pos in range(0, screen_width, 5):
        coin.place(x=x_pos, y=y_pos)
        root.update()
        root.after(20)  # Adjust speed
    
    # Hide coin after it leaves the screen
    coin.place_forget()

# Start the coin movement at random intervals
def random_coin_spawner():
    while True:
        root.after(random.randint(5000, 15000), move_coin)  # Random 5-15 sec
        root.update_idletasks()
        root.update()

# Function to trigger a coin manually
def spawn_coin():
    move_coin()

# Background thread for hotkey detection
def hotkey_listener():
    while True:
        if keyboard.is_pressed('q') and keyboard.is_pressed('p'):
            spawn_coin()
            # Prevent multiple triggers by waiting until the keys are released
            while keyboard.is_pressed('q') or keyboard.is_pressed('p'):
                pass

# Start the hotkey listener in a separate thread
threading.Thread(target=hotkey_listener, daemon=True).start()

# Run the spawner
root.after(0, random_coin_spawner)
root.mainloop()
