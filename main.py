import mss
import mss.tools
import cv2
import numpy as np
import pytesseract as tes

def main():
    mainStat = {'top': 270, 'left': 1750, 'width': 250, 'height': 170}
    subStats = {'top': 560, 'left': 1750, 'width': 400, 'height': 205}

    sct = mss.mss()
    tes.pytesseract.tesseract_cmd = r'D:\Users\Dosx001\AppData\Local\Programs\Tesseract-OCR\tesseract.exe'
    for sect in [mainStat, subStats]:
        img = sct.grab(sect)
        #mss.tools.to_png(img.rgb, img.size, output='img.png')

        img = np.asarray(img)
        img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        img = cv2.GaussianBlur(img, (3, 3), 0)

        text = tes.image_to_string(img)
        print(text)

if __name__ == "__main__":
    main()
