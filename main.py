from processText.img2text import Img2Text
from control.mouse import Mouse
import asyncio

def main():
    itt = Img2Text()
    mu = Mouse(1)
    for i in range(31):
        mu.click()
        print(asyncio.run(itt.getText()))
        mu.click()
        mu.move()

if __name__ == "__main__":
    main()
