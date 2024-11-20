import requests

facts = []
fun = {
  "username": "dauwg",
  "avatar_url": "https://static.toiimg.com/photo/114390036/114390036.jpg",
  "embeds": [
    {
      "title": "dauwg",
      "description": "fun dog facts",
      "color": 15258703,
      "fields": []
    }
  ]
}

discordurl = 'https://discord.com/api/webhooks/1304159442903765103/ggYRi-CJco2HpCQaOGycMGFo55gbfeGP6WRICGE6ebjlAuDJe1s4EIMkpkDy7Fu_5jhz'
url = 'http://dog-api.kinduff.com/api/facts?number=5'
r = requests.get(url)
print(r)
#print(r.json())
f = r.json()
c = 0
for fact in f["facts"]:
    c += 1
    facts.append(fact)
    z = { 
        "name": f"dogfact #{c}",
        "value": fact
    }
    fun["embeds"][0]["fields"].append(z)

print(fun)

# Send the payload to Discord webhook
response = requests.post(discordurl, json=fun)
print(response.status_code)
print(response.text)
