import pyautogui
import time
import random

# Constants for click coordinates
COOK_CLICK = (924, 465)
COOK_START = (843, 607)
RS_CLICK = (905, 907)
CLOSE_CLICK = (14, 51)
BANK_CLICK = (731, 352)
PRESET_CLICK = (700, 410)

# Constants for coordinate randomization
COORDINATE_OFFSET = 10

# Constants for time intervals
MIN_INTERVAL = 65  # 65 seconds
MAX_INTERVAL = 75  # 75 seconds

# Set the total runtime in seconds (3 hours)
total_runtime = 3 * 60 * 60

# Record the start time
start_time = time.time()


def perform_actions():
    # Sleep before start cooking
    time.sleep(3)

    # Randomize click coordinates
    cook_click = (COOK_CLICK[0] + random.randint(-COORDINATE_OFFSET, COORDINATE_OFFSET),
                  COOK_CLICK[1] + random.randint(-COORDINATE_OFFSET, COORDINATE_OFFSET))
    pyautogui.click(cook_click, duration=0.25)  # Click cooking range with duration
    time.sleep(2)

    # Start cook
    cook_start = (COOK_START[0] + random.randint(-COORDINATE_OFFSET, COORDINATE_OFFSET),
                  COOK_START[1] + random.randint(-COORDINATE_OFFSET, COORDINATE_OFFSET))
    pyautogui.click(cook_start, duration=0.25)  # Click to start cooking with duration

    # Add a random sleep time between MIN_INTERVAL and MAX_INTERVAL
    interval = random.randint(MIN_INTERVAL, MAX_INTERVAL)
    time.sleep(interval)

    # Right-click at bank_click coordinate
    pyautogui.rightClick(BANK_CLICK, duration=0.25)
    time.sleep(3)  # Wait for 3 seconds

    # Left-click at preset_click coordinate
    pyautogui.click(PRESET_CLICK, duration=0.25)  # Use a duration to simulate a more natural click
    time.sleep(2)  # Wait for 2 seconds


if __name__ == "__main__":
    # Sleep before opening RS
    time.sleep(3)
    pyautogui.click(RS_CLICK)  # Click to open RS

    # Perform actions in a loop
    while True:
        # Check if the total elapsed time exceeds 3 hours
        if time.time() - start_time > total_runtime:
            # Close RS before stopping the script
            pyautogui.click(CLOSE_CLICK)
            print("Script has run for 3 hours. Stopping the script.")
            break

        perform_actions()
