import requests
import json
import key_RapidApi as key


url = "https://openai80.p.rapidapi.com/chat/completions"


def openai(message):
    payload = {
        "model": "gpt-3.5-turbo",
        "messages": [
            {
                "role": "user",
                "content": f"{message}"
            }
        ]
    }
    headers = {
        "content-type": "application/json",
        "X-RapidAPI-Key": f"{key.key}",
        "X-RapidAPI-Host": "openai80.p.rapidapi.com"
    }

    response = requests.request("POST", url, json=payload, headers=headers)

    return response.json()['choices'][0]['message']['content']