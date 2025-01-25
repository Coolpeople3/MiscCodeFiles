import tkinter
import pyautogui
import threading
import time
import cv2

moving_cursor = False
photo_taken = False
photo_counter = 1

def take_photo():
    global photo_taken, photo_counter
    if not photo_taken:
        cap = cv2.VideoCapture(0)
        if not cap.isOpened():
            print("Error: Unable to access the webcam.")
            return
        ret, frame = cap.read()
        if ret:
            photo_filename = f"CatchClose Photo number {photo_counter}.jpg"
            cv2.imwrite(photo_filename, frame)
            print(f"Photo taken: {photo_filename}")
            photo_counter += 1
        cap.release()
        photo_taken = True

def move_cursor_to_red_box():
    global moving_cursor, photo_taken
    red_box_x = red_box.winfo_rootx() + red_box.winfo_width() / 2
    red_box_y = red_box.winfo_rooty() + red_box.winfo_height() / 2
    x, y = pyautogui.position()
    start_time = time.time()
    while moving_cursor and (abs(x - red_box_x) > 1 or abs(y - red_box_y) > 1):
        x_step = (red_box_x - x) * 0.05
        y_step = (red_box_y - y) * 0.05
        x += x_step
        y += y_step
        pyautogui.moveTo(x, y, duration=0.01)
        time.sleep(0.01)
        if time.time() - start_time > 4.5 and not photo_taken:
            threading.Thread(target=take_photo).start()
    pyautogui.moveTo(red_box_x, red_box_y)
    moving_cursor = False
    photo_taken = False

def on_mouse_move(event):
    global moving_cursor
    button_x, button_y = close_button.winfo_rootx(), close_button.winfo_rooty()
    button_width, button_height = close_button.winfo_width(), close_button.winfo_height()
    if (button_x - 50 < event.x_root < button_x + button_width + 50 and
        button_y - 50 < event.y_root < button_y + button_height + 50 and not moving_cursor):
        moving_cursor = True
        threading.Thread(target=move_cursor_to_red_box).start()

def close_app():
    print("Haha you thought you could close me!")

root = tkinter.Tk()
root.geometry("600x400")
root.title("Press the close button below to exit!")

title_label = tkinter.Label(root, text="Press the close button below to exit!", font=("Arial", 16))
title_label.place(relx=0.5, rely=0.2, anchor=tkinter.CENTER)

close_button = tkinter.Button(root, text="Close", command=close_app)
close_button.place(relx=0.5, rely=0.5, anchor=tkinter.CENTER)

red_box = tkinter.Canvas(root, width=50, height=50, bg="red")
red_box.place(relx=0.8, rely=0.5, anchor=tkinter.CENTER)

root.bind('<Motion>', on_mouse_move)
root.mainloop()
