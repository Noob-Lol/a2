import os, time, requests
import pyautogui as pag
from PIL import Image
webhook_url = os.environ["WEBHOOK"]
time.sleep(10)
num = 0
pag.screenshot().save(f"img{num}.png")
num += 1
img_filename = 'Image.png'
pag.click(516, 405, duration=4)
pag.screenshot().save(f"img{num}.png")
num += 1
time.sleep(15)
pag.click(249, 203, duration=4)
time.sleep(1)
pag.screenshot().save(img_filename)
#Image.open(img_filename).crop((230, 120, 500, 160)).save(img_filename)
try:
    requests.post(webhook_url, files={"file": open(img_filename, "rb")})
    print("Connection info was sent via webhook.")
except Exception as e:
    print(f"An error occurred: {e}")
