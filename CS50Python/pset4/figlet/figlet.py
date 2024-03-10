import sys
import random
from pyfiglet import Figlet

fonts[] = figlet.getFonts()

if len(sys.argv) == 0:
    # random font
    if sys.argv[2] in fonts:
        f = Figlet(font=random.choice(fonts))

elif len(sys.argv) == 2:
    # argv[1] is "-f" or "--font", argv[2] is fontName
else:
    sys.exit("Invalid usage")




str = input("Input: ")

f = Figlet(font='slant')

print(f.renderText(str))
