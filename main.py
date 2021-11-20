from processText.img2text import Img2Text
from control.mouse import Mouse
from argparse import ArgumentParser
import asyncio

def main(args):
    mu = Mouse(args.column, args.total)
    itt = Img2Text()
    for i in range(1000):
        mu.click()
        print(asyncio.run(itt.getText()))
        mu.click()
        mu.move()

if __name__ == "__main__":
    parser = ArgumentParser()
    parser.add_argument('--column', type=int, default=0, help='An optional integer argument')
    parser.add_argument('--total', type=int, default=0, help='An optional integer argument')
    main(parser.parse_args())
