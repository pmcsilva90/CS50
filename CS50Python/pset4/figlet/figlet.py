import sys
import random
from pyfiglet import Figlet

fonts = figlet.getFonts()

str = input("Input: ")

f = Figlet(font='slant')

print(f.renderText(str))
