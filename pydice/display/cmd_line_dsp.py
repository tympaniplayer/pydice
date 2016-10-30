die = """+-----+
| {} |
| {} |
| {} |
+-----+"""

die_map = { 1: die.format("   ", " * ", "   "),
            2: die.format("  *", "   ", "*  "),
            3: die.format("  *", " * ", "*  "),
            4: die.format("* *", "   ", "* *"),
            5: die.format("* *", " * ", "* *"),
            6: die.format("* *", "* *", "* *") }

def std_die(val):
    return die_map[val]

def print_std_dice_row(dice):
    dice_lines = [die.split("\n") for die in dice]

    for i in range(0, 5):
        for j in range(0, len(dice_lines)):
            print(str(dice_lines[j][i]) + "  ", end="")
        print("")
