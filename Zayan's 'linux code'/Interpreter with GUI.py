import tkinter as tk
from tkinter import ttk

def cipher(text):
    """Converts text into its numeric representation."""
    result = []
    for letter in text.lower():
        if letter.isalpha():
            number = ord(letter) - 96
            if number > 9:
                result.append(f"({number})")
            else:
                result.append(str(number))
        elif letter == " ":
            result.append("(27)")  # Use (27) for space
    return " ".join(result)

def decipher(code):
    """Converts numeric code into the corresponding text message."""
    result = []
    code = code.replace("(", "").replace(")", "").split()
    for number in code:
        if number == "27":  # (27) represents a space
            result.append(" ")
        elif number.isdigit():
            letter = chr(int(number) + 96)
            result.append(letter)
    return "".join(result)

def run_cipher():
    input_text = text_area.get("1.0", tk.END).strip()
    output_text = cipher(input_text)
    output_display.config(state=tk.NORMAL)
    output_display.delete("1.0", tk.END)
    output_display.insert(tk.END, output_text)
    output_display.config(state=tk.DISABLED)

def run_decipher():
    input_text = text_area.get("1.0", tk.END).strip()
    output_text = decipher(input_text)
    output_display.config(state=tk.NORMAL)
    output_display.delete("1.0", tk.END)
    output_display.insert(tk.END, output_text)
    output_display.config(state=tk.DISABLED)

def switch_to_cipher():
    clear_text_areas()
    text_area_label.config(text="Enter Text to Cipher")
    run_button.config(command=run_cipher)
    output_display.config(state=tk.NORMAL)
    output_display.delete("1.0", tk.END)
    output_display.config(state=tk.DISABLED)

def switch_to_decipher():
    clear_text_areas()
    text_area_label.config(text="Enter Code to Decipher")
    run_button.config(command=run_decipher)
    output_display.config(state=tk.NORMAL)
    output_display.delete("1.0", tk.END)
    output_display.config(state=tk.DISABLED)

def clear_text_areas():
    text_area.delete("1.0", tk.END)
    output_display.config(state=tk.NORMAL)
    output_display.delete("1.0", tk.END)
    output_display.config(state=tk.DISABLED)

# Set up main window
root = tk.Tk()
root.title("Cipher-IDE")
root.geometry("800x600")
root.configure(bg="#2b2b2b")

# Style configuration
style = ttk.Style()
style.theme_use("clam")
style.configure("TButton", font=("Courier New", 12), background="#3c3f41", foreground="#a9b7c6")
style.configure("TLabel", background="#2b2b2b", foreground="#a9b7c6", font=("Courier New", 12))

# Cipher and Decipher buttons
cipher_button = ttk.Button(root, text="Cipher", command=switch_to_cipher)
cipher_button.place(x=50, y=20, width=100, height=30)

decipher_button = ttk.Button(root, text="Decipher", command=switch_to_decipher)
decipher_button.place(x=160, y=20, width=100, height=30)

# Text area label
text_area_label = ttk.Label(root, text="Select an option above")
text_area_label.place(x=50, y=70)

# Text area (input)
text_area = tk.Text(root, wrap=tk.WORD, font=("Courier New", 12), background="#313335", foreground="#ffffff", insertbackground="white")
text_area.place(x=50, y=100, width=700, height=200)

# Run button
run_button = ttk.Button(root, text="Run", command=run_cipher)
run_button.place(x=50, y=320, width=100, height=30)

# Output area (result display)
output_display_label = ttk.Label(root, text="Output")
output_display_label.place(x=50, y=360)

output_display = tk.Text(root, wrap=tk.WORD, font=("Courier New", 12), background="#313335", foreground="#ffffff", insertbackground="white", state=tk.DISABLED)
output_display.place(x=50, y=390, width=700, height=150)

root.mainloop()
