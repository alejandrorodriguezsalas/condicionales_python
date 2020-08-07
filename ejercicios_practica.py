#!/usr/bin/env python
'''
Condicionales [Python]
Ejercicios de práctica
---------------------------
Autor: Inove Coding School
Version: 1.2

Descripcion:
Programa creado para que practiquen los conocimietos adquiridos durante la semana
'''

__author__ = "Inove Coding School"
__email__ = "alumnos@inove.com.ar"
__version__ = "1.2"


def ej1():
    print('Ej1: Ejercicios de práctica con números\n')

    '''
    Realice un programa que solicite por consola 2 números
    Calcule la diferencia entre ellos e informe por pantalla
    si el resultado es positivo, negativo o cero.
    '''
    print("Ingrese dos números a restar entre ellos:")
    num_1 = float(input("Ingrese el primer número\n"))
    num_2 = float(input("Ingrese el segundo número\n"))
    resta = num_1 - num_2

    print("Verificación del signo de la resta:")

    if resta > 0:
        print("{} es positivo\f".format(resta))
    elif resta < 0:
        print("{} es negativo\f".format(resta))
    else:
        print("La resta es cero\f")



def ej2():
    print('Ej2: Ejercicios de práctica con números')
  
    '''
    Realice un programa que solicite el ingreso de tres números
    enteros, y luego en cada caso informe si el número es par
    o impar.
    Para cada caso imprimir el resultado en pantalla.
    '''

    print("Ingrese 3 numeros enteros:")
    num_1 = int(input())
    num_2 = int(input())
    num_3 = int(input())

    print("\nVericación de paridad de los numeros:")
    if (num_1 % 2) == 0:
       print("El numero {} es par".format(num_1))
    else:
        print("El numero {} es impar".format(num_1))
    
    if (num_2 % 2) == 0:
       print("El numero {} es par".format(num_2))
    else:
        print("El numero {} es impar".format(num_2))
    
    if (num_3 % 2) == 0:
       print("El numero {} es par\f".format(num_3))
    else:
        print("El numero {} es impar\f".format(num_3))
        


def ej3():
    print('Ej3: Ejercicios de práctica con números')

    '''
    Realice una calculadora, se ingresará por línea de comando dos números
    Luego se ingresará como tercera entrada al programa el símbolo de la operación
    que se desea ejecutar
    - Suma (+)
    - Resta (-)
    - Multiplicación (*)
    - División (/)
    - Exponente/Potencia (**)

    Se debe efectuar el cálculo correcto según la operación ingresada por consola
    Imprimir en pantalla la operación realizada y el resultado
    '''

    print("Ingrese dos números:")
    num_1 = float(input())
    num_2 = float(input())

    print('''Ingrese el simbolo de la operación que desee realizar:
    - Suma (+)
    - Resta (-)
    - Multiplicación (*)
    - División (/)
    - Exponente/Potencia (**)''')
    opcion = str(input())

    if opcion == '+':
        print("{} + {} = {}".format(num_1,num_2,num_1+num_2))
    elif opcion == '-':
        print("{} - {} = {}".format(num_1,num_2,num_1-num_2))
    elif opcion == '*':
        print("{} x {} = {}".format(num_1,num_2,num_1*num_2))
    elif opcion == '/':
        print("{} : {} = {}".format(num_1,num_2,num_1/num_2))
    elif opcion == '**':
        print("{} ^ {} = {}".format(num_1,num_2,num_1**num_2))
    


