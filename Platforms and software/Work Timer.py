import tkinter as tk
from tkinter import ttk

class PomodoroTimer:
    def __init__(self, root):
        self.root = root
        self.root.title("Hitarth's Work Timer")
        self.root.geometry("400x300")
        
        # Title and subtitle
        title = tk.Label(root, text="Hitarth's Work Timer", font=("Arial", 18, "bold"))
        title.pack(pady=10)
        subtitle = tk.Label(root, text="It actually works!", font=("Arial", 12))
        subtitle.pack()

        # Input fields for work and break time
        self.setup_input_frame()
        
        # Timer and progress bar
        self.timer_label = tk.Label(root, text="Time Remaining: 00:00", font=("Arial", 14))
        self.timer_label.pack(pady=20)
        
        self.progress = ttk.Progressbar(root, orient="horizontal", length=300, mode="determinate")
        self.progress.pack(pady=10)
        
        # Initialize timer values
        self.time_left = 0
        self.is_work_time = True
        self.total_time = 0

    def setup_input_frame(self):
        input_frame = tk.Frame(self.root)
        input_frame.pack(pady=10)

        tk.Label(input_frame, text="Work Time (minutes):").grid(row=0, column=0)
        self.work_time_entry = tk.Entry(input_frame, width=5)
        self.work_time_entry.grid(row=0, column=1)

        tk.Label(input_frame, text="Break Time (minutes):").grid(row=1, column=0)
        self.break_time_entry = tk.Entry(input_frame, width=5)
        self.break_time_entry.grid(row=1, column=1)
        
        start_button = tk.Button(self.root, text="Start Timer", command=self.start_timer)
        start_button.pack(pady=10)

    def start_timer(self):
        work_time = int(self.work_time_entry.get()) * 60
        break_time = int(self.break_time_entry.get()) * 60
        self.is_work_time = True
        self.total_time = work_time
        self.time_left = work_time
        self.progress["maximum"] = self.total_time
        self.update_timer()

    def update_timer(self):
        minutes, seconds = divmod(self.time_left, 60)
        self.timer_label.config(text=f"Time Remaining: {minutes:02d}:{seconds:02d}")
        self.progress["value"] = self.total_time - self.time_left
        
        if self.time_left > 0:
            self.time_left -= 1
            self.root.after(1000, self.update_timer)
        else:
            self.is_work_time = not self.is_work_time
            self.switch_phase()

    def switch_phase(self):
        if self.is_work_time:
            self.total_time = int(self.work_time_entry.get()) * 60
        else:
            self.total_time = int(self.break_time_entry.get()) * 60
        self.time_left = self.total_time
        self.progress["maximum"] = self.total_time
        self.update_timer()

root = tk.Tk()
app = PomodoroTimer(root)
root.mainloop()
