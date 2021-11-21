from utils.img2text import Img2Text
from utils.mouse import Mouse
from artifact.leveler import Leveler
from argparse import ArgumentParser
import asyncio

def main(args):
    mu = Mouse(args.column)
    itt = Img2Text()
    lvl = Leveler(args.total)
    while (lvl.total < 6):
        mu.click()
        if lvl.picker(asyncio.run(itt.getText())):
            mu.click()
        mu.move()

if __name__ == "__main__":
    parser = ArgumentParser()
    parser.add_argument('--column', type=int, default=0, help='An optional integer argument')
    parser.add_argument('--total', type=int, default=0, help='An optional integer argument')
    main(parser.parse_args())