def ej4():
    print('Ej4: Ejercicios de práctica con cadenas')

    '''
    Realice un programa que solicite por consola 3 palabras cualesquiera
    Luego el programa debe consultar al usuario como quiere ordenar las palabras
    1 - Ordenar por orden alfabético (usando el operador ">")
    2 - Ordenar por cantidad de letras (longitud de la palabra)

    Si se ingresa "1" por consola se deben ordenar las 3 palabras por orden alfabético
    e imprimir en pantalla de la mayor a la menor

    Si se ingresa "2" por consola se deben ordenar las 3 palabras por cantidad de letras
    e imprimir en pantalla de la mayor a la menor
    '''
    print("Que palabras quiere trabajar:")
    pal_1 = str(input("Ingrese primera palabra:  "))
    pal_2 = str(input("Ingrese segunda palabra:  "))
    pal_3 = str(input("Ingrese tercera palabra:  "))
    print('''\nSeleccione el número de la tarea que desea realizar:
    1 - Ordenar por orden alfabético
    2 - Ordenar por cantidad de letras''')

    opcion = str(input())

    if opcion == '1':
        print("\nOrden alfabetico:")
        if pal_1 < pal_2 and pal_1 < pal_3:
            if pal_2 < pal_3:
                print ("{} _ {} _ {}".format(pal_1,pal_2,pal_3))
            else:
                print("{} _ {} _ {}".format(pal_1,pal_3,pal_2))
        elif pal_2 < pal_1 and pal_2 < pal_3:
            if pal_1 < pal_3:
                print("{} _ {} _ {}".format(pal_2,pal_1,pal_3))
            else:
                print("{} _ {} _ {}".format(pal_2,pal_3,pal_1))
        elif pal_1 < pal_2:
            print("{} _ {} _ {}".format(pal_3,pal_1,pal_2))
        else:
            print("{} _ {} _ {}".format(pal_3,pal_2,pal_1))
    elif opcion == '2':
        print("\nOrden de mayor a menor por cant de letras:")
        if len(pal_1) > len(pal_2) and len(pal_1) > len(pal_3):
            if len(pal_2) > len(pal_3):
                print("{}, {}, {}".format(pal_1,pal_2,pal_3))
            else:
                print("{}, {}, {}".format/pal_1,pal_3,pal_2)
        elif len(pal_2) > len(pal_1) and len(pal_2) > len(pal_3):
            if len(pal_1) > len(pal_3):
                print("{}, {}, {}".format(pal_2,pal_1,pal_3))
            else:
                print("{}, {}, {}".format(pal_2,pal_3,pal_1))
        elif len(pal_1) > len(pal_2):
            print("{}, {}, {}".format(pal_3,pal_1,pal_2))
        else:
            print("{}, {}, {}".format(pal_3,pal_2,pal_1))
            


def ej5():
    print('EJ5: Ejercicios de práctica con números')

    '''
    Realice un programa que solicite ingresar tres valores de temperatura
    De las temperaturas ingresadas por consola determinar:
    1 - ¿Cuáles de ellas es la máxima temperatura ingresada?
    2 - ¿Cuáles de ellas es la mínima temperatura ingresada?
    3 - ¿Cuál es el promedio de las temperaturas ingresadas?

    En cada caso imprimir en pantalla el resultado
    '''
    print("Ingrese 3 valores de temperatura (ºC)")
    temp_1 = float(input("Temperatura 1:  "))
    temp_2 = float(input("Temperatura 2:  "))
    temp_3 = float(input("Temperatura 3:  "))

    if temp_1 > temp_2 and temp_1 > temp_3:
        print("\nTemperatura máx: {} ºC".format(temp_1))
        if temp_2 > temp_3:
            print("Temperatura min: {} ºC".format(temp_3))
        else:
            print("Temperatura min: {} ºC".format(temp_2))
    elif temp_2 > temp_3 and temp_2 > temp_1:
        print("\nTemperatura máx: {} ºC".format(temp_2))
        if temp_1 > temp_3:
            print("Temperatura min: {} ºC".format(temp_3))
        else:
            print("Temperatura min: {} ºC".format(temp_1))
    elif temp_1 > temp_2:
        print("\nTemperatura máx: {} ºC".format(temp_3))
        print("Temperatura min: {} ºC".format(temp_2))
    else:
        print("\nTemperatura máx: {} ºC".format(temp_3))
        print("Temperatura min: {} ºC".format(temp_1))

    prom = (temp_1+temp_2+temp_3) / 3

    print("El promedio de la temperatura es {} ºC".format(prom))
    


if __name__ == '__main__':
    print("\n         Ejercicios de práctica\n")
    ej1()
    ej2()
    ej3()
    ej4()
    ej5()
