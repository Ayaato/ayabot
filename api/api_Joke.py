import requests
import key_RapidApi as key

url = "https://dad-jokes.p.rapidapi.com/joke/type/general"

headers = {
	"X-RapidAPI-Key": f"{key.key}",
	"X-RapidAPI-Host": "dad-jokes.p.rapidapi.com"
}
def dadjoke():
    response = requests.request("GET", url, headers=headers)

    return response.json()['message']