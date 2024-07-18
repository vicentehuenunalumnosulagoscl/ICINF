def soloNumeros(var):
    return var.isdigit()

entrada = input("Ingrese un valor: ")

if soloNumeros(entrada):
    print("True")
else:
    print("False")
