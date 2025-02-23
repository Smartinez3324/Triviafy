import requests

r = requests.get("https://itunes.apple.com/lookup?id=909253")

print(r.status_code)

