from PIL import ImageGrab, Image
import pytesseract

def main():
    file = "fullscreen.png"
    artSet = (1770, 210, 2220, 255)
    mainStat = (1750, 270, 2000, 440)
    subStats = (1750, 550, 2150, 725)
    im = ImageGrab.grab(bbox = artSet)
    im.save(file)
    pytesseract.pytesseract.tesseract_cmd = r'D:\Users\Dosx001\AppData\Local\Programs\Tesseract-OCR\tesseract.exe'
    text = pytesseract.image_to_string(Image.open(file))
    print(text)
    print(text.split('\n'))

if __name__ == "__main__":
    main()
