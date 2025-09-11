"""/*
 * EJERCICIO:
 * - Crea ejemplos utilizando todos los tipos de operadores de tu lenguaje:
 *   Aritméticos, lógicos, de comparación, asignación, identidad, pertenencia, bits...
 *   (Ten en cuenta que cada lenguaje puede poseer unos diferentes)
 * - Utilizando las operaciones con operadores que tú quieras, crea ejemplos
 *   que representen todos los tipos de estructuras de control que existan
 *   en tu lenguaje:
 *   Condicionales, iterativas, excepciones...
 * - Debes hacer print por consola del resultado de todos los ejemplos.
 */"""

# Operadores aritméticos
print(f"Suma 10 + 3 = {10 + 3}")
print(f"Módulo: 10 % 3 = {10 % 3}")
print(f"Exponente: 10 ** 3 = {10 ** 3}")
print(f"División entera: 10 // 3 = {10 // 3}")

# Operadores de comparación
print(f"Igualdad: 10 == 3 es {10 == 3}")
print(f"Desigualdad: 10 != 3 es {10 != 3}")

#Operadores lógicos
print(f"AND &&: 10 + 3 == 13 and 5 -1 == 4: {10 + 3 == 13 and 5 -1 == 4}")
print(f"OR ||: 10 + 3 == 13 or 5 -1 == 4: {10 + 3 == 13 or 7 - 1 == 4}")
print(f"NOT !: not 10 + 3 == 14 es {not 10 + 3 == 14}")

#Operadores de asinación
my_number = 1
my_number += 1
my_number -= 1 
"""
*=
/=
%=
**=
//=
"""
print(f"{my_number}")

#Operador de la identidad (posición de memoria)
my_number = 1.0
my_new_number = 1.0
print(f"my_number is my new_number es {my_number is my_new_number}")
print(f"{my_new_number}, {my_number}")
# 'is' o 'is not'

#Operadores de pertenencia

print(f"a" in "Ana")

#Operadores de bit
a = 10 #1010
b = 3 #0011

print(f"AND: 10 & 3 = {10 & 3}")
#OR
#EXOR
#NOT
#Desplazamiento a la derecha: 
print(f"10 >> 2 {10 << 2}")

"""
Estructuras de control
"""

try:
    print(1/10)
except:
    print("Se ha producido un error")
finally: #Siempre se ejecuta independientemente de si ha funcionado o no
    print("Ha finalizado el manejo de excepciones")

"""
 * DIFICULTAD EXTRA (opcional):
 * Crea un programa que imprima por consola todos los números comprendidos
 * entre 10 y 55 (incluidos), pares, y que no son ni el 16 ni múltiplos de 3.
 *
 * Seguro que al revisar detenidamente las posibilidades has descubierto algo nuevo.
 """

for number in range (10, 56):
    if number % 2 == 0 and number !=16 and number % 3 != 0:
        print(number)


