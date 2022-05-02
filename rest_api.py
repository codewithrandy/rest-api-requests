### WATCH THE VIDEO TUTORIAL ON MY YOUTUBE CHANNEL
### https://youtu.be/K1JgQsgWFio

import requests

base_url = 'https://api.sunrise-sunset.org/json?'
parameters = {
	'lat': 56.7201600,
	'lng': -4.4203400,
	'date': '2022-12-25',
}
response = requests.get(base_url, params=parameters)
data = response.json()
print('Sunrise is at:', data.get('results').get('sunrise'))