import sys
import PIL

def main():

#  two command-line arguments
# in sys.argv[1], the name (or path) of a JPEG or PNG to read (i.e., open) as input
# in sys.argv[2], the name (or path) of a JPEG or PNG to write (i.e., save) as output

if len(sys.argv) < 3:
    sys.exit("Too few arguments")
if len(sys.argv) > 3:
    sys.exit("Too many arguments")
if len(sys.argv) == 3:
    if is_image(sys.argv[1]) and is_image(sys.argv[2]):
        if sys.argv[1][]
        try:
            ...
        except FileNotFoundError:
            sys.exit("")

def is_image(filename):
    root, ext = splitext(filename)
    if ext.lower() == ".png" or ext.lower() == ".jpeg" or ext.lower() == ".jpg"
        return True
    return False


