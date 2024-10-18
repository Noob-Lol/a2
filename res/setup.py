import os, time, requests, os
import pyautogui as pag
from PIL import Image
webhook_url = os.environ["WEBHOOK"]
# Define actions with coordinates and duration
actions = [
    (516, 405, 4),  # install (wait 15sec)
    (50, 100, 1),   # tic launch avica
    (447, 286, 4),  # ss id & upload (launch avica and take screenshot and send to gofile)
]

# Give time to focus on the target application
time.sleep(10)
num = 0
pag.screenshot().save(f"img{num}.png")
num += 1
# Credentials and upload information
img_filename = 'NoobImage.png'
img2 = 'NoobImage2.png'
# Iterate through actions
for x, y, duration in actions:
    pag.click(x, y, duration=duration)
    pag.screenshot().save(f"img{num}.png")
    num += 1
    if (x, y) == (249, 203):  # Attempt to activate "Allow remote access"
        time.sleep(1)  # Delay to ensure the button click registers
        pag.click(x, y, duration=duration)  # Try activating the button again
    pag.screenshot().save(f"img{num}.png")
    num += 1
    if (x, y) == (447, 286):  # Launch avica and upload screenshot
        time.sleep(10)
        pag.screenshot().save(img_filename)
        Image.open(img_filename).crop((230, 120, 500, 160)).save(img2)
        try:
            requests.post(webhook_url, files={"file": open(img2, "rb")})
            print("Connection info was sent via webhook.")
        except Exception as e:
            print(f"An error occurred: {e}")
    time.sleep(10)
