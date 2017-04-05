# -*- coding: latin-1 -*-
def openFile(file):
	fichier = open("numbers.txt", "r")
	contenu = fichier.read()
	try:
		contenu = contenu.replace("\n","")
		contenu = contenu.replace(",","\n")
		print (contenu)

	finally:
		fichier.close()

if __name__ == '__main__':
	openFile('numbers.txt')