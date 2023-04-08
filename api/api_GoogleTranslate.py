import requests
import key_RapidApi as key

def translated_text(text):
    url = "https://google-translate1.p.rapidapi.com/language/translate/v2"

    payload = f"q={text}&target=en&source=tr"
    headers = {
        "content-type": "application/x-www-form-urlencoded",
        "Accept-Encoding": "application/gzip",
        "X-RapidAPI-Key": f"{key.key}",
        "X-RapidAPI-Host": "google-translate1.p.rapidapi.com"
    }

    try:
        response = requests.request("POST", url, data=payload, headers=headers)
    except UnicodeEncodeError:
        return "Lütfen Türkçe karakter kullanmadan deneyin."

    return response.json()['data']['translations'][0]['translatedText']