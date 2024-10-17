import sys, os, time, requests, pytesseract, os
import pyautogui as pag
from PIL import Image
pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"
webhook_url = os.environ["WEBHOOK"]
# Define actions with coordinates and duration
actions = [
    (516, 405, 4),  # install (wait 15sec)
    (50, 100, 1),   # tic launch avica
    (249, 203, 4),  # allow rdp (attempt to activate the Allow button)
    (249, 203, 4),  # allow rdp (attempt to activate the Allow button again)
    (249, 203, 4),  # allow rdp (attempt to activate the Allow button again)
    (249, 203, 4),  # allow rdp (attempt to activate the Allow button again)
    (447, 286, 4),  # ss id & upload (launch avica and take screenshot and send to gofile)
]

# Give time to focus on the target application
time.sleep(10)

# Credentials and upload information
img_filename = 'NoobImage.png'

# Iterate through actions
for x, y, duration in actions:
    pag.click(x, y, duration=duration)
    if (x, y) == (249, 203):  # Attempt to activate "Allow remote access"
        time.sleep(1)  # Delay to ensure the button click registers
        pag.click(x, y, duration=duration)  # Try activating the button again
    
    if (x, y) == (447, 286):  # Launch avica and upload screenshot
        os.system("C:/Program Files x86/Avica/Avica.exe")
        time.sleep(5)  # Give some time for the app to launch
        pag.click(249, 203, duration=4)  # Re-click on the Allow button coordinates
        time.sleep(10)  # Extra 10 seconds delay before taking the screenshot
        pag.screenshot().save(img_filename)
        Image.open(img_filename).crop((230, 120, 500, 160)).save(img_filename)
        text = pytesseract.image_to_string(img_filename)
        part1, part2 = text.rsplit(' ', 1)
        try:
            requests.post(webhook_url, json={"content": f"ID: {part1}\nPass: {part2}"})
            print("Connection info was sent via webhook.")
        except Exception as e:
            print(f"An error occurred: {e}")
    time.sleep(10)
