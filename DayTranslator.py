import pyautogui as pag
import numpy as np
from PIL import Image
import pytesseract
import time
import re
import cv2
from matplotlib import pyplot as plt

# Since I tested on a 3k Monitor, the default screen size for ratio calculations is 2560x1440
# TEST_SCREEN_WIDTH, TEST_SCREEN_HEIGHT = 2560, 1440
SCREEN_WIDTH, SCREEN_HEIGHT = pag.size()


def getBattleButton():
    """
    Battle Button Reference Values (On 2560x1440 Screen)

    Width = 287
    Height = 129

    BeginFromLeft = 2244
    BeginFromTop = 26

    Begin From Left / Screen Width RATIO = 2244 / 2560
    Begin From Top / Screen Height RATIO = 26 / 1440
    Button Width / Screen Width RATIO = 287 / 2560
    Button Height / Screen Height RATIO = 129 / 1440

    :return: Image of Battle Button
    """

    return pag.screenshot("BattleButton.PNG", region=(
        np.multiply(SCREEN_WIDTH, np.divide(2244, 2560)),
        np.multiply(SCREEN_HEIGHT, np.divide(26, 1440)),
        np.multiply(SCREEN_WIDTH, np.divide(287, 2560)),
        np.multiply(SCREEN_HEIGHT, np.divide(129, 1440))
    ))


def getCampaignButton():
    """
    Campaign Button Reference Values (On 2560x1440 Screen)

    Width = 932
    Height = 218

    BeginFromLeft = 814
    BeginFromTop = 301

    Begin From Left / Screen Width RATIO = 814 / 2560
    Begin From Top / Screen Height RATIO = 301 / 1440
    Button Width / Screen Width RATIO = 932 / 2560
    Button Height / Screen Height RATIO = 218 / 1440

    :return: Image of Campaign Button
    """

    return pag.screenshot("CampaignButton.PNG", region=(
        np.multiply(SCREEN_WIDTH, np.divide(814, 2560)),
        np.multiply(SCREEN_HEIGHT, np.divide(301, 1440)),
        np.multiply(SCREEN_WIDTH, np.divide(932, 2560)),
        np.multiply(SCREEN_HEIGHT, np.divide(218, 1440))
    ))


def getDoubleGoldButton():
    """
    Campaign Button Reference Values (On 2560x1440 Screen)

    Width = 359
    Height = 115

    BeginFromLeft = 1297
    BeginFromTop = 892

    Begin From Left / Screen Width RATIO = 1297 / 2560
    Begin From Top / Screen Height RATIO = 892 / 1440
    Button Width / Screen Width RATIO = 359 / 2560
    Button Height / Screen Height RATIO = 115 / 1440

    :return: Image of Campaign Button
    """

    return pag.screenshot("DoubleGoldButton.PNG", region=(
        np.multiply(SCREEN_WIDTH, np.divide(1297, 2560)),
        np.multiply(SCREEN_HEIGHT, np.divide(892, 1440)),
        np.multiply(SCREEN_WIDTH, np.divide(359, 2560)),
        np.multiply(SCREEN_HEIGHT, np.divide(115, 1440))
    ))


# i = 116
# while ( True ):
#     img = pag.screenshot("Resources\Day{}.PNG".format(i), region=(
#         975,
#         25,
#         410,
#         100
#     ))
#     i += 1
#     input("Press Enter to continue...")


txt = open("Day Values2.txt", 'w')
txt2 = open("Day Values.txt", 'w')
i = 38
while ( i <= 115):
    img = cv2.imread("Resources\Day{}.PNG".format(i))

    img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    _, img = cv2.threshold(img, 50, 255, cv2.THRESH_BINARY_INV)
    kernel = np.ones((3, 3), np.uint8)
    img = cv2.erode(img, kernel, iterations=1)
    img = cv2.blur(img, (5,5))
    # cv2.imwrite("E:\ProjectsPython\DaysBygoneBot\ResourcesUpdated\Day{}.PNG".format(i), img)
    var = pytesseract.image_to_string(img, lang='eng', config='--psm 13 --oem 3 -c tessedit_char_whitelist=0123456789')
    txt.write(var + "\n")

    var = re.sub("[^0-9]", "", var)
    txt2.write(var + "\n")

    i += 1

txt.close()



# txt = open("Day Values.txt", 'w')
#
# i = 0
# while (True):
#     pag.screenshot("Day.PNG", region=(
#         975,
#         25,
#         410,
#         100
#
#     ))
#
#     var = pytesseract.image_to_string(Image.open('Day.PNG'), config='--psm 13 --oem 3 -c tessedit_char_whitelist=0123456789')
#     var = re.sub("[^0-9]", "", var)
#
#     txt.write(var + "\n")
#
#     print("VAR:" + var)
#
#     try:
#         if (int(var) >= 2983):
#             break
#         elif (i >= 3000):
#             break
#     except(ValueError):
#         pass
#
#     i += 1
#     time.sleep(1)
#
# txt.close()

# if __name__ == '__main__':
#     getBattleButton()
