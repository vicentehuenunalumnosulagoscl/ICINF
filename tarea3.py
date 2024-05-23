altura = float(input("Ingrese la altura de una persona (o 0 para terminar): "))
total_alturas = 0
numero_personas = 0

while altura != 0:
    total_alturas += altura
    numero_personas += 1
    altura = float(input("Ingrese la altura de una persona (o 0 para terminar): "))

if numero_personas > 0:
    promedio_altura = total_alturas / numero_personas
    print("La altura promedio es de: " + str(promedio_altura) + " metros")
else:
    print("No se ingresaron alturas")
