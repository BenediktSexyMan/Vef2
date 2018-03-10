import json, requests
url = 'https://api.foursquare.com/v2/venues/explore'

params = dict(
  client_id='2A4DOUFQZGSPS5T1RAKAOTTYODQ1UQCGPPW4Z25C12WYYF4B',
  client_secret='XO0J05FI1M3JQYSN12G20WO5NTTSLMFAPQEZOXJODZYUTWXE',
  v='20170801',
  ll='64.128288, -21.827774',
  query='pizza',
  limit=10000000
)
resp = requests.get(url=url, params=params)
data = json.loads(resp.text)
for x in data["response"]["groups"][0]["items"]:
    print(x["venue"]["name"], end=" ")
    try: print(x["venue"]["location"]["address"], end="")
    except KeyError: pass
    print()