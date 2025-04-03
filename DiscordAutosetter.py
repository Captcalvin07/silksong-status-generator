from SilksongGenerator.py import generate_status
import requests

url = "https://discord.com/api/v10/users/@me/settings"

message = generate_status()

def change_status(message):

  header = {
    "authorization": "Insert Auth Token Here"
  }

  jsonData = {
    "status": "online"
    "custom_status": {
      "text": message
    }
  }
  request = requests.path(url, headers=header, json=jsonData)
change_status(message)
