lista=[2,4,8,3,8,20,10,4]
print(lista[-1])
# Diana

for numeros in lista:
    print(numeros) # 2 - David Ortega
#Alex Minchala
for numeros in lista:
    print(numeros, end=" ")
    
#ROLANDO NAVARRO 
 
for numeros in lista:
    print(numeros, end=" ")

for numeros in lista:
    if numeros%2==0:
        print(numeros, "El numero s par")
    else:
            print(numeros, "El numero es impar")

#Diego Rojas
saldo = 200
if saldo >= 1000:
        print ("Categoria oro")
elif saldo >=100 :
        print ("Categoria plata")
else:
        print ("Categoria basica")

#Domenica Ayllon
monto=100

estado="con fondos" if monto>=100 else "sin fondos"
print(estado)

#Santiago Brito
edad = 24
activo = True
tiene_Deuda= False 

if edad >=18 and edad <=64 and activo==True and not tiene_Deuda:
     print ("Puede realizar un credito")
else:
     print ("No puede realizar un credito")

#Samuel Tobar
num = 1
while num <= 5:
      print("Vuelta numero ",num)
      num+=1
print("Fin de la ejecucion")

#Rene Dominguez
deposito = 0
meses = 0
while deposito < 400 :
    meses += 1
    deposito += 50
    
print("Se necesito ", meses, "meses para llegar a 400 dolares")

#Steven Ortiz 

monto = float(input("Ingrese el monto a depositar "))


while monto <=0:
    monto = float(input("Ingrese un monto mayor a cero"))

print ("El monto depositado es:", monto)

#Maria Bravo
 
    