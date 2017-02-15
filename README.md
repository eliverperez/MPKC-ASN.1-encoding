# ASN.1
Archivo "generarPolinomiosCompuestos.sage"

Ejecutar SageMath y cargar el archivo utilizando la funcion "load()"

load("generarPolinomiosCompuestos.sage") ——> ya que si se ejecuta utilizando sage -python archivo da error por utilizar funciones de sage en un archivo .py

Te pedira un numero para las variables, numero para cuantos polinomios se generaran y el campo donde estaran sus coeficientes, p que es la caracteristica del campo y d el grado del campo.

se generan los polinomios con la funcion genPolynomials en el mismo archivo y se almacenan en la variable 

"PolySet"










Para la codificacion se instancia la clase SflashEncoder()

encoder = SflashEncoder("BER")

y se ejecuta la funcion encodePublicKey() que recibe como parametros, la lista de polinomios que se estan trabajando, el numero de variables, la caracteristica y el grado del campo donde se esta trabajando.

publicBin = encoder.encodePublicKey(PolySet, n, p, d)

Se almacena en un archivo con extension .pub






Para la decodificacion se instancia la clase SflashDecoder()

decoder = SflashDecoder("BER")

se abre el archivo donde se encuentra el texto codificado

file = open(filename + ".pub", "rb")

y para decodificar se llama al metodo decodePublicKey() de la clase SflashDecoder()

polys = decoder.decodePublicKey(file)





los polinomios se almacenan en la variable polys, puedes verificar que son los mismo comparando estas 2 variables
