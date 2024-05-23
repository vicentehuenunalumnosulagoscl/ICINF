sueldos_bajos = 0
sueldos_altos = 0
gasto_total = 0

print("Ingrese los sueldos de los empleados mensualmente. Ingrese -1 para finalizar.")

sueldo = int(input("Ingrese el sueldo del empleado: "))
while sueldo != -1:
    if 500000 <= sueldo <= 900000:
        sueldos_bajos += 1
    elif sueldo > 900000:
        sueldos_altos += 1
    gasto_total += sueldo
    sueldo = int(input("Ingrese el sueldo del empleado: "))

print("Empleados que cobran entre $500.000 y $900.000: " + str(sueldos_bajos))
print("Empleados que cobran más de $900.000: " + str(sueldos_altos))
print("Gasto total en sueldos: $" + str(gasto_total))
