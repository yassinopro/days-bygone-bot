import numpy as np
from pyautogui import screenshot, size
from skimage import io, color, measure
from skimage.transform import resize


class ScreenReader:


    def __init__(self, max_day = 68, min_day = 38):
        self.__screen_width = size().width
        self.__screen_height = size().height

        # Since I tested on a 3k Monitor, the default screen size for ratio calculations is 2560x1440
        self.__ref_screen_width = 2560
        self.__ref_screen_height = 1440

        self.__max_day = max_day
        self.__min_day = min_day


    def getBattleButton(self):
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

        BeginFromLeft = 2244
        BeginFromTop = 26

        return screenshot("Resources\Images\BattleButton.PNG", region=(
            np.multiply(self.__screen_width, np.divide(2244, self.__ref_screen_width)),
            np.multiply(self.__screen_height, np.divide(26, self.__ref_screen_height)),
            np.multiply(self.__screen_width, np.divide(287, self.__ref_screen_width)),
            np.multiply(self.__screen_height, np.divide(129, self.__ref_screen_height))
        )), BeginFromLeft, BeginFromTop


    def getCampaignButton(self):
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

        BeginFromLeft = 814
        BeginFromTop = 301

        return screenshot("Resources\Images\CampaignButton.PNG", region=(
            np.multiply(self.__screen_width, np.divide(814, self.__ref_screen_width)),
            np.multiply(self.__screen_height, np.divide(301, self.__ref_screen_height)),
            np.multiply(self.__screen_width, np.divide(932, self.__ref_screen_width)),
            np.multiply(self.__screen_height, np.divide(218, self.__ref_screen_height))
        )), BeginFromLeft, BeginFromTop


    def getDoubleGoldButton(self):
        """
        Campaign Button Reference Values (On 2560x1440 Screen)

        Width = 359
        Height = 115

        BeginFromLeft = 1288
        BeginFromTop = 892

        Begin From Left / Screen Width RATIO = 1288 / 2560
        Begin From Top / Screen Height RATIO = 892 / 1440
        Button Width / Screen Width RATIO = 359 / 2560
        Button Height / Screen Height RATIO = 115 / 1440

        :return: Image of Campaign Button
        """

        BeginFromLeft = 1288
        BeginFromTop = 892

        return screenshot("Resources\Images\DoubleGoldButton.PNG", region=(
            np.multiply(self.__screen_width, np.divide(1288, self.__ref_screen_width)),
            np.multiply(self.__screen_height, np.divide(892, self.__ref_screen_height)),
            np.multiply(self.__screen_width, np.divide(359, self.__ref_screen_width)),
            np.multiply(self.__screen_height, np.divide(115, self.__ref_screen_height))
        )), BeginFromLeft, BeginFromTop


    def getPauseButton(self):
        """
        Pause Button Reference Values (On 2560x1440 Screen)

        Width = 74
        Height = 96

        BeginFromLeft = 59
        BeginFromTop = 40

        Begin From Left / Screen Width RATIO = 59 / 2560
        Begin From Top / Screen Height RATIO = 40 / 1440
        Button Width / Screen Width RATIO = 74 / 2560
        Button Height / Screen Height RATIO = 96 / 1440

        :return: Image of Campaign Button
        """

        BeginFromLeft = 59
        BeginFromTop = 40

        return screenshot("Resources\Images\PauseButton.PNG", region=(
            np.multiply(self.__screen_width, np.divide(59, self.__ref_screen_width)),
            np.multiply(self.__screen_height, np.divide(40, self.__ref_screen_height)),
            np.multiply(self.__screen_width, np.divide(74, self.__ref_screen_width)),
            np.multiply(self.__screen_height, np.divide(96, self.__ref_screen_height))
        )), BeginFromLeft, BeginFromTop


    def getReturnButton(self):
        """
        Return Button Reference Values (On 2560x1440 Screen)

        Width = 320
        Height = 111

        BeginFromLeft = 1120
        BeginFromTop = 925

        Begin From Left / Screen Width RATIO = 1120 / 2560
        Begin From Top / Screen Height RATIO = 925 / 1440
        Button Width / Screen Width RATIO = 320 / 2560
        Button Height / Screen Height RATIO = 111 / 1440

        :return: Image of Return Button
        """

        BeginFromLeft = 1120
        BeginFromTop = 925

        return screenshot("Resources\Images\ReturnButton.PNG", region=(
            np.multiply(self.__screen_width, np.divide(1120, self.__ref_screen_width)),
            np.multiply(self.__screen_height, np.divide(925, self.__ref_screen_height)),
            np.multiply(self.__screen_width, np.divide(320, self.__ref_screen_width)),
            np.multiply(self.__screen_height, np.divide(111, self.__ref_screen_height))
        )), BeginFromLeft, BeginFromTop


    def getOkButton(self):
        """
        Ok Button Reference Values (On 2560x1440 Screen)

        Width = 360
        Height = 115

        BeginFromLeft = 1100
        BeginFromTop = 893

        Begin From Left / Screen Width RATIO = 1100 / 2560
        Begin From Top / Screen Height RATIO = 893 / 1440
        Button Width / Screen Width RATIO = 360 / 2560
        Button Height / Screen Height RATIO = 115 / 1440

        :return: Image of Ok Button
        """

        BeginFromLeft = 1100
        BeginFromTop = 893

        return screenshot("Resources\Images\OkButton.PNG", region=(
            np.multiply(self.__screen_width, np.divide(1100, self.__ref_screen_width)),
            np.multiply(self.__screen_height, np.divide(893, self.__ref_screen_height)),
            np.multiply(self.__screen_width, np.divide(360, self.__ref_screen_width)),
            np.multiply(self.__screen_height, np.divide(115, self.__ref_screen_height))
        )), BeginFromLeft, BeginFromTop


    def getRewindButton(self):
        """
        Rewind Button Reference Values (On 2560x1440 Screen)

        Width = 342
        Height = 114

        BeginFromLeft = 623
        BeginFromTop = 489

        Begin From Left / Screen Width RATIO = 623 / 2560
        Begin From Top / Screen Height RATIO = 489 / 1440
        Button Width / Screen Width RATIO = 342 / 2560
        Button Height / Screen Height RATIO = 114 / 1440

        :return: Image of Rewind Button
        """

        BeginFromLeft = 623
        BeginFromTop = 489

        return screenshot("Resources\Images\RewindButton.PNG", region=(
            np.multiply(self.__screen_width, np.divide(623, self.__ref_screen_width)),
            np.multiply(self.__screen_height, np.divide(489, self.__ref_screen_height)),
            np.multiply(self.__screen_width, np.divide(342, self.__ref_screen_width)),
            np.multiply(self.__screen_height, np.divide(115, self.__ref_screen_height))
        )), BeginFromLeft, BeginFromTop


    def getConfirmRewindButton(self):
        """
        Confirm Rewind Button Reference Values (On 2560x1440 Screen)

        Width = 341
        Height = 109

        BeginFromLeft = 1480
        BeginFromTop = 1157

        Begin From Left / Screen Width RATIO = 1480 / 2560
        Begin From Top / Screen Height RATIO = 1157 / 1440
        Button Width / Screen Width RATIO = 341 / 2560
        Button Height / Screen Height RATIO = 109 / 1440

        :return: Image of Confirm Rewind Button
        """

        BeginFromLeft = 1480
        BeginFromTop = 1157

        return screenshot("Resources\Images\ConfirmRewindButton.PNG", region=(
            np.multiply(self.__screen_width, np.divide(1480, self.__ref_screen_width)),
            np.multiply(self.__screen_height, np.divide(1157, self.__ref_screen_height)),
            np.multiply(self.__screen_width, np.divide(341, self.__ref_screen_width)),
            np.multiply(self.__screen_height, np.divide(109, self.__ref_screen_height))
        )), BeginFromLeft, BeginFromTop


    def getRewindButtonLock(self):
        """
        Rewind Button Lock Reference Values (On 2560x1440 Screen)

        Width = 44
        Height = 49

        BeginFromLeft = 651
        BeginFromTop = 522

        Begin From Left / Screen Width RATIO = 651 / 2560
        Begin From Top / Screen Height RATIO = 522 / 1440
        Button Width / Screen Width RATIO = 44 / 2560
        Button Height / Screen Height RATIO = 49 / 1440

        :return: Image of Rewind Button Lock Button
        """

        BeginFromLeft = 651
        BeginFromTop = 522

        return screenshot("Resources\Images\RewindButtonLock.PNG", region=(
            np.multiply(self.__screen_width, np.divide(651, self.__ref_screen_width)),
            np.multiply(self.__screen_height, np.divide(522, self.__ref_screen_height)),
            np.multiply(self.__screen_width, np.divide(44, self.__ref_screen_width)),
            np.multiply(self.__screen_height, np.divide(49, self.__ref_screen_height))
        )), BeginFromLeft, BeginFromTop


    def getSectionTitleSkills(self):
        """
        Section Title Skills Reference Values (On 2560x1440 Screen)

        Width = 406
        Height = 118

        BeginFromLeft = 22
        BeginFromTop = 31

        Begin From Left / Screen Width RATIO = 22 / 2560
        Begin From Top / Screen Height RATIO = 31 / 1440
        Button Width / Screen Width RATIO = 406 / 2560
        Button Height / Screen Height RATIO = 118 / 1440

        :return: Image of Section Skills Title
        """

        BeginFromLeft = 22
        BeginFromTop = 31

        return screenshot("Resources\Images\SectionTitleSkills.PNG", region=(
            np.multiply(self.__screen_width, np.divide(22, self.__ref_screen_width)),
            np.multiply(self.__screen_height, np.divide(31, self.__ref_screen_height)),
            np.multiply(self.__screen_width, np.divide(406, self.__ref_screen_width)),
            np.multiply(self.__screen_height, np.divide(118, self.__ref_screen_height))
        )), BeginFromLeft, BeginFromTop


    def getTabSkills(self):
        """
        Confirm Rewind Button Reference Values (On 2560x1440 Screen)

        Width = 91
        Height = 98

        BeginFromLeft = 52
        BeginFromTop = 1265

        Begin From Left / Screen Width RATIO = 52 / 2560
        Begin From Top / Screen Height RATIO = 1265 / 1440
        Button Width / Screen Width RATIO = 91 / 2560
        Button Height / Screen Height RATIO = 98 / 1440

        :return: Image of Confirm Rewind Button
        """

        BeginFromLeft = 52
        BeginFromTop = 1265

        return screenshot("Resources\Images\SkillsTab.PNG", region=(
            np.multiply(self.__screen_width, np.divide(52, self.__ref_screen_width)),
            np.multiply(self.__screen_height, np.divide(1265, self.__ref_screen_height)),
            np.multiply(self.__screen_width, np.divide(91, self.__ref_screen_width)),
            np.multiply(self.__screen_height, np.divide(98, self.__ref_screen_height))
        )), BeginFromLeft, BeginFromTop


    def getDay(self):
        """
        Day Area Reference Values (On 2560x1440 Screen)

        Width = 410
        Height = 100

        BeginFromLeft = 975
        BeginFromTop = 25

        Begin From Left / Screen Width RATIO = 975 / 2560
        Begin From Top / Screen Height RATIO = 25 / 1440
        Button Width / Screen Width RATIO = 410 / 2560
        Button Height / Screen Height RATIO = 100 / 1440

        :return: Image of Day Area
        """

        return screenshot("Resources\Images\Day.PNG", region=(
            np.multiply(self.__screen_width, np.divide(975, self.__ref_screen_width)),
            np.multiply(self.__screen_height, np.divide(25, self.__ref_screen_height)),
            np.multiply(self.__screen_width, np.divide(410, self.__ref_screen_width)),
            np.multiply(self.__screen_height, np.divide(100, self.__ref_screen_height))
        ))


    def compareImages(self, filename1, filename2):
        ref_image = io.imread(filename1)
        ref_image = color.rgb2gray(ref_image)
        ref_image = resize(ref_image, (123, 274), anti_aliasing=True)

        image = io.imread(filename2)
        image = color.rgb2gray(image)
        image = resize(image, (123, 274), anti_aliasing=True)

        if (measure.compare_mse(ref_image, image) < 0.05):
            print("True: {}".format(measure.compare_mse(ref_image, image)))
            return True
        else:
            print("False")
            print("File1: {}; File2: {}".format(filename1, filename2))
            return False

    # Getter/Setter
    def get_min_day(self):
        return self.__min_day
    def set_min_day(self, arg__min_day):
        self.__min_day = arg__min_day
    def del_min_day(self):
        del self.__min_day
    min_day = property(get_min_day, set_min_day, del_min_day)


    def get_max_day(self):
        return self.__max_day
    def set_max_day(self, arg__max_day):
        self.__max_day = arg__max_day
    def del_max_day(self):
        del self.__max_day
    max_day = property(get_max_day, set_max_day, del_max_day)