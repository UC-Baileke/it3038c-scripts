import json
import requests


print('Please enter your zip code: ')
zip = input()

r= requests.get('http://api.openweathermap.org/data/2.5/weather?zip=%s&appid=8265009e72ead666b18608e591a2fdc5' % zip)

data = r.json()

print(data['weather'] [0] ['description'])
