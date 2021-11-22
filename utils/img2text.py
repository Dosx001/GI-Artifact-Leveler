import mss
import mss.tools
import cv2
import numpy as np
import pytesseract as tes
from fuzzywuzzy import process
import asyncio

class Img2Text:
    def __init__(self):
        self.setPiece = {'top': 280, 'left': 1750, 'width': 250, 'height': 160}
        self.mainStat = {'top': 350, 'left': 1750, 'width': 250, 'height': 40}
        self.subStats = {'top': 560, 'left': 1750, 'width': 400, 'height': 205}
        self.sct = mss.mss()
        tes.pytesseract.tesseract_cmd = r'D:\Users\Dosx001\AppData\Local\Programs\Tesseract-OCR\tesseract.exe'
        self.stats = ["CRIT Rate", "CRIT DMG", "Energy Recharge",
                "Elemental Mastery", "ATK", "HP", "DEF"]

    def saveImg(self, sect):
        img = self.sct.grab(sect)
        mss.tools.to_png(img.rgb, img.size, output="out.png")

    async def getText(self):
        output = {"set": "", "piece": "", "mainStat": [], "subStats" : {}}
        task1 = asyncio.create_task(self.processText(self.setPiece, 2))
        task2 = asyncio.create_task(self.processText(self.mainStat, 1))
        task3 = asyncio.create_task(self.processText(self.subStats, 5))
        txt = await task1
        output['piece'] = txt[0]
        stat = self.correction(txt[-1])
        txt = await task2
        output['mainStat'].append(txt[0])
        output['mainStat'].append(stat)
        txt = await task3
        for stat in txt:
            if len(stat) == 0:
                continue
            if " " in stat[0:3]:
                stat = stat[2::].split("+" if "+" in stat else "t")
                key = process.extractOne(" ".join(stat[:-1]), self.stats)[0]
                if "%" in stat[-1] and key in ["ATK", "HP", "DEF"]:
                    key += "%"
                output['subStats'][key] = stat[-1].strip('%')
            else:
                output['set'] = stat[:-1]
                break
        return output

    async def processText(self, sect, split):
        img = self.sct.grab(sect)
        img = np.asarray(img)
        img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        thr = cv2.threshold(img, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)[1]
        (h_thr, w_thr) = thr.shape[:2]
        s_idx = 0
        e_idx = int(h_thr / split)

        output = []
        for _ in range(0, split):
            crp = thr[s_idx:e_idx, 0:w_thr]
            (h_crp, w_crp) = crp.shape[:2]
            crp = cv2.resize(crp, (w_crp * 2, h_crp * 2))
            crp = cv2.erode(crp, None, iterations = 1)
            s_idx = e_idx
            e_idx = s_idx + int(h_thr / split)
            txt = tes.image_to_string(crp).split('\n')
            txt.pop()
            output += txt
            #print(txt)
            #cv2.imshow("crp", crp)
            #cv2.waitKey(0)
        return output

    def correction(self, stat):
        fix = {"rar": "717", "1.0%" : "7.0%"}
        try:
            return fix[stat]
        except KeyError:
            return stat
