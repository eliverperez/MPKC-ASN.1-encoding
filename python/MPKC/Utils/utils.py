from sage.all import *
#from sage.rings.finite_rings.finite_field_prime_modn import FiniteField_prime_modn_with_category
#from sage.rings.polynomial.polynomial_ring import PolynomialRing_dense_mod_p_with_category

''' Converts the byte array to a vector in the vector space (Fq)^n
'''
def binToGF2nElm(b,Fq):
	# str must be a bin array
	m = Fq.degree()
	l = len(b)
	x = Fq.gen()
	Y = vector(Fq,floor(8 * l / m))
	for i in range(len(Y)):
		j = floor((i * m) / 8)
		idx = (i * m) % 8
		y = b[j] >> idx
		j += 1
		s = 1
		while j <= floor((i+1)*m / 8):
			y = y | (b[j] << 8*s-idx)
			j += 1
		y = y % Fq.order()
		Y[i] = Fq.fetch_int(y)
	return Y;

''' Converts the vector in (Fq)^n to a byte array
'''
def GF2nElmToBin(xarray,Fq):
	l = len(xarray)
	m = Fq.degree()
	y = 0
	b = bytearray(ceil(m*l/8))
	for i in range(l):
		y = y | (xarray[i].integer_representation() << (i * m))
	for i in range(len(b)):
		b[i] = ((y >> 8*i) & 0xff)
	return b


def intToBin(n, l=0):
	i = 0
	ba = bytearray()
	while n > 0:
		ba.append(n & 0xFF)
		n = n >> 8
	if l > 0:
		if len(ba) > l:
			ba = ba[:l]
		elif len(ba) < l:
			ba1 = bytearray(l)
			ba1[l - len(ba):] =  ba[:]
			ba = ba1
	return ba

def binToInt(ba):
	n = 0
	for i in range(len(ba)):
		n = n | (ba[i] << (8*i))
	return n

''' Higher degree in leftmost position
def polToInt(pol):
	polInt = 0
	coeff = pol.list()
	for i in range(len(coeff)):
		if coeff[i] == 1:
			polInt = polInt | (1 << i)
	return polInt'''

def polToInt(pol):
	return int(pol)

def polToBin(pol):
	return intToBin(polToInt(pol))

'''
'''
def quadraticPolToInt(p):
	bin = 0
	vars = p.parent().gens()
	varNum = len(vars)
	#Quadratic coefficients
	for i in range(varNum):
		for j in range(i, varNum):
			c = int(p.coefficient(vars[i]*vars[j]))
			bin = (bin << 1) | c
			p = p - c*vars[i]*vars[j]
	#Linear coefficients
	for i in range(varNum):
		c = int(p.coefficient(vars[i]))
		bin = (bin << 1) | c
	#Constant coefficient
	bin = (bin << 1) | int(p.constant_coefficient())
	return bin

''' FROM OLD CODE '''
def encodeAffine(self, affine):
	baseField = affine.matrix()[0,0].parent()
	deg = baseField.polynomial().degree()
	affineMatrix = affine.matrix()[0:deg, 0:deg]
	affineVector = affine.matrix()[0:deg, deg:deg+1]
	affineMatrixBin = bytearray()
	affineVectorBin = bytearray()
	for i in range(deg):
		affine1Matrix.append(GF2nElmToBin(affineMatrix[i]), baseField)
	affine1VectorBin.append(GF2nElmToBin(affineVector), baseField)

''' Int to 0-1 polynomials for base and extension fields'''
def getBaseAndExtension(self, m, n):
	#r.<X>=GF(2)[]
	r = PolynomialRing(GF(7), 'X')
	pol = 0
	i = 0
	while (m > 0):
		pol = pol + (m & 1)*X**i
		m = m >> 1
		i += 1
	k=GF(2**pol.degree(), 'x', pol)
	R=PolynomialRing(k,'T')
	T=R.gens()[0]
	i = 0
	pol = k(0)
	while n > 0:
		pol = pol + k(n & 1)*T**i
		n = n >> 1
		i += 1
	K=k.extension(T**37+T**12+T**10+T**2+1, 't')
	return k, K
