import requests

def chat_with_ai(message):

    url = "https://ai-chatbot.p.rapidapi.com/chat/free"

    querystring = {
        "message":f"{message}",
        "uid":"user1"}

    headers = {
        "X-RapidAPI-Key": "Your-RapidAPI-Key",
        "X-RapidAPI-Host": "ai-chatbot.p.rapidapi.com"
    }

    response = requests.request("GET", url, headers=headers, params=querystring)

    return response.text