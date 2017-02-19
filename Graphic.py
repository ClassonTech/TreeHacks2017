import random
from graphics import *
from shelters1.py import *

def areaCirc (area):
	return (1.0*area/3.142)**0.5


def main():
	win = GraphWin("Everybody Lives", 1024, 605)
	
	shelters = ["shelter1", "shelter2", "shelter3", "shelter4", "shelter5", "shelter6"]
	#shelters randomly over or under capacity within a range
	shelterCapacities = [random.randint(20, 30), random.randint(40, 50), random.randint(50, 60), 
	  					 random.randint(10,90), random.randint(30, 70), random.randint(10, 20)]
	shelterAnimals = [makeList(random.randint(20, 30), shelters[0]), makeList(random.randint(40, 50), shelters[1]), makeList(random.randint(50, 60), shelters[2]), 
	  			      makeList(random.randint(10,90), shelters[3]), makeList(random.randint(30, 70), shelters[4]), makeList(random.randint(10, 20), shelters[5])]

	print(shelters, shelterCapacities, shelterAnimals)
	printData([shelters, shelterCapacities, shelterAnimals])

	mapImage = Image(Point(512, 302.5), "map1.gif")
	mapImage.draw(win)


	pt1 = Point(684, 571)
	cir1 = Circle(pt1, areaCirc(len(shelterAnimals[0])))
	cir1.setOutline(color_rgb(160, 80, 255))
	cir1.draw(win)
	cir1.setWidth(2.25)

	pt2 = Point(452, 539)
	cir2 = Circle(pt2, areaCirc(len(shelterAnimals[1])))
	cir2.setOutline(color_rgb(160, 80, 255))
	cir2.draw(win)
	cir2.setWidth(2.25)

	pt3 = Point(441, 505)
	cir3 = Circle(pt3, areaCirc(len(shelterAnimals[2])))
	cir3.setOutline(color_rgb(160, 80, 255))
	cir3.draw(win)
	cir3.setWidth(2.25)

	pt4 = Point(343, 404)
	cir4 = Circle(pt4, areaCirc(len(shelterAnimals[3])))
	cir4.setOutline(color_rgb(160, 80, 255))
	cir4.draw(win)
	cir4.setWidth(2.25)

	pt5 = Point(270, 226)
	cir5 = Circle(pt5, areaCirc(len(shelterAnimals[4])))
	cir5.setOutline(color_rgb(160, 80, 255))
	cir5.draw(win)
	cir5.setWidth(2.25)

	pt6 = Point(367, 132)
	cir6 = Circle(pt6, areaCirc(len(shelterAnimals[5])))
	cir6.setOutline(color_rgb(160, 80, 255))
	cir6.draw(win)
	cir6.setWidth(2.25)

	#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~Redistribute~~~~~~~~~~~~~~~~~~~
	redistribute([shelters, shelterCapacities, shelterAnimals])
	printRecommendedDistribution([shelters, shelterCapacities, shelterAnimals])
	printData([shelters, shelterCapacities, shelterAnimals])

	cir12 = Circle(pt1, areaCirc(len(shelterAnimals[0])))
	cir12.setOutline(color_rgb(160, 80, 255))
	cir12.draw(win)
	cir12.setWidth(2.25)

	cir22 = Circle(pt2, areaCirc(len(shelterAnimals[1])))
	cir22.setOutline(color_rgb(160, 80, 255))
	cir22.draw(win)
	cir22.setWidth(2.25)

	cir32 = Circle(pt3, areaCirc(len(shelterAnimals[2])))
	cir32.setOutline(color_rgb(160, 80, 255))
	cir32.draw(win)
	cir32.setWidth(2.25)

	cir42 = Circle(pt4, areaCirc(len(shelterAnimals[3])))
	cir42.setOutline(color_rgb(160, 80, 255))
	cir42.draw(win)
	cir42.setWidth(2.25)

	cir52 = Circle(pt5, areaCirc(len(shelterAnimals[4])))
	cir52.setOutline(color_rgb(160, 80, 255))
	cir52.draw(win)
	cir52.setWidth(2.25)

	cir62 = Circle(pt6, areaCirc(len(shelterAnimals[5])))
	cir62.setOutline(color_rgb(160, 80, 255))
	cir62.draw(win)
	cir62.setWidth(2.25)

	#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
	MainRectangle = Rectangle(Point(802, 552), Point(1021, 602))
	MainRectangle.setFill(color_rgb(255, 255, 255))
	MainRectangle.setOutline(color_rgb(0, 0, 0))
	MainRectangle.draw(win)

	Logo = Text(Point(910, 570), "Everybody Lives")
	Logo.setFace("courier")
	Logo.setSize(18)
	Logo.draw(win)

	Stan = Text(Point(910, 590), "Stanford University | TreeHacks 2017")
	Stan.setFace("times roman")
	Stan.setSize(12)
	Stan.draw(win)

	



	win.getMouse()
	win.close()

main()	





