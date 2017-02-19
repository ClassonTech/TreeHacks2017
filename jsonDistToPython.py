import json

#pull return vals where first = location dict, second = street address

#END RESULT OF THIS FILE
#generates a map with:
#key: street address of shelter (so use the other map 
#	"shelter_name_to_street" in order to get street address)
#Value: dictionary of all distances and durations of trip
#	from current (key) shelter to all other shelters
#	can get to diff shelters using map above to go from
#	name to street address

def populate_shelter_locations():
	#uploading json distance files into python usable elems
	filename1 = 'PaloAltoHumaneSociety.json'
	filename2 = 'PeninsulaHumaneSociety.json'
	filename3 = 'PetsinNeedShelter.json'
	filename4 = 'SiliconValleyHumaneSociety.json'
	filename5 = 'BerkeleyHumane.json'
	filename6 = 'SanFranciscoAnimalCareandControl.json'

	#map to hold street address of each shelter
	shelter_name_to_street = {}

	#using filename1 for init
	#Palo Alto Humane Society
	vector = {}
	i = 0
	with open(filename1, 'rw') as infile:
		locationData1 = json.load(infile)
		shelter_name_to_street["Palo Alto Humane Society"] = locationData1["origin_addresses"]
		while (i < 5):
			vector[locationData1["destination_addresses"][i]] = locationData1["rows"][0]["elements"][i]
			i +=1

	shelter_location_data = {}
	shelter_location_data["Palo Alto Humane Society"] = vector

	#Peninsula Humane Society
	vector = {}
	i = 0
	with open(filename2, 'rw') as infile:
		locationData1 = json.load(infile)
		shelter_name_to_street["Peninsula Humane Society"] = locationData1["origin_addresses"]
		while (i < 5):
			vector[locationData1["destination_addresses"][i]] = locationData1["rows"][0]["elements"][i]
			i +=1

	shelter_location_data["Peninsula Humane Society"] = vector

	#Pets in Need Shelter
	vector = {}
	i = 0
	with open(filename3, 'rw') as infile:
		locationData1 = json.load(infile)
		shelter_name_to_street["Pets in Need Shelter"] = locationData1["origin_addresses"]
		while (i < 5):
			vector[locationData1["destination_addresses"][i]] = locationData1["rows"][0]["elements"][i]
			i +=1

	shelter_location_data["Pets in Need Shelter"] = vector

	#Silicon Valley Humane Society
	vector = {}
	i = 0
	with open(filename4, 'rw') as infile:
		locationData1 = json.load(infile)
		shelter_name_to_street["Silicon Valley Humane Society"] = locationData1["origin_addresses"]
		while (i < 5):
			vector[locationData1["destination_addresses"][i]] = locationData1["rows"][0]["elements"][i]
			i +=1

	shelter_location_data["Silicon Valley Humane Society"] = vector

	#Berkeley Humane
	vector = {}
	i = 0
	with open(filename5, 'rw') as infile:
		locationData1 = json.load(infile)
		shelter_name_to_street["Berkeley Humane"] = locationData1["origin_addresses"]
		while (i < 5):
			vector[locationData1["destination_addresses"][i]] = locationData1["rows"][0]["elements"][i]
			i +=1

	shelter_location_data["Berkeley Humane"] = vector

	#San Francisco Animal Care and Emergency
	vector = {}
	i = 0
	with open(filename6, 'rw') as infile:
		locationData1 = json.load(infile)
		shelter_name_to_street["San Francisco Animal Care and Emergency"] = locationData1["origin_addresses"]
		while (i < 5):
			vector[locationData1["destination_addresses"][i]] = locationData1["rows"][0]["elements"][i]
			i +=1

	shelter_location_data["San Francisco Animal Care and Emergency"] = vector

	return shelter_location_data, shelter_name_to_street