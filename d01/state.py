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
	if param in capital_cities.values():
		for key in capital_cities:
			if capital_cities[key] == param:
				for key2 in states:
					if states[key2] == key:
						print(key2)
	else:
		print('Unknown capital city')
		
if __name__ == '__main__':
	import sys
	if len(sys.argv) == 2:
		traitement(sys.argv[1])