import requests
import key_RapidApi as key

def chat_with_ai(message):

    url = "https://ai-chatbot.p.rapidapi.com/chat/free"

    querystring = {
        "message":f"{message}",
        "uid":"user1"}

    headers = {
        "X-RapidAPI-Key": f"{key.key}",
        "X-RapidAPI-Host": "ai-chatbot.p.rapidapi.com"
    }

    response = requests.request("GET", url, headers=headers, params=querystring)

    response = response.json()['chatbot']['response']

    if (response == 'Internal Server'):
        return "Lütfen Türkçe karakter kullanmadan deneyin."
    
    return response