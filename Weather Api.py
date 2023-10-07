import requests

url = "https://weatherapi-com.p.rapidapi.com/current.json"
Town = input('What city would you like to know the weather for? ')
querystring = {"q":Town}

headers = {
	"X-RapidAPI-Key": "0142ab06f3mshf4e17c5911c470cp158874jsn7081aebc27a9",
	"X-RapidAPI-Host": "weatherapi-com.p.rapidapi.com"
}

response = requests.get(url, headers=headers, params=querystring)

print(response.json())