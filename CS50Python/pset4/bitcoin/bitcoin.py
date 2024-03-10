import json
import requests
import sys

if len(sys.argv) == 2:
    try:
        n = int(sys.argv[1])
    except ValueError:
        sys.exit("Not a valid value")
else:
    sys.exit(f"Usage: {sys.argv[0]} number")

response = requests.get(https://api.coindesk.com/v1/bpi/currentprice.json)

print(n)
