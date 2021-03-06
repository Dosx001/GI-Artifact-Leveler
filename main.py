from utils.img2text import Img2Text
from utils.mouse import Mouse
from artifact.enhancer import Enhancer
from argparse import ArgumentParser
import asyncio

def main(args):
    mu = Mouse(args.column)
    itt = Img2Text()
    eh = Enhancer(args.total)
    while (eh.total < 6):
        mu.click()
        score = eh.score(asyncio.run(itt.getText()))
        if score == 0:
            mu.lock()
        elif score == 1:
            mu.click()
        mu.move()

if __name__ == "__main__":
    parser = ArgumentParser()
    parser.add_argument('--column', '-c',  type=int, default=1, help='Integer: 1 to 11')
    parser.add_argument('--total', '-t', type=int, default=0, help='Integer: 0 to 6')
    main(parser.parse_args())
