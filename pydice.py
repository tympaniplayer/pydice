import sys
from pydice.display.cmd_line_dsp import *
from pydice.dice.std import *
from pydice.util import *

dice_count = 1

if len(sys.argv) > 1 and int(sys.argv[1]) > 0:
    dice_count = int(sys.argv[1])

dice = [std_die(rnd_std_die()) for i in range(dice_count)]
for row in list(group(dice, 4)):
    print_std_dice_row(row)
