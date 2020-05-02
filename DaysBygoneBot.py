import cv2
import numpy as np
import pytesseract
import re
import pyautogui as pag
import time
import keyboard
from src.ScreenReader import ScreenReader


def alterImage(img):
    img = cv2.imread("Resources\Images\Day.PNG")
    img = cv2.cvtColor(img, cv2.COLOR_BGRA2BGR)
    img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    _, img = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY_INV)
    kernel = np.ones((5, 5), np.uint8)

    img = cv2.erode(img, kernel, iterations=1)
    img = cv2.blur(img, (5, 5))

    cv2.imwrite("Resources\Images\DayAltered.PNG", img)

    return img


def campaignMode(reader, time_to_sleep = 5):
    is_running = True
    while (is_running):

        img = reader.getDay()
        img = alterImage(img)

        var = pytesseract.image_to_string(img, lang='eng', config='--psm 13 --oem 3 -c tessedit_char_whitelist=0123456789')
        var = re.sub("[^0-9]", "", var)

        print("VAR: {}".format(var))

        try:
            var = int(var)
            if (var >= reader.max_day):
                is_running = False
            if (var <= reader.max_day) and (var >= reader.max_day - 10):
                time_to_sleep = 1
        except ValueError:
            pass

        time.sleep(time_to_sleep)


def clickButton(file_name, getImageFunc):
    is_running = True
    t0 = time.clock()
    while (is_running):
        t1 = t0 - time.clock()
        print("t1: {}".format(t1))
        if t1 < -15:
            break
        if (keyboard.is_pressed('y')):
            break
        image_battlebutton, from_left_battlebutton, from_top_battlebutton = getImageFunc()
        if reader.compareImages("Resources\RefImages\{}".format(file_name), "Resources\Images\{}".format(file_name)):
           pag.moveTo(
               ( from_left_battlebutton + image_battlebutton.width/2 ),
               ( from_top_battlebutton + image_battlebutton.height/2 )
           )
           pag.click()
           is_running = False
        else:
            pass


if __name__ == '__main__':
    reader = ScreenReader()

    running = True
    while running:
        if (keyboard.is_pressed('y')):
            break

        clickButton("BattleButton.PNG", reader.getBattleButton)

        clickButton("CampaignButton.PNG", reader.getCampaignButton)

        clickButton("DoubleGoldButton.PNG", reader.getDoubleGoldButton)

        campaignMode(reader)

        clickButton("PauseButton.PNG", reader.getPauseButton)

        clickButton("ReturnButton.PNG", reader.getReturnButton)

        clickButton("OkButton.PNG", reader.getOkButton)

        clickButton("SkillsTab.PNG", reader.getTabSkills)

        is_running = True
        while is_running:
            reader.getRewindButtonLock()
            if (keyboard.is_pressed('y')):
                break
            if ( reader.compareImages("Resources\RefImages\RewindButtonLock.PNG", "Resources\Images\RewindButtonLock.PNG") ):
                is_running = False
            else:
                clickButton("RewindButton.PNG", reader.getRewindButton)
                clickButton("ConfirmRewindButton.PNG", reader.getConfirmRewindButton)
