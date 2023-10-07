import requests

url = "https://google-translate1.p.rapidapi.com/language/translate/v2"
Response = input('What would you like me to translate into Spanish for you?\n')
payload = {
	"q": Response,
	"target": "es",
	"source": "en"
}
headers = {
	"content-type": "application/x-www-form-urlencoded",
	"Accept-Encoding": "application/gzip",
	"X-RapidAPI-Key": "0142ab06f3mshf4e17c5911c470cp158874jsn7081aebc27a9",
	"X-RapidAPI-Host": "google-translate1.p.rapidapi.com"
}

response = requests.post(url, data=payload, headers=headers)

print(response.json())