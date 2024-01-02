import pyautogui
import time
import random

# Constants for click coordinates
FORGE_CLICK = (740, 226)
ANVIL_CLICK = (520, 438)
RS_CLICK = (935, 907)

# Constants for coordinate randomization
COORDINATE_OFFSET = 3

def perform_actions():
    # Sleep before clicking forge
    time.sleep(5)
    forge_click = (FORGE_CLICK[0] + random.randint(-COORDINATE_OFFSET, COORDINATE_OFFSET),
                   FORGE_CLICK[1] + random.randint(-COORDINATE_OFFSET, COORDINATE_OFFSET))
    pyautogui.click(forge_click)  # click forge

    # Sleep before clicking anvil
    time.sleep(5)
    anvil_click = (ANVIL_CLICK[0] + random.randint(-COORDINATE_OFFSET, COORDINATE_OFFSET),
                   ANVIL_CLICK[1] + random.randint(-COORDINATE_OFFSET, COORDINATE_OFFSET))
    pyautogui.click(anvil_click)  # click anvil

    # Add a random sleep time between min_interval and max_interval
    interval = random.randint(min_interval, max_interval)
    time.sleep(interval)

if __name__ == "__main__":
    # Constants for time intervals
    min_interval = 30  # 30 seconds
    max_interval = 40  # 40 seconds

    # Sleep before opening RS
    time.sleep(3)
    pyautogui.click(RS_CLICK)  # click to open RS

    # Perform actions in a loop
    while True:
        perform_actions()
