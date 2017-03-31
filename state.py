# -*- coding: utf8 -*-
def traitement(param):
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
	#print (states)
	#print(states.has_key(param))
	if param in capital_cities.values():
		print('ok')
		for key in capital_cities:
			if capital_cities[key] == param:
				print(states[param])
	else:
		print('Unknown capital city')
		
if __name__ == '__main__':
	import sys
	if len(sys.argv) == 2:
		traitement(sys.argv[1])