import requests

def translated_text(text):
    url = "https://google-translate1.p.rapidapi.com/language/translate/v2"

    payload = f"q={text}&target=en&source=tr"
    headers = {
        "content-type": "application/x-www-form-urlencoded",
        "Accept-Encoding": "application/gzip",
        "X-RapidAPI-Key": "Your-RapidAPI-Key",
        "X-RapidAPI-Host": "google-translate1.p.rapidapi.com"
    }

    response = requests.request("POST", url, data=payload, headers=headers)

    return response.text

print(translated_text("merhaba"))