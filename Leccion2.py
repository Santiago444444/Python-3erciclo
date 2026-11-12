#PRIMERA PREGUNTA
print("ab" * 3)


#SEGUNDA PREGUNTA
ciudad = "Paute y"
print(ciudad[-1].upper())


#TERCERA PREGUNTA
print(int(9.99))


#CUARTA PREGUNTA
a = {1, 2, 3, 4}
b = {3, 4, 5}
print(len(a & b))


#QUINTA PREGUNTA
print(type(10.0))


#SEXTA PREGUNTA
for i in range(1, 10, 3):
    print(i, end=" ")


#SEPTIMA PREGUNTA
print([n ** 2 for n in [1, 2, 3, 4] if n % 2 == 0])


#OCTAVA PREGUNTA 
for i in range(3):
    for j in range(2):
        print("*", end="")


#NOVENA PREGUNTA
for i in range(3, 0, -1):
    print(i, end=" ")


#DECIMA PREGUNTA
saldo = 350
if saldo >= 1000:
    print("Oro")
elif saldo >= 100:
    print("Plata")
else:
    print("Básica")


#PREGUNTA DE CODIGO
notas = [8.5, 6.0, 9.75, 4.5, 7.0, 10.0, 5.25]
# Escriba su solución aquí

suma = 0
cantidad = 0
mas_alta = notas[0]
mas_baja = notas[0]
aprobados = 0

for n in notas:
    suma = suma + n
    cantidad = cantidad + 1
    if n > mas_alta:
        mas_alta = n
    if n < mas_baja:
        mas_baja = n
    if n >= 7:
        aprobados = aprobados + 1

promedio = round(suma / cantidad, 2)

print("Promedio:", f"{promedio:.2f}")
print("Nota más alta:", mas_alta)
print("Nota más baja:", mas_baja)

