import sys
import PIL

def main():

#  two command-line arguments
# in sys.argv[1], the name (or path) of a JPEG or PNG to read (i.e., open) as input
# in sys.argv[2], the name (or path) of a JPEG or PNG to write (i.e., save) as output

    if len(sys.argv) < 3:
        sys.exit("Too few arguments")
    elif len(sys.argv) > 3:
        sys.exit("Too many arguments")
    elif len(sys.argv) == 3:
        if is_image(sys.argv[1]) and is_image(sys.argv[2]):
            if splitext(sys.argv[1])[1] == splitext(sys.argv[2])[1]:
                try:
                    print("good so far")
                except FileNotFoundError:
                    sys.exit("File not found")
            else:
                sys.exit("Input and output have different extensions")
        else:
            sys.exit("Invalid input")

def is_image(filename):
    _, ext = splitext(filename)
    if ext.lower() == ".png" or ext.lower() == ".jpeg" or ext.lower() == ".jpg":
        return True
    return False


