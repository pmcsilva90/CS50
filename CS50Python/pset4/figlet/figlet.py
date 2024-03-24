import sys
import random
from pyfiglet import Figlet

figlet = Figlet()
fonts = figlet.getFonts()


if len(sys.argv) == 1:
    f = random.choice(fonts)
    print(f)
    figlet.setFont(font=f)
elif len(sys.argv) == 3:
    f = sys.argv[2]
    if sys.argv[1] == "-f" or sys.argv[1] == "--font":
        if f in fonts:
            figlet.setFont(font=f)
        else:
            sys.exit("Invalid font")
    else:
        sys.exit("Invalid usage")
else:
    sys.exit("Invalid usage")

str = input("Input: ")

print("Output:")
print(figlet.renderText(str))
