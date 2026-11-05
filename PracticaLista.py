notas = [10,8,9,5]
print(notas)
print (notas[1])
notas.append(20)
print (max(notas))
notas.insert(1,10)
print(len(notas))
print (notas[-1])
print (sum(notas))
print (notas[0])
print (notas[-2:])
print (min(notas))
notas.remove(9) 
notas = sorted(notas) 
print(notas)
print (notas[2:])
print (notas[:2])
print (notas[:-1])


#TUPLAS
meses=("1","2","3","4","5","6","7","8","9","10","11","12")
print (meses)
print (meses[0])
#(meses[3])=45

#DICCIONARIOS
estudiante={"cedula": "0107434227", 
           "nombre": "Santiago", 
           "correo": "arielbrito824@gmail.com",
           "celular": "0960785864", 
           "notas": [10,9,5,4]
           }
print(estudiante.get("nombre"))
print(estudiante.keys())


#CONJUNTOS 
conjunto_a={1,1,5,4,6,8}
conjunto_b={1,9,6,5,4}

print (conjunto_a & conjunto_b)
print (conjunto_a | conjunto_b)


#CASO PRACTICO 1

socio = {
    "cedula": "0102030405",   
    "nombre": "  ana lucía pérez ",      
    "edad": 34,           
    "activo": True, 
    "garante": None, 
    "cuentas": [                          
        {"numero": "AH-001", "tipo": "ahorros", "saldo": 1520.75},
        {"numero": "PF-010", "tipo": "plazo fijo", "saldo": 5000.0},
        {"numero": "AH-002", "tipo": "ahorros", "saldo": 80.5},
    ],
}
