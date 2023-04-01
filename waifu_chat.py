import requests
from translate import *

def waifu_chat(message):

    url = "https://waifu.p.rapidapi.com/path"

    querystring = {
        "user_id":"sample_user_id",
        "message":f"{message}",
        "from_name":"You",
        "to_name":"Girl",
        "situation":"Girl loves You.",
        "translate_from":"auto",
        "translate_to":"auto"
        }

    payload = {}
    headers = {
        "content-type": "application/json",
        "X-RapidAPI-Key": "Your-RapidAPI-Key",
        "X-RapidAPI-Host": "waifu.p.rapidapi.com"
    }

    response = requests.request("POST", url, json=payload, headers=headers, params=querystring)

    return response.text

def waifu_delete():
    url = "https://waifu.p.rapidapi.com/v1/user/dialog/sample_user_id"

    headers = {
	    "X-RapidAPI-Key": "20f573414amsh9541b83d962a293p196bb2jsn71986416f433",
	    "X-RapidAPI-Host": "waifu.p.rapidapi.com"
    }

    response = requests.request("DELETE", url, headers=headers)

    return response.text