import tkinter as tk

# Initialize the main window
root = tk.Tk()  # This should be 'tk.Tk()', not 'tk.tk()'

# Set title and geometry for the main window
root.title("Hitarth learning Tkinter")
root.geometry("300x200")

# Add a label widget
label = tk.Label(root, text="This is a button")
label.pack()

# Define the function to change label text
def change_text():
    label.config(text="button clicked")

# Add a button widget and link it to the change_text function
button = tk.Button(root, text="click me", command=change_text)
button.pack()

# Start the main loop to display the window
root.mainloop()
