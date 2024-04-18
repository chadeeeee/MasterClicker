import pyautogui
import customtkinter as ctk


def cursor_position(label_x, label_y):
    x, y = pyautogui.position()
    label_x.configure(text=f"x: {x}")
    label_y.configure(text=f"y: {y}")
    label_x.after(100, cursor_position, label_x, label_y)


w = ctk.CTk()
w.geometry("300x100")
w.title("Cursor Tracker")

label_x = ctk.CTkLabel(w, text="x: 0")
label_y = ctk.CTkLabel(w, text="y: 0")

label_x.pack()
label_y.pack()

cursor_position(label_x, label_y)

w.mainloop()
