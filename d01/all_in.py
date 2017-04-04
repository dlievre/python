
def isState(param, states, capital_cities):
	if param in states:
		return getCapitalOfState(param, states, capital_cities)

def isCapital(param, states, capital_cities):
	if param in capital_cities.values():
		return getStateOfCapital(param, states, capital_cities)

def getStateOfCapital(param, states, capital_cities):
	if param in capital_cities.values():
		for key in capital_cities:
			if capital_cities[key] == param:
				for key2 in states:
					if states[key2] == key:
						return key2

def getCapitalOfState(param, states, capital_cities):
	return capital_cities[states[param]]

def formatWord(param):
	resulta = param.rstrip()
	resultb = resulta.lstrip()
	resultc = resultb.title()
	return resultc
	
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
		for paramBrut in newlist:
			param = formatWord(paramBrut)
			St = 0
			Ca = 0
			chkState = isState(param, states, capital_cities)
			if chkState:
				St = 1
				print (getCapitalOfState(param, states, capital_cities), 'is the capital of', param)
			chkCapital = isCapital(param, states, capital_cities)
			if chkCapital:
				Ca = 1
				print (param, 'is the capital of', getStateOfCapital(param, states, capital_cities))
			if Ca + St == 0 and len(param) >0:
				print (paramBrut.rstrip().lstrip(),'is neither a capital city nor a state')	