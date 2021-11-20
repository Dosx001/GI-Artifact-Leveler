from time import sleep
import pyautogui as ag

class Mouse:
    def __init__(self, col, total):
        self.col = col
        self.total = total

    def move(self):
        if self.col == 10:
            self.col = 0
            ag.moveRel(-1420, 6)
            for i in range(9):
                ag.scroll(-1)
        else:
            self.col += 1
            ag.moveRel(142, 0)

    def click(self):
        ag.click(clicks=2)
        sleep(.1)
