total_preguntas = int(input("Ingrese el número total de preguntas realizadas al entrevistado: "))
respuestas_correctas = int(input("Ingrese el número de respuestas correctas del entrevistado: "))

porcentaje_correctas = (respuestas_correctas / total_preguntas) * 100

if porcentaje_correctas >= 95:
    print("El nivel de conocimiento del entrevistado es máximo")
elif porcentaje_correctas >= 70:
    print("El nivel de conocimiento del entrevistado es medio")
elif porcentaje_correctas >= 40:
    print("El nivel de conocimiento del entrevistado es regular")
else:
    print("El nivel de conocimiento del entrevistado es insuficiente")

print("El puntaje de la entrevista es de " + str(porcentaje_correctas) + "%")
