import pyautogui
from pyautogui import moveTo
from time import sleep
from pyautogui import pixel

sleep(3)
pix = ()
for i in range(39274961648646161616123):
    sleep(1)
    moveTo(1800, 440)
    pyautogui.click(button='left')
    for i in range(10):
        pyautogui.press('tab')
    pyautogui.press('enter')
    sleep(6)
    try:
        pix = pyautogui.pixel(1300, 540)
        print(pix)
    except:
        pass
    if pix[0] == 0 and pix[1] == 0 and pix[2] == 0:
        moveTo(1420, 190)
        pyautogui.click(button='left')
        pyautogui.press('f5')
        sleep(1)
    else:
        sleep(0.5)
        pyautogui.press('tab')
        pyautogui.press('enter')
        sleep(1.6)
        pyautogui.press('esc')
        sleep(1.1)
        pyautogui.press('tab')
        pyautogui.press('tab')
        pyautogui.press('enter')
        sleep(1)
        moveTo(1420,190)
        pyautogui.click(button='left')
        sleep(1)
        pyautogui.click(button='left')
        for i in range(10):
            pyautogui.press('tab')
        pyautogui.press('enter')
        sleep(3.3)
        pyautogui.press('f5')
        sleep(1)