import sys
import PIL

#  two command-line arguments
# in sys.argv[1], the name (or path) of a JPEG or PNG to read (i.e., open) as input
# in sys.argv[2], the name (or path) of a JPEG or PNG to write (i.e., save) as output

if len(sys.argv) < 3:
    sys.exit("Too few arguments")
if len(sys.argv) > 3:
    sys.exit("Too many arguments")
if len(sys.argv) == 3:
    if 
