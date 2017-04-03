# -*- coding: latin-1 -*-
def openFile(file):
	fichier = open("numbers.txt", "r")
	contenu = fichier.read()
	try:
		new = contenu.replace(",","\n")
		print (new)

	finally:
		fichier.close()

if __name__ == '__main__':
	openFile('numbers.txt')