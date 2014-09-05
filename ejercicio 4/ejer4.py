def ValorCadena(a,b):
	c=len(a)
	d=len(b)
	if c<d:
		return b
	if d<c:
		return b
	if d==c:
		return d+c
print "introduzca la primera cadena"
a=input()
print "introduzca la segunda cadena"
b=input()
print ValorCadena(a,b)