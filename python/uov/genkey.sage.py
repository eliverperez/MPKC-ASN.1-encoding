# This file was *autogenerated* from the file genkey.sage
from sage.all_cmdline import *   # import sage library
_sage_const_3 = Integer(3); _sage_const_2 = Integer(2); _sage_const_1 = Integer(1); _sage_const_1p0 = RealNumber('1.0'); _sage_const_3p0 = RealNumber('3.0'); _sage_const_100000 = Integer(100000)
load('/home/edgar/Documents/UOV/uov.sage')
load('/home/edgar/Documents/UOV/cryptokeys.sage')
import copy
import sys

###################################################
#   Program to generate keys for authentication   #
#                                                 #
#   Jose Luis Juan Herrera Garcia       May, 2015 #
#   Thesis work                                   #
#   Computer science graduate studies             #
#   CINVESTAV                                     #
###################################################

reset() # Erase all previously defined variables

###################################################
#                      Add-on's                   #
###################################################
import copy
import sys
load('/home/edgar/Documents/UOV/uov.sage')
load('/home/edgar/Documents/UOV/cryptokeys.sage')
        
###################################################
#                  Initialization                 #
###################################################
if ( len( sys.argv ) != _sage_const_3  ):
    print "\nUsage: genkey NumVars EncryptedFile\n\n"
    sys.exit(_sage_const_1 )
else:
    try:
        n = int( sys.argv[_sage_const_1 ] )
    except:
        print "\nNumVars must be an integer number\n\n"
        sys.exit(_sage_const_2 )
    encFile = sys.argv[_sage_const_2 ]
    
extPI = ".ir"   # File name extension for files with polys represented as ints
extMV = ".mv"   # File name extension for files with Matrix an vector
CTE  = _sage_const_100000    # Just a constant to be added to the constant term of poly
porc = _sage_const_1p0 /_sage_const_3p0   # Percentage of Oil variables

o = int(n*porc) # Number of Oil variables
v = n-o         # Number of Vinegar variables


a = list(var('a%d' % i) for i in range(n))  # Define 'a' list.
x = list(var('x%d' % i) for i in range(n))  # Define 'x' list. No matter
                                            # its content
k = PolynomialRing( GF(_sage_const_2 ), len(a) + len(x),
                    a + x )                 # Polynomial ring in 'n' variables
for i in range(n):          # Now 'a' and 'x' list have generators
    a[i] = k.gen(i)
    x[i] = k.gen(len(a) + i)

y    = vector(GF(_sage_const_2 ), o)     # Evaluation of polynomial (Pi)
yUOV = vector(GF(_sage_const_2 ), o)     # Evaluation of polynomial (PiUOV)

Ms    = matrix(GF(_sage_const_2 ), n, n) # Matrix for affine transformation
vs    = vector(GF(_sage_const_2 ), n)    # Vector for affine transformation
Pi    = vector(k, o)        # 'o' polynomials will be generated
PiUOV = vector(k, o)        # 'o' polynomials will be generated

set_random_seed()	    # Set a random seed for RNG

###################################################
#                     Main code                   #
###################################################
print "\nSecret and Public Key generation for Zero Knowledge \
Authentication\n"
print "Number of variables:        ", n
print "Number of vinegar variables:", v
print "Number of oil variables:    ", o

##### Generate elements for affine transformation:
print "\nComputing 'Ms' matrix"
genRndMatrix(Ms)
print "\nComputing 'vs' vector"
genRndVector(vs)

####### Generate polynomial "P'" (PiUOV):
print "\nGenerating polynomial PiUOV. {0} equations".format(o)
genPolyVectorUOV(o, v, a, PiUOV, Debug = True)

####### Generate polynomial "P" (Pi):
print "\nGenerating polynomial Pi. {0} equations".format(o)
A = S(Ms, vector(x), vs)    # First generate affine transformation
evalPolyVect(PiUOV, a, A, Pi, Debug = True)

####### Writing encrypted file with private and public key
#pp = readPP("\nPlease enter pass-phrase to encrypt private key file: ")
writeKeysEnc(PiUOV, Ms, vs, Pi, 'nopassword', easyK, encFile)

storePublicKey(Pi, 'pubKey.txt')

print "\ndone!\n"