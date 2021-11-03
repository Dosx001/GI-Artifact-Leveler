import mss
import mss.tools
import numpy
import pytesseract

def main():
    artSet = {'top': 210, 'left': 1770, 'width': 450, 'height': 45}
    mainStat = {'top': 270, 'left': 1750, 'width': 250, 'height': 170}
    subStats = {'top': 550, 'left': 1750, 'width': 400, 'height': 175}

    sct = mss.mss()
    img = sct.grab(mainStat)
    mss.tools.to_png(img.rgb, img.size, output='img.png')

    pytesseract.pytesseract.tesseract_cmd = r'D:\Users\Dosx001\AppData\Local\Programs\Tesseract-OCR\tesseract.exe'
    text = pytesseract.image_to_string(numpy.asarray(img))
    print(text)
    print(text.split('\n'))

if __name__ == "__main__":
    main()
