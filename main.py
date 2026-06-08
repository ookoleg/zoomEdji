import os
import pyautogui
import time

app_path = 'C:\\Users\SystemX\AppData\Roaming\Zoom\\bin\Zoom.exe'

def open_zoom():
    os.startfile(app_path)

join_conferenceImage = 'D:\zoomEdji\images\join.png'

def join_meeting():
    join_conference = pyautogui.locateOnScreen(join_conferenceImage)
    print(join_conference)
    pyautogui.click(join_conference)


open_zoom()
time.sleep(3)
join_meeting()