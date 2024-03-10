import sys
import random
from pyfiglet import Figlet

figlet = Figlet()

fonts = figlet.getFonts()
figlet.setFont(font=f)


str = input("Input: ")

print(figlet.renderText(str))
