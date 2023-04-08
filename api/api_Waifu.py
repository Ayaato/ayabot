import requests
import key_RapidApi as key

def waifu_chat(message):

    url = "https://waifu.p.rapidapi.com/path"

    querystring = {
        "user_id":"sample_user_id",
        "message":f"{message}",
        "from_name":"Ömer",
        "to_name":"Girl",
        "situation":"Girl loves Ömer.",
        "translate_from":"auto",
        "translate_to":"auto"
        }

    payload = {}
    headers = {
        "content-type": "application/json",
        "X-RapidAPI-Key": f"{key.key}",
        "X-RapidAPI-Host": "waifu.p.rapidapi.com"
    }

    response = requests.request("POST", url, json=payload, headers=headers, params=querystring)

    return response.text