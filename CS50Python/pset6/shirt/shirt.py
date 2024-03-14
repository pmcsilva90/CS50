import sys
from PIL import Image, ImageOps
from os.path import splitext


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
            if splitext(sys.argv[1])[1].lower() == splitext(sys.argv[2])[1].lower():
                try:
                    with open(sys.argv[1], "rb"):
                        dress(sys.argv[1], sys.argv[2])
                except FileNotFoundError:
                    sys.exit("Input does not exist")
            else:
                sys.exit("Input and output have different extensions")
        else:
            sys.exit("Invalid input/output")


def dress(i_input, i_output):

    shirt = Image.open("shirt.png")
    size = shirt.size

    image = Image.open(i_input)
    image = ImageOps.fit(image, size)

    image.paste(shirt, shirt)

    image.save(i_output)


def is_image(filename):
    _, ext = splitext(filename)
    if ext.lower() == ".png" or ext.lower() == ".jpeg" or ext.lower() == ".jpg":
        return True
    return False


if __name__ == "__main__":
    main()
