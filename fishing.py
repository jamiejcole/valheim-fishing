import time
import pyautogui
from pynput import keyboard

active = False
start_time = None
right_hold_duration = 0
toggle_time = None

def toggle_activation():
    global active, start_time, toggle_time
    active = not active
    toggle_time = time.time()
    
    if not active:
        pyautogui.mouseUp(button='left')
        pyautogui.mouseUp(button='right')

    if active and start_time is None:
        start_time = time.time()
    
    print("Activated" if active else "Deactivated")

def on_press(key):
    if hasattr(key, 'char') and key.char == 'o':  # Check if 'o' was pressed
        toggle_activation()

listener = keyboard.Listener(on_press=on_press)
listener.start()

try:
    while True:
        if active:
            pyautogui.mouseDown(button='left')
            time.sleep(0.55)
            pyautogui.mouseUp(button='left')

            right_start = time.time()
            pyautogui.mouseDown(button='right')
            time.sleep(9)
            pyautogui.mouseUp(button='right')
            right_hold_duration += time.time() - right_start
        time.sleep(0.01)  # Small delay to reduce CPU usage
except KeyboardInterrupt:
    total_runtime = int(time.time() - start_time) if start_time else 0
    runtime_hhmmss = f"{total_runtime // 3600:02}:{(total_runtime % 3600) // 60:02}:{total_runtime % 60:02}"
    right_hhmmss = f"{int(right_hold_duration) // 3600:02}:{(int(right_hold_duration) % 3600) // 60:02}:{int(right_hold_duration) % 60:02}"
    
    print(f"\nExiting gracefully...\nTotal runtime: {runtime_hhmmss} (hh:mm:ss)\nRight hold duration: {right_hhmmss} (hh:mm:ss)")
    pyautogui.mouseUp(button='left')
    pyautogui.mouseUp(button='right')
