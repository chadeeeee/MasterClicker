import sqlite3 as sq
import customtkinter
from pynput.keyboard import Key, Listener

button_hotkey = None

conn = sq.connect('database.db')
cur = conn.cursor()

cur.execute('''
CREATE TABLE IF NOT EXISTS db (
button INTEGER PRIMARY KEY,
)
''')

conn.commit()


def on_press(key):
    global button_hotkey
    try:
        button_hotkey = key.char  # Якщо натиснута символьна клавіша
    except AttributeError:
        button_hotkey = str(key)  # Якщо натиснута не символьна клавіша
    print(f"Кнопка: {button_hotkey}")
    key_label.configure(text=str(button_hotkey))  # Використовуйте метод configure


def bind_button():
    global button_hotkey
    cur.execute("INSERT INTO db(button) VALUES (?)", ("button_hotkey"))
    conn.commit()
    conn.close()


def rebind():
    global key_label, bind_window
    if 'bind_window' in globals():
        bind_window.focus_force()
        return

    bind_window = customtkinter.CTkToplevel()
    bind_window.geometry("300x200")
    bind_window.title("Bind a new hotkey")

    prompt_label = customtkinter.CTkLabel(bind_window, text="Натисни шось", font=("Roboto", 12))
    prompt_label.pack(pady=20)

    key_label = customtkinter.CTkLabel(bind_window, text="", font=("Roboto", 12))
    key_label.pack()

    bind_btn = customtkinter.CTkButton(bind_window, text="Bind", command=bind_button)
    bind_btn.pack(pady=10)

    # Починаємо відстежувати натискання клавіш
    listener = Listener(on_press=on_press)
    listener.start()

    # Функція для зупинки відстеження натискання клавіш при закритті вікна
    def stop_listener():
        listener.stop()
        bind_window.destroy()

    bind_window.protocol("WM_DELETE_WINDOW", stop_listener)
