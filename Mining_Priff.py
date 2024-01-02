import pyautogui
import time
import random

# Constants for click coordinates
CLAY_CLICK = (730, 248)
RS_CLICK = (905, 907)
CLOSE_CLICK = (14, 51)

# Constants for coordinate randomization
COORDINATE_OFFSET = 10

# Constants for time intervals
MIN_INTERVAL = 20  # 20 seconds
MAX_INTERVAL = 30  # 30 seconds

# Set the total runtime in seconds (3 hours)
total_runtime = 3 * 60 * 60

# Record the start time
start_time = time.time()

def perform_actions():
    # Sleep before clicking mine soft clay
    time.sleep(5)
    
    # Randomize click coordinates
    clay_click = (CLAY_CLICK[0] + random.randint(-COORDINATE_OFFSET, COORDINATE_OFFSET),
                  CLAY_CLICK[1] + random.randint(-COORDINATE_OFFSET, COORDINATE_OFFSET))
    pyautogui.click(clay_click)  # Click to mine clay

    # Add a random sleep time between MIN_INTERVAL and MAX_INTERVAL
    interval = random.randint(MIN_INTERVAL, MAX_INTERVAL)
    time.sleep(interval)

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
