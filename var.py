# -*- coding: latin-1 -*-
def my_var():
	msg = "est de type"
	n = int(42)
	print (n, msg , type(n))
	n = "42"
	print (n, msg , type(n))
	n = "quqrante-deux"
	print (n, msg , type(n))
	n = 42.0
	print (n, msg , type(n))
	n = True
	print (n, msg , type(n))
	n = [42]
	print (n, msg , type(n))
	n = {42: 42}
	print (n, msg , type(n))
	n = (42,)
	print (n, msg , type(n))
	n = set()
	print (n, msg , type(n))

if __name__ == '__main__':
	my_var()