# clicker.py
import threading
import pyautogui
import time
from pynput.keyboard import Listener, Key

running = False
stop_thread = False


def auto_clicker():
    global running, stop_thread
    try:
        while running:
            if stop_thread:
                break
            x, y = pyautogui.position()
            pyautogui.click(x, y)
            time.sleep(0.001)  # Інтервал між кліками
    except Exception as e:
        print(f"Error in auto_clicker: {e}")
        running = False


def toggle_auto_clicker():
    global running, stop_thread
    if running:
        running = False
        stop_thread = True
    else:
        running = True
        stop_thread = False
        threading.Thread(target=auto_clicker).start()

def on_press(key):
    if key == Key.f9:
        toggle_auto_clicker()
    elif key == Key.esc:
        global running
        running = False
        global stop_thread
        stop_thread = True


def start_listener():
    with Listener(on_press=on_press) as listener:
        listener.join()


if __name__ == '__main__':
    start_listener()
