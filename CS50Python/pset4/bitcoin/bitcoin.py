import json
import requests
import sys

n = 0

if len(sys.argv) == 2:
    try:
        n = int(sys.argv[1])
    except ValueError:
        sys.exit("Not a valid value")
else:
    sys.exit(f"Usage: {sys.argv[0]} number")

response = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")

data = response.json()
rate = data["bpi"]["USD"]["rate_float"]


print(f"{rate:,.4f}")
