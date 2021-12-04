from time import sleep
import pyautogui as ag

class Mouse:
    def __init__(self, col):
        self.col = col

    def move(self):
        if self.col == 11:
            self.col = 1
            ag.moveRel(-1420, 6)
            for i in range(9):
                ag.scroll(-1)
        else:
            self.col += 1
            ag.moveRel(142, 0)

    def click(self):
        ag.click(clicks=2)
        sleep(.1)

    def button(self, target):
        pos = ag.position()
        ag.moveTo(target)
        self.click()
        ag.moveTo(pos)

    def lock(self):
        self.button((2190, 525))

    def enchance(self):
        self.button((2300, 1035))
