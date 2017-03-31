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
	if param in states:
		print(capital_cities[states[param]])
	else:
		print('Unknown state')
		
if __name__ == '__main__':
	import sys
	if len(sys.argv) == 2:
		traitement(sys.argv[1])