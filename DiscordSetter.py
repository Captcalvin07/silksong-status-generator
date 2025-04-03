import requests
import importlib.util
import sys

f = open("Info.txt", "r")
text = f.read().splitlines()

url = "https://discord.com/api/v10/users/@me/settings"

if text[1][0] == "n":
  message = text[1][1:]
elif text[1][0] == "f":
  spec = importlib.util.spec_from_file_location("module.name", text[1][1:])
  foo = importlib.util.module_from_spec(spec)
  sys.modules["module.name"] = foo
  spec.loader.exec_module(foo)
  message = foo.generate_status()

if text[2][0] == "n":
  emoji_id = text[2][1:]
elif text[2][0] == "f":
  spec = importlib.util.spec_from_file_location("module.name", text[2][1:])
  foo = importlib.util.module_from_spec(spec)
  sys.modules["module.name"] = foo
  spec.loader.exec_module(foo)
  message = foo.generate_emoji()

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
