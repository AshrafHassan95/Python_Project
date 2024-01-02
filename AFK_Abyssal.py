import pyautogui
import time
import random


# Aggression potion coordinate
target_x = 819
target_y = 740

# Define the interval in seconds (between 5.5 to 6.5 minutes)
min_interval = 330  # 5.5 minutes in seconds
max_interval = 390  # 6.5 minutes in seconds

while True:
    # Generate a random interval between min_interval and max_interval
    interval = random.randint(min_interval, max_interval)
    
    # Sleep for the calculated interval
    time.sleep(interval)
    
    # Move the mouse to the target position and click
    pyautogui.click(target_x, target_y)