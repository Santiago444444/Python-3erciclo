def codigo_pregunta_1():
    print("ab" * 3)

def codigo_pregunta_2():
    ciudad = "Paute y"
    print(ciudad[-1].upper())

def codigo_pregunta_3():
    print(int(9.99))

def codigo_pregunta_4():
    a = {1, 2, 3, 4}
    b = {3, 4, 5}
    print(len(a & b))

def codigo_pregunta_5():
    print(type(10.0))

def codigo_pregunta_6():
    for i in range(1, 10, 3):
        print(i, end=" ")
    print()

def codigo_pregunta_7():
    print([n ** 2 for n in [1, 2, 3, 4] if n % 2 == 0])

def codigo_pregunta_8():
    for i in range(3):
        for j in range(2):
            print("*", end="")
    print()

def codigo_pregunta_9():
    for i in range(3, 0, -1):
        print(i, end=" ")
    print()

def codigo_pregunta_10():
    saldo = 350
    if saldo >= 1000:
        print("Oro")
    elif saldo >= 100:
        print("Plata")
    else:
        print("Básica")

def codigo_pregunta_11():
    notas = [8.5, 6.0, 9.75, 4.5, 7.0, 10.0, 5.25]
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
    print("Aprobados:", aprobados)


ejecutando = True

while ejecutando:
    print("\n=== MENU PRINCIPAL ===")
    print("1. Ingrese el nombre")
    print("2. Menu de preguntas")
    print("3. Salir")
    
    opcion_principal = input("Seleccione una opción: ").strip()
    
    if opcion_principal == "1":
        nombre = input("Ingrese su nombre: ").strip()
        print("Bienvenido,", nombre)
        
    elif opcion_principal == "2":
        while True:
            print("\n--- MENU DE PREGUNTAS ---")
            print("1. Pregunta 1")
            print("2. Pregunta 2")
            print("3. Pregunta 3")
            print("4. Pregunta 4")
            print("5. Pregunta 5")
            print("6. Pregunta 6")
            print("7. Pregunta 7")
            print("8. Pregunta 8")
            print("9. Pregunta 9")
            print("10. Pregunta 10")
            print("11. Pregunta 11")
            print("12. Salir")
            print("13. Volver al menu principal")
            
            entrada = input("Seleccione una pregunta: ").strip()
            
            if not entrada.isdigit():
                print("Por favor, ingrese un número válido.")
                continue
                
            op = int(entrada)
            
            if op == 1:
                print("\n¿Qué imprime el siguiente código?")
                print('print("ab" * 3)')
                print("a. ab ab ab | b. Error | c. ababab | d. ab3")
                print("Ejecución del código:")
                codigo_pregunta_1()
                print("The correct answer is: ababab")
                input("\nPresione Enter para volver al menú...")
                
            elif op == 2:
                print("\n¿Qué imprime el siguiente código?")
                print('ciudad = "Paute y"\nprint(ciudad[-1].upper())')
                print("a. A | b. Y | c. Error | d. y")
                print("Ejecución del código:")
                codigo_pregunta_2()
                print("The correct answer is: Y")
                input("\nPresione Enter para volver al menú...")
                
            elif op == 3:
                print("\n¿Qué imprime el siguiente código?")
                print("print(int(9.99))")
                print("a. 10 | b. 9 | c. Error | d. 9.99")
                print("Ejecución del código:")
                codigo_pregunta_3()
                print("The correct answer is: 9")
                input("\nPresione Enter para volver al menú...")
                
            elif op == 4:
                print("\n¿Qué imprime el siguiente código?")
                print("a = {1, 2, 3, 4}\nb = {3, 4, 5}\nprint(len(a & b))")
                print("a. 5 | b. 2 | c. 4 | d. 3")
                print("Ejecución del código:")
                codigo_pregunta_4()
                print("The correct answer is: 2")
                input("\nPresione Enter para volver al menú...")
                
            elif op == 5:
                print("\n¿Qué imprime el siguiente código?")
                print("print(type(10.0))")
                print("a. <class 'int'> | b. <class 'str'> | c. <class 'float'> | d. <class 'double'>")
                print("Ejecución del código:")
                codigo_pregunta_5()
                print("The correct answer is: <class 'float'>")
                input("\nPresione Enter para volver al menú...")
                
            elif op == 6:
                print("\n¿Qué imprime el siguiente código?")
                print('for i in range(1, 10, 3):\n    print(i, end=" ")')
                print("a. 0 3 6 9 | b. 1 3 5 7 9 | c. 1 4 7 10 | d. 1 4 7")
                print("Ejecución del código:")
                codigo_pregunta_6()
                print("The correct answer is: 1 4 7")
                input("\nPresione Enter para volver al menú...")
                
            elif op == 7:
                print("\n¿Qué imprime el siguiente código?")
                print("print([n ** 2 for n in [1, 2, 3, 4] if n % 2 == 0])")
                print("a. [2, 4] | b. [1, 4, 9, 16] | c. [4, 16] | d. [1, 9]")
                print("Ejecución del código:")
                codigo_pregunta_7()
                print("The correct answer is: [4, 16]")
                input("\nPresione Enter para volver al menú...")
                
            elif op == 8:
                print('\n¿Cuántas veces se imprime "*" en el siguiente código?')
                print('for i in range(3):\n    for j in range(2):\n        print("*", end="")')
                print("a. 9 | b. 5 | c. 3 | d. 6")
                print("Ejecución del código:")
                codigo_pregunta_8()
                print("The correct answer is: 6")
                input("\nPresione Enter para volver al menú...")
                
            elif op == 9:
                print("\n¿Qué imprime el siguiente código?")
                print('for i in range(3, 0, -1):\n    print(i, end=" ")')
                print("a. Nada | b. 1 2 3 | c. 3 2 1 0 | d. 3 2 1")
                print("Ejecución del código:")
                codigo_pregunta_9()
                print("The correct answer is: 3 2 1")
                input("\nPresione Enter para volver al menú...")
                
            elif op == 10:
                print("\n¿Qué imprime el siguiente código?")
                print('saldo = 350\nif saldo >= 1000:\n    print("Oro")\nelif saldo >= 100:\n    print("Plata")\nelse:\n    print("Básica")')
                print("a. Básica | b. Plata Básica | c. Plata | d. Oro")
                print("Ejecución del código:")
                codigo_pregunta_10()
                print("The correct answer is: Plata")
                input("\nPresione Enter para volver al menú...")
                
            elif op == 11:
                print("\nEjercicio 3. Estadística de notas")
                print("Dada la lista notas = [8.5, 6.0, 9.75, 4.5, 7.0, 10.0, 5.25], calcule con un ciclo:")
                print("el promedio con 2 decimales, la nota más alta, la más baja y cuántos estudiantes aprobaron (nota >= 7).")
                print("Ejecución del código:")
                codigo_pregunta_11()
                input("\nPresione Enter para volver al menú...")
                
            elif op == 12:
                print("Saliendo del programa...")
                ejecutando = False
                break
                
            elif op == 13:
                break
                
            else:
                print("Opción no válida.")
                
    elif opcion_principal == "3":
        print("Saliendo del programa...")
        ejecutando = False
        
    else:
        print("Opción no válida.")