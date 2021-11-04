import mss
import mss.tools
import cv2
import numpy as np
import pytesseract as tes

class Img2Text:
    def __init__(self):
        self.output = []
        self.mainStat = {'top': 270, 'left': 1750, 'width': 250, 'height': 170}
        self.subStats = {'top': 560, 'left': 1750, 'width': 400, 'height': 205}
        self.sct = mss.mss()
        tes.pytesseract.tesseract_cmd = r'D:\Users\Dosx001\AppData\Local\Programs\Tesseract-OCR\tesseract.exe'

    def getText(self):
        self.processText(self.mainStat)
        self.processText(self.subStats)

    def processText(self, sect):
        img = self.sct.grab(sect)
        img = np.asarray(img)
        img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        img = cv2.GaussianBlur(img, (3, 3), 0)
        text = tes.image_to_string(img).split('\n')
        print(text)
