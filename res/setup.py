import os, time, requests, subprocess
import pyautogui as pag
from PIL import Image
webhook_url = os.environ["WEBHOOK"]
subprocess.Popen(r'start "" /MAX "C:\Users\Public\Desktop\VMQuickConfig"', shell=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
pag.click(143, 487, duration=5)
pag.click(155, 554, duration=2)
pag.click(637, 417, duration=2)
pag.click(588, 10, duration=2)
time.sleep(2)
img_filename = 'Image.png'
pag.click(516, 405, duration=4)
time.sleep(40)
pag.click(249, 203, duration=4)
time.sleep(1)
pag.screenshot().save(img_filename)
#Image.open(img_filename).crop((230, 120, 500, 160)).save(img_filename)
try:
    requests.post(webhook_url, files={"file": open(img_filename, "rb")})
    print("Connection info was sent via webhook.")
except Exception as e:
    print(f"An error occurred: {e}")
