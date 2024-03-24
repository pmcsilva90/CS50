import sys
import random
from pyfiglet import Figlet

figlet = Figlet()
fonts = figlet.getFonts()


if len(sys.argv) == 0:
    f = Figlet(font=random.choice(fonts))
    figlet.setFont(font=f)
elif len(sys.argv) == 2:
    f = sys.argv[2]
    if sys.argv[1] == "-f" or sys.argv[1] == "--font":
        try:
            figlet.setFont(font=f)
        except ValueError:
            sys.exit("Invalid font")
else:
    sys.exit("Invalid usage")

str = input("Input: ")

f = Figlet(font='slant')

print(f.renderText(str))
