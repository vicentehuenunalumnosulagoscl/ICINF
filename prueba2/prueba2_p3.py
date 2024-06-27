paisesCapitales = {}

for i in range(5):
    pais = input("Ingrese un país: ")
    capital = input("Ingrese la capital de {}: ".format(pais))
    paisesCapitales[pais] = capital

nombreTurista = input("Ingrese el nombre del turista: ")
paisProcedencia = input("Ingrese el país de procedencia del turista: ")

if paisProcedencia in paisesCapitales:
    capital = paisesCapitales[paisProcedencia]
    mensaje = "El turista con el nombre {} viene del país {} y su capital es {}.".format(nombreTurista, paisProcedencia, capital)
    print(mensaje)
else:
    print("No se encontró información de capital para el país", paisProcedencia)
