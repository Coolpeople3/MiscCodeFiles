import tkinter as tk
from tkinter import ttk
import pygame
from datetime import datetime, timedelta
import sys

# Initialize Pygame
pygame.init()

# Main app class
class PercentageOfDayTimer:
    def __init__(self, root):
        self.root = root
        self.root.title("Percentage of Day Timer")
        self.root.geometry("400x300")
        self.root.configure(bg="lightgrey")

        # Default wake-up and sleep times
        self.wake_time = datetime.now().replace(hour=7, minute=0, second=0)
        self.sleep_time = datetime.now().replace(hour=23, minute=0, second=0)

        # Create header with settings button
        header = tk.Frame(self.root, bg="lightgrey")
        header.pack(fill=tk.X, pady=10)

        settings_button = tk.Button(
            header, text="Settings", command=self.open_settings, bg="#4285F4", fg="white"
        )
        settings_button.pack(side=tk.LEFT, padx=10)

        # Main display label for percentage
        self.percentage_label = tk.Label(
            self.root, text="", font=("Arial", 36), fg="#4285F4", bg="lightgrey"
        )
        self.percentage_label.pack(expand=True)

        # Start updating the percentage
        self.update_percentage()

    def update_percentage(self):
        # Calculate percentage of day that has passed
        now = datetime.now()
        day_duration = (self.sleep_time - self.wake_time).total_seconds()
        time_elapsed = (now - self.wake_time).total_seconds()
        
        # Bound time_elapsed within the duration of the day
        if time_elapsed < 0:
            percentage = 0
        elif time_elapsed > day_duration:
            percentage = 100
        else:
            percentage = (time_elapsed / day_duration) * 100

        # Update percentage display
        self.percentage_label.config(text=f"{int(percentage)}%")

        # Schedule next update
        self.root.after(1000, self.update_percentage)

    def open_settings(self):
        settings_window = tk.Toplevel(self.root)
        settings_window.title("Settings")
        settings_window.geometry("300x200")
        settings_window.configure(bg="lightgrey")

        tk.Label(settings_window, text="Wake Up Time (HH:MM):", bg="lightgrey").pack(pady=5)
        self.wake_entry = tk.Entry(settings_window)
        self.wake_entry.pack(pady=5)
        self.wake_entry.insert(0, self.wake_time.strftime("%H:%M"))

        tk.Label(settings_window, text="Sleep Time (HH:MM):", bg="lightgrey").pack(pady=5)
        self.sleep_entry = tk.Entry(settings_window)
        self.sleep_entry.pack(pady=5)
        self.sleep_entry.insert(0, self.sleep_time.strftime("%H:%M"))

        save_button = tk.Button(
            settings_window, text="Save", command=self.save_settings, bg="#34A853", fg="white"
        )
        save_button.pack(pady=20)

    def save_settings(self):
        # Parse and save the new wake-up and sleep times
        try:
            wake_time_str = self.wake_entry.get()
            sleep_time_str = self.sleep_entry.get()

            self.wake_time = datetime.strptime(wake_time_str, "%H:%M").replace(
                year=datetime.now().year,
                month=datetime.now().month,
                day=datetime.now().day
            )
            self.sleep_time = datetime.strptime(sleep_time_str, "%H:%M").replace(
                year=datetime.now().year,
                month=datetime.now().month,
                day=datetime.now().day
            )

            # Close settings window
            self.wake_entry.master.destroy()
        except ValueError:
            # Handle invalid input gracefully
            tk.messagebox.showerror("Invalid Time", "Please enter a valid time format (HH:MM).")

# Initialize main Tkinter root window
root = tk.Tk()
app = PercentageOfDayTimer(root)
root.mainloop()
pygame.quit()
sys.exit()
