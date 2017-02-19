import urllib2
import requests
import json
import random

json_data = {"apikey" : "y9CJUD8A", "objectType" : "animals", "objectAction": "publicSearch", 
			 "search" : {"calcFoundRows" : "Yes", "resultStart" : "0", "resultLimit" : "50", "resultSort" : "animalID", 
			 			 "fields" : ["animalID", "animalName"], 
			 			 "filters" : [{"fieldName" : "animalStatus", "operation" : "equals", "criteria" : "Available"}]}}

json_encoded = json.dumps(json_data)
url = "https://api.rescuegroups.org/http/v2.json";
headers = {'Content-type': 'application/json'}
r = requests.post(url, data=json_encoded, headers=headers)
filename = 'pets1.json'
with open(filename, 'w') as outfile:
    json.dump(r.json(), outfile)

json_data["search"]["resultStart"] = "50"
json_encoded = json.dumps(json_data)
r = requests.post(url, data=json_encoded, headers=headers)
filename = 'pets2.json'
with open(filename, 'w') as outfile:
	json.dump(r.json(), outfile)
json_data["search"]["resultStart"] = "100"
json_encoded = json.dumps(json_data)
r = requests.post(url, data=json_encoded, headers=headers)
filename = 'pets3.json'
with open(filename, 'w') as outfile:
    json.dump(r.json(), outfile)
json_data["search"]["resultStart"] = "150"
json_encoded = json.dumps(json_data)
r = requests.post(url, data=json_encoded, headers=headers)
filename = 'pets4.json'
with open(filename, 'w') as outfile:
    json.dump(r.json(), outfile)
json_data["search"]["resultStart"] = "200"
json_encoded = json.dumps(json_data)
r = requests.post(url, data=json_encoded, headers=headers)
filename = 'pets5.json'
with open(filename, 'w') as outfile:
    json.dump(r.json(), outfile)
json_data["search"]["resultStart"] = "250"
json_encoded = json.dumps(json_data)
r = requests.post(url, data=json_encoded, headers=headers)
filename = 'pets6.json'
with open(filename, 'w') as outfile:
    json.dump(r.json(), outfile)
