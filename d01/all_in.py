# -*- coding: utf8 -*-
def isstate(param, states, capital_cities):
	if param in states:
		print(param, 'is a state')
		return getCapitalOfState(param, states, capital_cities)

def isCapital(param, states, capital_cities):
	if param in capital_cities.values():
		print(param, 'is a capital')
		return getStateOfCapital(param, states, capital_cities)

def getStateOfCapital(param, states, capital_cities):
	if param in capital_cities.values():
		for key in capital_cities:
			if capital_cities[key] == param:
				for key2 in states:
					if states[key2] == key:
						print(key2)
						return key2

def getCapitalOfState(param, states, capital_cities):
	return capital_cities[states[param]]
		
if __name__ == '__main__':
	import sys
	if len(sys.argv) == 2:
		states = {
			"Oregon"    : "OR",
			"Alabama"   : "AL",
			"New Jersey": "NJ",
			"Colorado"  : "CO"
			}
		capital_cities = {
			"OR": "Salem",
			"AL": "Montgomery",
			"NJ": "Trenton",
			"CO": "Denver"
			}
		newlist = sys.argv[1].split(',')
		for param in newlist:
			chkState = isstate(param, states, capital_cities)
			if chkState:
				print (getCapitalOfState(param, states, capital_cities), 'is the capital of', param)
			chkCapital = isCapital(param, states, capital_cities)
			if chkCapital:
				print (param, 'is the capital of', getStateOfCapital(param, states, capital_cities))

