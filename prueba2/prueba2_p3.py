paisesCapitales = {
    "España": "Madrid",
    "México": "Ciudad de México",
    "Chile": "Santiago",
    "Argentina": "Buenos Aires",
    "Colombia": "Bogotá"
}

nombreTurista = input("Ingrese el nombre del turista: ")
paisProcedencia = input("Ingrese el pais de procedencia del turista: ")

if paisProcedencia in paisesCapitales:
    capital = paisesCapitales[paisProcedencia]
    mensaje = "El turista con el nombre " + nombreTurista + " viene del país "
    + paisProcedencia + " y su capital es " + capital + "."
    print(mensaje)
else:
    print("No se encontró información de capital para el pais", paisProcedencia)
