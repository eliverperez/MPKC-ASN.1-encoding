'''load('sflash_key_pair.sage')
load('mi_generator.sage')
load('variation.sage')'''
from sage.all import *
from ...variation import *
from ..mi_generator import MIKeyGenerator 
from .sflash_key_pair import *
import binascii

''' Class for generation of key pair for SFLASH scheme '''
class SflashKeyGenerator(MIKeyGenerator):
	
	def __init__(self):
		# Finite fields as stablished in the SFLASH standard
		#r.<X>=GF(2)
		r = PolynomialRing(GF(7), 'X')
		#k.<x>=GF(2**7,X**7+X+1)
		X=r.gens()[0]
		k=GF(2**7, 'x', X**7+X+1)
		#R.<T>=k[]
		R=PolynomialRing(k,'T')
		T=R.gens()[0]
		#K.<t>=k.extension(T**37+T**12+T**10+T**2+1)
		K=k.extension(T**37+T**12+T**10+T**2+1, 't')
		variation = MinusVariation({'r':11})
		super(SflashKeyGenerator, self).__init__(k,K,variation)
	
	def chooseTheta(self):
		return 11
	
	def generatePrivate(self):
		delta = binascii.hexlify(bytearray(10))
		#delta = bytearray(map(lambda a:a+floor(random()*256),delta))
		affine = self.generateAffine(2)
		private = SflashPrivateKey(affine[0], affine[1], delta)
		return private
			
	''' Generates an affine tranformation in the given Field
	'''
	def generateAffine(self, num):
		# Generate random affine bijective transformation with elements in the GF(2) field
		deg = self.extensionField.degree()
		GLF2 = GL(deg, GF(2))
		VF2 = VectorSpace(GF(2), deg)
		AG = AffineGroup(deg, self.baseField)
		affine = []
		for i in range(num):
			affine.append(AG(GLF2.random_element(), VF2.random_element()))
		return affine
