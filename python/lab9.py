import json
import requests

r= requests.get('http://localhost:3000')

data = r.json()


a = data[0]['color']
b = data[1]['color']
c = data[2]['color']
d = data[3]['color']

print("Widget 1 is %s" % a) 

print("Widget 2 is %s" % b)

print("Widget 3 is %s" % c)

print("Widget x is %s" % d)

