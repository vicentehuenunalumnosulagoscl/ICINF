def potencia(num, exp):
    if exp == 0:
        return 1
    else:
        return num * potencia(num, exp - 1)

num = int(input("Ingrese la base: "))
exp = int(input("Ingrese el exponente: "))

res = potencia(num, exp)

print(num, "elevado a ", exp, "es igual a", res)