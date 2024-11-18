import tkinter as tk

# Initialize the loops counter and loops per second tracker
loops = 1
loops_per_second = 0

# Function to update label text when the "eat frootloops" button is clicked
def on_button_click():
    global loops
    loops += 1
    frootCount.config(text=str(loops))
    jen.config(text="Frootloops eaten!")
    rateDisplay.config(text=f"Loops per second: {round(loops_per_second, 2)}")
    update_powerups()

# Function to activate the first power-up
def powerUp1Clicked():
    global loops, loops_per_second
    if loops >= 30:
        loops -= 30
        loops_per_second += 0.33
        jen.config(text="Power-up 1 activated!")
        increment_loops_1()
        update_powerups()

# Function to increment loops every 3 seconds
def increment_loops_1():
    global loops
    loops += 1
    frootCount.config(text=str(loops))
    root.after(3000, increment_loops_1)

# Function to activate the second power-up
def powerUp2Clicked():
    global loops, loops_per_second
    if loops >= 60:
        loops -= 40
        loops_per_second += 1
        jen.config(text="Power-up 2 activated!")
        increment_loops_2()
        update_powerups()

# Function to increment loops by 3 every 3 seconds
def increment_loops_2():
    global loops
    loops += 3
    frootCount.config(text=str(loops))
    root.after(3000, increment_loops_2)

# Function to activate the third power-up
def powerUp3Clicked():
    global loops, loops_per_second
    if loops >= 100:
        loops -= 100
        loops_per_second += 5
        jen.config(text="Power-up 3 activated!")
        increment_loops_3()
        update_powerups()

# Function to increment loops by 5 every second
def increment_loops_3():
    global loops
    loops += 5
    frootCount.config(text=str(loops))
    root.after(1000, increment_loops_3)

# Function to update the visibility of power-ups
def update_powerups():
    if loops >= 30:
        powerUp1.pack(pady=10)
    else:
        powerUp1.pack_forget()
    if loops >= 60:
        powerUp2.pack(pady=10)
    else:
        powerUp2.pack_forget()
    if loops >= 100:
        powerUp3.pack(pady=10)
    else:
        powerUp3.pack_forget()

# Create the main window
root = tk.Tk()
root.title("Hitarth's IdleFrootloop Eater")
root.geometry("700x500")

# Create labels and buttons
frootCount = tk.Label(root, text=str(loops), font=("Impact", 30))
frootCount.pack(pady=10)

jen = tk.Label(root, text="Welcome to the Frootloop Eater!", font=("Arial", 14))
jen.pack(pady=20)

froot = tk.Button(root, text="Eat Frootloops", command=on_button_click)
froot.pack(pady=10)

rateDisplay = tk.Label(root, text=f"Loops per second: {round(loops_per_second, 2)}", font=("Arial", 12))
rateDisplay.pack(pady=10)

powerUp1 = tk.Button(root, text="+1 loop every 3 seconds (Cost: 30 loops)", command=powerUp1Clicked)
powerUp2 = tk.Button(root, text="+3 loops every 3 seconds (Cost: 60 loops)", command=powerUp2Clicked)
powerUp3 = tk.Button(root, text="+5 loops every second (Cost: 100 loops)", command=powerUp3Clicked)

# Start the Tkinter event loop
update_powerups()  # Initial check for power-ups
root.mainloop()
