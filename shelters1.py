import random
import pprint
from jsonDistToPython import *

MAX_DISTANCE = 30

#Arbitrary initialization of Vector of animals in the form [{distanceMoved}, {origName}]
def makeList(numAnimals, vecName):
	myList = [];
	for i in range(0, numAnimals):
		myList.append([0, vecName, vecName + "pet" + str(i)])
	return myList

#Prints capacity, count, and most overloaded.
def printData(localShelters):
	maximumOverCapacityShelter = "Palo Alto Humane Society";
	maximumOverCapacity = -9999;
	for i in range(0, len(localShelters[0])):
		overcap = getOverCapacity(i, localShelters)
		if overcap > maximumOverCapacity:
			maximumOverCapacity = overcap
			maximumOverCapacityShelter = localShelters[0][i]
	print "Determined that ", maximumOverCapacityShelter, "is the most overloaded, at ", (str(maximumOverCapacity) + " animals above capacity." if maximumOverCapacity >= 0 else str(-maximumOverCapacity) + " animals below capacity.")
	# print "Shelters in this area have a variance of "

	for i in range(0, len(localShelters[0])):
		print localShelters[0][i], "animal count: \t", len(localShelters[2][i]), "| shelter capacity ", localShelters[1][i]

#Prints animals that chanegd places in O(N) time
def printRecommendedDistribution(localShelters):
	print "Recommend that the following shelters move these animals, optimized such that no animal is transported further than ", MAX_DISTANCE, "kilometers."
	for i in range(0, len(localShelters[0])):
		for animal in localShelters[2][i]:
			if(animal[1] == localShelters[0][i]): continue #don't move from same shelter 
			print "Move ", animal[2], animal[0], "kilometers from ", animal[1], "to", localShelters[0][i]
	print "---------------------------------------"
			

#To be connected to Google Maps API later
def getNeighborsWithinRange(shelter, localShelters):
	return localShelters

#To be connected to Google maps API later
def getDistance(shelter1, shelter2):
	if shelter1 == shelter2:
		return MAX_DISTANCE + 1 #don't move from one shelter to the same shelter
	addr2 = memoizedStreetNames[shelter2]
	return memoizedDistances[shelter1][addr2[0]]["distance"]["value"]/1000

def getMovableCount(shelter, localShelters):
	count = 0
	for animal in localShelters[2][shelter]:
		if(animal[0] < MAX_DISTANCE):
			count += 1
	return count

def getOverCapacity(shelter, localShelters):
	return len(localShelters[2][shelter]) - localShelters[1][shelter]

def bestBurden(neighbor_count, neighbor_capacities):
	totalcount = totalcapacities = 0
	totalcount = sum(neighbor_count)
	totalcapacities = sum(neighbor_capacities)
	burden = 1.0*totalcount/totalcapacities
	print "Shelters in this area have a", ("high" if burden >= 1 else "low"), "total concentration, at ", int(burden*1000)/10.0, "% total capacity."
	return burden

def printMovable(localShelters):
	for i in range(0, len(localShelters[0])):
		print getMovableCount(i, localShelters), "movable out of ", len(localShelters[2][i])
		print getOverCapacity(i, localShelters), "over capacity of ", localShelters[1][i]
	return

def redistribute(localShelters):
	maximumOverCapacityShelter = 0;
	maximumOverCapacity = 0;
	for i in range(0, len(localShelters[0])):
		overcap = getOverCapacity(i, localShelters)
		if overcap > maximumOverCapacity:
			maximumOverCapacity = overcap
			maximumOverCapacityShelter = localShelters[0][i]

	if recursiveRedistribute(localShelters[0].index(maximumOverCapacityShelter), localShelters):
		return True

def recursiveRedistribute(shelter, localShelters):
	neighbors = getNeighborsWithinRange(shelter, localShelters) #for right now, equal
	neighbor_count = []
	neighbor_capacities = []
	for i in range(0, len(neighbors[0])):
		neighbor_count.append(len(neighbors[2][i]))
		neighbor_capacities.append(neighbors[1][i])
	new_burden = bestBurden(neighbor_count, neighbor_capacities)
	num_animals_to_move = []
	for i in range(0, len(neighbors[0])):
		num_animals_to_move.append(int(new_burden*neighbor_capacities[i]-neighbor_count[i]))
	#This shelter picks up the int remainder of pets
	num_animals_to_move[shelter] += -sum(num_animals_to_move)
	optimalAnimalMove(num_animals_to_move, localShelters)

	return;

#currently assuming that all animals are available to transport
#will be based on a variety of factors:
#---going through adoption process
#---undergoing medical treatment
#---animal breed
#assumes animal of the form {distance moved, original shelter}
def animalTransportable(animal):
	if animal[0] < MAX_DISTANCE: return True
	return False

def withinRange(animal, distance):
	return animal[0] + distance <= MAX_DISTANCE

def optimalAnimalMove(num_animals_to_move, localShelters):
	temp_animals = []
	for i in range(0, len(localShelters[0])):
		count = num_animals_to_move[i]
		if count >= 0: continue; #first loop, only want overflow shelter(s)
		for animal in localShelters[2][i]:
			if count == 0: break #got rid of our overflow
			if(animalTransportable(animal)):
				temp_animals.append(animal)
				localShelters[2][i].remove(animal)
				count += 1
	for i in range(0, len(localShelters[0])):
		count = num_animals_to_move[i]
		if count <= 0 : continue; #second loop, only want shelter(s) with room
		for animal in temp_animals:
			if count == 0: break
			distance = getDistance(animal[1], localShelters[0][i])
			if not withinRange(animal, distance): continue
			animal[0] += distance
			localShelters[2][i].append(animal)
			temp_animals.remove(animal)
			count -= 1
	for animal in temp_animals: #all remaining animals stay in their shelters
		originalShelter = localShelters[0].index(animal[1])
		localShelters[2][originalShelter].append(animal)

shelters = ["Palo Alto Humane Society", "Peninsula Humane Society", "Pets in Need Shelter", "Silicon Valley Humane Society", "Berkeley Humane", "San Francisco Animal Care and Emergency"]
#shelters randomly over or under capacity within a range
shelterCapacities = [random.randint(20, 30), random.randint(40, 50), random.randint(50, 60), 
  					 random.randint(10,90), random.randint(30, 70), random.randint(10, 20)]
shelterAnimals = [makeList(random.randint(20, 30), shelters[0]), makeList(random.randint(40, 50), shelters[1]), makeList(random.randint(50, 60), shelters[2]), 
  			      makeList(random.randint(10,90), shelters[3]), makeList(random.randint(30, 70), shelters[4]), makeList(random.randint(10, 20), shelters[5])]
#access Google API to get distances between shelters
memoizedDistances, memoizedStreetNames = populate_shelter_locations()

printData([shelters, shelterCapacities, shelterAnimals])
redistribute([shelters, shelterCapacities, shelterAnimals])
printRecommendedDistribution([shelters, shelterCapacities, shelterAnimals])
printData([shelters, shelterCapacities, shelterAnimals])