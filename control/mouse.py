import pyautogui as ag

class Mouse:
    def __init__(self, post = 0, items = 0):
        self.post = post
        self.items = items

    def move(self):
        if self.post == 10:
            self.post = 0
            ag.moveRel(-1420, 10)
        else:
            self.post += 1
            ag.moveRel(142, 0)
        for i in range(9):
            ag.scroll(-1)
        ag.moveRel(0, 5)

    def click(self):
        ag.click(clicks=2)
