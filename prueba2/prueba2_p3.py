paisesCapitales = {}

while True:
    pais = input("Ingrese un país o pulse '0' para terminar: ")
    if pais.lower() == '0':
        break
    capital = input("Ingrese la capital de {}: ".format(pais))
    paisesCapitales[pais] = capital
nombreTurista = input("Ingrese el nombre del turista: ")
paisProcedencia = input("Ingrese el país de procedencia del turista: ")

if paisProcedencia in paisesCapitales:
    capital = paisesCapitales[paisProcedencia]
    mensaje = "El turista con el nombre " + nombreTurista + " viene del país " + paisProcedencia + " y su capital es " + capital + "."
    print(mensaje)
else:
    print("No se encontró información de capital para el país", paisProcedencia)
