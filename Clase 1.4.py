#DECLARACION DE FUNCIONES
def saludar ():
    print ("Hola Santiago")
 
saludar ()


#FUNCION CON PARAMETROS

#def calcular_edad(anio_nacimiento, anio_actual):
#    print ("La edad actual es: ", anio_actual-anio_nacimiento)

#a = int (input("Ingrese su anio de nacimiento: "))
#b = int (input("Ingrese el anio actual: "))

#calcular_edad(a,b)

#FUNCIONES CON RETORNO 
def calcular_iva (precio,iva=0.15):
    return precio*iva

resultado = calcular_iva (100)

print ("El valor del iva es, ", resultado)


resultado = calcular_iva (100,0.14)
print ("El iva es: ", resultado)

#FUNCIONES CON LISTAS
def calcular_par(numeros):
    for i in numeros:
        if i % 2 ==0:
            print (i, "Es par")
        else:
            print (i, "Es impar")

lista_numeros = range (0,1000,2)
calcular_par (lista_numeros)

lista_numeros = range (5,0,-1)
for i in lista_numeros:
    print (i, end=" ")

#FUNCIONES CON TUPLAS

def suma_numeros (*a):
    return sum (a)

print (suma_numeros(1,2,3))

#FUNCIONES CON DICCIONARIOS
def estudiantes(**lista_estudiantes):
    total_edad = 0

    for nombre,edad in lista_estudiantes.items():
        print ("El estudiante, ", nombre, "tiene ", edad, "anios")
        total_edad += edad

    print ("La suma total de las edades es: ", total_edad )

estudiantes (Santiago=20, Gerard=21, Jose=19, Fricson=18, Pablo=23, Alex=25, Andres=27)
