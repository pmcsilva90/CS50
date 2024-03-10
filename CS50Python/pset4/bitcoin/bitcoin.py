import json
import requests
import sys

n = 0

if len(sys.argv) == 2:
    try:
        n = float(sys.argv[1])
    except ValueError:
        sys.exit("Command-line argument is not a number")
elif len(sys.argv) == 1:
    sys.exit("Missing command-line argument")
elif len(sys.argv) > 2:
    sys.exit("Too many arguments")

response = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")
data = response.json()
rate = data["bpi"]["USD"]["rate_float"]

print(f"${n * rate:,.4f}")
