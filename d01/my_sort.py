def traitement():
	d={
	'Hendrix'   :   '1942',
	'Allman'    :   '1946',
	'King'      :   '1925',
	'Clapton'   :   '1945',
	'Johnson'   :   '1911',
	'Berry'     :   '1926',
	'Vaughan'   :   '1954',
	'Cooder'    :   '1947',
	'Page'      :   '1944',
	'Richards'  :   '1943',
	'Hammett'   :   '1962',
	'Cobain'    :   '1967',
	'Garcia'    :   '1942',
	'Beck'      :   '1944',
	'Santana'   :   '1947',
	'Ramone'    :   '1948',
	'White'     :   '1975',
	'Frusciante':   '1970',
	'Thompson'  :   '1949',
	'Burton'    :   '1939',
	}
	dict = {} # on crée un nouveau tableau avec comme keys les années
	for key in d:
		if d[key] not in dict:
			dict.update({d[key]:key})
		else:
			dict[d[key]] = dict[d[key]]+','+key# ajout value +, systématique
	for key in sorted(dict):
		tbl = []
		tbl  = dict[key].split(',')
		for musicien in sorted(tbl):
			print (musicien)

if __name__ == '__main__':
	traitement()