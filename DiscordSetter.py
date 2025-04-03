import requests

f = open("Info.txt", "r")
text = f.read().splitlines()

url = "https://discord.com/api/v10/users/@me/settings"

if text[1][0] == "n":
  message = text[1][1:]
elif text[1][0] == "f":
  message = "error 404, status generator is being fixed now"

if text[2][0] == "n":
  emoji_id = text[2][1:]
elif text[2][0] == "f":
  emoji_id = "0"

def change_status(message, emoji_id):
  header = {
    "authorization": text[0]
  }

  jsonData = {
    "status": "online",
    "custom_status": {
      "text": message,
      "emoji_id":emoji_id
    }
  }
  request = requests.patch(url, headers=header, json=jsonData)
change_status(message, emoji_id)
