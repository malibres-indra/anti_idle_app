import pyautogui
import time
from pynput import mouse
import threading

def move_mouse():
    try:
        # Get the current mouse position
        x, y = pyautogui.position()
        
        # Move the mouse slightly to the right
        pyautogui.moveTo(x + 10, y)
        
        print("Mouse moved successfully")
    except Exception as e:
        print(f"Error moving mouse: {e}")

def on_move(x, y):
    print(f"Mouse moved to ({x}, {y})")

def mouse_listener_init():
    # Create a mouse listener
    with mouse.Listener(on_move=on_move) as listener:
        listener.join()  # Start listening for events

def mouse_anti_idle_init():  
    while True:
        move_mouse()
        time.sleep(1)  # Move the mouse every 60 seconds
    
    

if __name__ == "__main__":

    thread1 = threading.Thread(target=mouse_listener_init)  # Thread with a delay of 1 second
    thread2 = threading.Thread(target=mouse_anti_idle_init)  # Thread with a delay of 1 second

    thread1.start()
    thread2.start()

    try:
        # Main loop to continuously move the mouse
        while True:
            move_mouse()
            time.sleep(1)  # Move the mouse every 60 seconds
    except KeyboardInterrupt:
        print("\nStopping the anti-idle script.")
