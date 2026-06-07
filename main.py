import os
import pyautogui
import pyscreeze

app_path = 'C:\\Users\SystemX\AppData\Roaming\Zoom\\bin\Zoom.exe'

def open_zoom():
    os.startfile(app_path)

join_conferenceImage = 'D:\zoomEdji\images\join.png'
join_conference = pyautogui.locateOnScreen(join_conferenceImage)
print(join_conference)

def join_meeting():
    print("[ВНИМАНИЕ] Уведомить службы внука если Zoom ID или Пароль были изменены")
    if join_conference == True:
        join_conference

open_zoom()
join_meeting()