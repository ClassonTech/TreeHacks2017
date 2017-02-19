import json
import random
import pprint

#Generating rand vals for shelters

capacities = [random.randint(20, 30), random.randint(40, 50), random.randint(50, 60), 
  			  random.randint(10,90), random.randint(30, 70), random.randint(10, 20)]

example_data =  {"Palo Alto Humane Society" : {"coordinates": ["37.4520087, -122.1855668"],"name": "Palo Alto Humane Society"},
				"Penisula Humane Society": {"coordinates": ["37.5873817, -122.3311192"],"name": "Penisula Humane Society"},
				"Pets in Need Shelter": {"coordinates": ["37.4812022, -122.1991530"],"name": "Pets in Need Shelter"},
				"Silicon Valley Humane Society": {"coordinates": ["37.4215079, -121.8870551"],"name": "Silicon Valley Humane Society"},
				"Berkeley Humane": {"coordinates": ["37.8570665, -122.2912348"],"name": "Berkeley Humane"},
				"San Francisco Animal Care and Control": {"coordinates": ["37.7673645, -122.4129426"],"name": "San Francisco Animal Care and Control"}}

filename = 'shelterdata.json'
with open(filename, 'w') as outfile:
    json.dump(example_data, outfile)

filename = 'shelterdata.json'
with open(filename, 'rw') as infile:
 	shelters_data = json.load(infile)

 	vector = {}
	filename2 = 'pets1.json'
	with open(filename2, 'r') as infile:   
		data = json.load(infile)
		for animal in data["data"]:
			vector[data["data"][animal]["animalID"]] = [data["data"][animal]["animalName"], 0, True]
 	
 	shelters_data["Palo Alto Humane Society"]["animals"] = vector
 	shelters_data["Palo Alto Humane Society"]["capacity"] = capacities[0]

 	vector = {}
	filename2 = 'pets2.json'
	with open(filename2, 'r') as infile:   
		data = json.load(infile)
		for animal in data["data"]:
			vector[data["data"][animal]["animalID"]] = [data["data"][animal]["animalName"], 0, True]
 	
 	shelters_data["Penisula Humane Society"]["animals"] = vector
 	shelters_data["Penisula Humane Society"]["capacity"] = capacities[1]

 	vector = {}
	filename2 = 'pets3.json'
	with open(filename2, 'r') as infile:   
		data = json.load(infile)
		for animal in data["data"]:
			vector[data["data"][animal]["animalID"]] = [data["data"][animal]["animalName"], 0, True]
 	
 	shelters_data["Pets in Need Shelter"]["animals"] = vector
 	shelters_data["Pets in Need Shelter"]["capacity"] = capacities[2]

 	vector = {}
	filename2 = 'pets4.json'
	with open(filename2, 'r') as infile:   
		data = json.load(infile)
		for animal in data["data"]:
			vector[data["data"][animal]["animalID"]] = [data["data"][animal]["animalName"], 0, True]
 	
 	shelters_data["Silicon Valley Humane Society"]["animals"] = vector
 	shelters_data["Silicon Valley Humane Society"]["capacity"] = capacities[3]

 	vector = {}
	filename2 = 'pets5.json'
	with open(filename2, 'r') as infile:   
		data = json.load(infile)
		for animal in data["data"]:
			vector[data["data"][animal]["animalID"]] = [data["data"][animal]["animalName"], 0, True]
 	
 	shelters_data["Berkeley Humane"]["animals"] = vector
 	shelters_data["Berkeley Humane"]["capacity"] = capacities[4]

 	vector = {}
	filename2 = 'pets6.json'
	with open(filename2, 'r') as infile:   
		data = json.load(infile)
		for animal in data["data"]:
			vector[data["data"][animal]["animalID"]] = [data["data"][animal]["animalName"], 0, True]
 	
 	shelters_data["San Francisco Animal Care and Control"]["animals"] = vector
 	shelters_data["San Francisco Animal Care and Control"]["capacity"] = capacities[5]
	filename = 'shelterdata.json'

filename = 'example_data.json'
with open(filename, 'w') as outfile:
    json.dump(shelters_data, outfile)

#print(shelters_data)
print(shelters_data["Silicon Valley Humane Society"]["capacity"])
