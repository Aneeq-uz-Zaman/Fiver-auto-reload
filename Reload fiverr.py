import pyautogui
import random
import time

# Function to simulate pressing Ctrl+R
def press_ctrl_r():
    pyautogui.hotkey('ctrl', 'r')
def click_image(image):
  # Find the image on the screen
  location = pyautogui.locateOnScreen(image,confidence=0.9)
  # If the image is found, click on the center of it
  if location:
    return True
  else:
    return False
# Main program
while True:
    # Generate a random interval between 160 and 1000 seconds
    interval = random.randint(160,1000)
    time.sleep(interval)
    status=click_image("Fv.PNG")
    if status:
        # Simulate pressing Ctrl+R
        press_ctrl_r()
    else:
       time.sleep(5)
