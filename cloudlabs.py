import requests

url = "https://cloudlabs-text-to-speech.p.rapidapi.com/synthesize"

def text_to_speech(message):

	message_words = message.split()

	message = list(map(lambda message_word:message_word+"%20",message_words))

	payload = f"voice_code=tr-TR-1&text={message}&speed=1.00&pitch=1.00&output_type=audio_url"
	headers = {
		"content-type": "application/x-www-form-urlencoded",
		"X-RapidAPI-Key": "Your-RapidAPI-Key",
		"X-RapidAPI-Host": "cloudlabs-text-to-speech.p.rapidapi.com"
	}

	response = requests.request("POST", url, data=payload, headers=headers)

	return response.text