import threading
import pyautogui
import time
import keyboard
import mouse

running = False
stop_thread = False
# Припускаємо, що clicker.py має такий вигляд
button = None


def update_button(new_button):
    global button
    button = new_button
    print(f"Змінна button оновлена: {button}")


# Інші функції в файлі...


def auto_clicker():
    global running, stop_thread
    try:
        while running:
            if stop_thread:
                break
            x, y = mouse.get_position()
            pyautogui.click(x, y)
            time.sleep(0.001)
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


def on_press(event):
    if event.name == button:
        toggle_auto_clicker()


def start_listener():
    keyboard.on_press(on_press)
    keyboard.wait('esc')


if __name__ == '__main__':
    start_listener()
