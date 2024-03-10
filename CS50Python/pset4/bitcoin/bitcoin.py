import json
import requests
import sys

try:
    n = (float)sys.argv[1]
except ValueError:
    sys.exit("Not a valid value")

print(n)
