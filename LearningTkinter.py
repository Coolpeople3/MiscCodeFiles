import tkinter as tk

# Initialize the main window
root = tk.Tk()

# Set title and geometry for the main window
root.title("Hitarth learning Tkinter")
root.geometry("300x200")

# Add a label widget
label = tk.Label(root, text="This is a button")
label.pack()

# Define the function to change label text
def change_text():
    label.config(text="Button clicked")

def turn_green():
    green.config(text="Green")

def button3():
    b3.config(text="button 3")
    
# Add buttons and link them to their functions
button = tk.Button(root, text="Click Me", command=change_text)
button.pack()

green = tk.Button(root, text="Click This", command=turn_green)
green.pack()

buttonThree = tk.Button(root, text="click this also", command=button3)
buttonThree.pack()
# Start the main loop to display the window
root.mainloop()
