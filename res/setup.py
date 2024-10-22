import os, requests, subprocess, re, pyperclip
import pyautogui as pag
webhook_url = os.environ["WEBHOOK"]
pag.sleep(1)
img_filename = 'Image.png'
pag.click(516, 405, duration=2)
pag.sleep(1)
while not pag.locateOnScreen('res/A-ready.png', confidence=0.9):
    pag.sleep(1)
pag.click(249, 203, duration=2)
pag.sleep(.5)
pag.click(301, 105, duration=2)
pag.sleep(.5)

text = pyperclip.paste()
#match = re.search(r"Avica ID:\s*(\d{3} \d{3} \d{3}).*?Password:\s*([A-Za-z0-9]+)", text, re.DOTALL)
match = False
try:
    if match:
        requests.post(webhook_url, json={"content": f"ID: {match.group(1)}\nPass: {match.group(2)}"})
    else:
        print("Details not found, sending screenshot.")
        pag.sleep(1)
        pag.screenshot.save(img_filename)
        requests.post(webhook_url, files={"file": open(img_filename, "rb")})
    print("Connection info was sent via webhook.")
except Exception as e:
    print(f"An error occurred: {e}")
subprocess.Popen(r'start "" /MAX "C:\Users\Public\Desktop\VMQuickConfig"', shell=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
pag.click(143, 487, duration=5)
pag.click(155, 554, duration=2)
pag.click(637, 417, duration=2)
pag.click(588, 10, duration=2)
pag.sleep(1)
