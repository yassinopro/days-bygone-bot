import pyautogui as pag
import numpy as np

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



# if __name__ == '__main__':
#     getBattleButton()


