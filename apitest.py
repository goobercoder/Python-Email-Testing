import requests
facts= []
fun = {
  {
  "username": "dauwg",
  "avatar_url": "https://i.imgur.com/4M34hi2.png",
  "content": "Text message. Up to 2000 characters.",
  "embeds": [
    {
      "title": "dauwg",
      "description": "fun dog facts",
      "color": 15258703,
      "fields": [
        {
          "name": "Text",
          "value": "More text"
        },
        {
          "name": "Even more text",
          "value": "Yup"
        },
        {
          "name": "Use `\"inline\": true` parameter, if you want to display fields in the same line.",
          "value": "okay..."
        },
        {
          "name": "Thanks!",
          "value": "You're welcome :wink:"
        }
    ],
    }
  ]
}
}
discordurl = 'https://discord.com/api/webhooks/1304159442903765103/ggYRi-CJco2HpCQaOGycMGFo55gbfeGP6WRICGE6ebjlAuDJe1s4EIMkpkDy7Fu_5jhz'
url = 'http://dog-api.kinduff.com/api/facts?number=5'
r = requests.get(url)
print(r)
#print(r.json())
f = r.json()
for fact in f["facts"]:
    facts.append(fact)
print(facts)