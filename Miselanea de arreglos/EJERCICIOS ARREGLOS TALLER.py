# Ejercicio 1
# Dado el arreglo [1,2,3,4,5,6]:

arr = [1, 2, 3, 4, 5, 6]

# a) Iterar con while
print("a) Iterar con while:")
i = 0
while i < len(arr):
    print(arr[i])
    i += 1

# b) Iterar con for
print("\nb) Iterar con for:")
for num in arr:
    print(num)

# c) Copia incrementada en 1
print("\nc) Copia incrementada:")
arr_copia = []
for num in arr:
    arr_copia.append(num + 1)
print(arr_copia)

# d) Calcular promedio
print("\nd) Promedio:")
promedio = sum(arr) / len(arr)
print(promedio)

# Ejercicio 2
# Dado el arreglo de cadenas de ADN [“AATGAAC”, “GTTTTTC”, “GGTAAA”, “CCCCATGGG”]
#cree una función que reciba como argumento tal arreglo y muestre las cadenas de una sola base
#(cadenas formadas solo de A, o solo de T, o solo de C o solo de G) que se pueden formar entre todos los
#elementos del arreglo.

def cadenas_base_unica(adn):
    bases = ['A', 'T', 'C', 'G']
    for cadena in adn:
        for base in bases:
            if all(c == base for c in cadena):
                print(cadena)

# adn = ["AATGAAC", "GTTTTTC", "GGTAAA", "CCCCATGGG"]
# cadenas_base_unica(adn)

# Ejercicio 3
# Cree una función que reciba un arreglo de números y retorne el número menor entre todos los
#elementos del arreglo.

def numero_menor(arr):
    return min(arr)

# Ejemplo de uso:
print(numero_menor([5, 3, 8, 1, 9]))

# Ejercicio 4
# Cree una función que reciba un arreglo de números naturales y muestre todos los números primos en
# él.

def es_primo(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def mostrar_primos(arr):
# primos = [num for num in arr if es_primo(num)]
    print("Números primos:", primos)

# Ejemplo de uso:
#mostrar_primos([2, 3, 4, 5, 6, 7, 8, 9, 10, 11])

# Ejercicio 5
def usuarios_mayores():
    n = int(input("¿Cuántos usuarios va a ingresar? "))
    mayores = []
    
    for i in range(n):
        nombre = input(f"Nombre del usuario {i+1}: ")
        edad = int(input(f"Edad del usuario {i+1}: "))
        if edad >= 18:
            mayores.append(nombre)
    
    print("\nUsuarios mayores de edad:", mayores)
    print("Total de mayores de edad:", len(mayores))
    return mayores

usuarios_mayores()

# Ejercicio 6

valle = ["Cali", "Tulua", "Cartago", "Salento"]
quindio = ["Cordoba", "Armenia", "Palmira", "Circasia"]

# Ciudades del Valle del Cauca: Cali, Tulua, Cartago
# Ciudades del Quindío: Armenia, Circasia

valle_correcto = []
quindio_correcto = []

for ciudad in valle + quindio:
    if ciudad in ["Cali", "Tulua", "Cartago"]:
        valle_correcto.append(ciudad)
    elif ciudad in ["Armenia", "Circasia", "Salento"]:
        quindio_correcto.append(ciudad)

print("Valle del Cauca:", valle_correcto)
print("Quindío:", quindio_correcto)

# Ejercicio 7

arreglo1 = ["Pera", "Cebolla", "Limón", "Pimentón"]
arreglo2 = ["Manzana", "Banano", "Lechuga", "Perejíl"]

frutas = []
verduras = []

for item in arreglo1 + arreglo2:
    if item in ["Pera", "Manzana", "Banano", "Limón"]:
        frutas.append(item)
    else:
        verduras.append(item)

print("Frutas:", frutas)
print("Verduras:", verduras)

# Ejercicio 8
def numero_mayor():
    entrada = input("Ingrese números separados por comas: ")
    arr = [int(x) for x in entrada.split(',')]
    return max(arr)

print("El número mayor es:", numero_mayor())

# Ejercicio 9

def comparar_promedios():
    entrada1 = input("Ingrese primer arreglo (números separados por comas): ")
    arr1 = [int(x) for x in entrada1.split(',')]
    
    entrada2 = input("Ingrese segundo arreglo (números separados por comas): ")
    arr2 = [int(x) for x in entrada2.split(',')]
    
    prom1 = sum(arr1) / len(arr1)
    prom2 = sum(arr2) / len(arr2)
    
    if prom1 > prom2:
        print("El primer arreglo tiene mayor promedio")
    elif prom2 > prom1:
        print("El segundo arreglo tiene mayor promedio")
    else:
        print("Ambos arreglos tienen el mismo promedio")

comparar_promedios()

# Ejercicio 10
def contar_letra_c():
    entrada = input("Ingrese nombres separados por comas: ")
    nombres = [nombre.strip() for nombre in entrada.split(',')]
    
    contador = 0
    encontrado = False
    
    for nombre in nombres:
        contador += nombre.lower().count('c')
    
    if contador > 0:
        print(f"La letra 'c' aparece {contador} veces")
    else:
        print("No se encontró la letra 'c'")

contar_letra_c()

# Ejercicio 11
def contar_impares():
    entrada = input("Ingrese números enteros positivos separados por comas: ")
    numeros = [int(x) for x in entrada.split(',') if int(x) > 0]
    impares = [num for num in numeros if num % 2 != 0]
    print(f"El arreglo tiene {len(impares)} números impares")

contar_impares()

# Ejercicio 12
def cadena_con_mas_t():
    entrada = input("Ingrese cadenas de ADN separadas por comas (solo A, C, T, G): ")
    cadenas = [cad.strip().upper() for cad in entrada.split(',')]
    
    max_t = 0
    cadena_max = ""
    
    for cadena in cadenas:
        conteo_t = cadena.count('T')
        if conteo_t > max_t:
            max_t = conteo_t
            cadena_max = cadena
    
    if max_t > 0:
        print(f"La cadena con más Timina (T) es: {cadena_max} con {max_t} T's")
    else:
        print("Ninguna cadena contiene Timina (T)")

cadena_con_mas_t()

# Ejercicio 13 (Juego del Ahorcado)
import random

def ahorcado():
    palabras = ["PYTHON", "PROGRAMACION", "AHORCADO", "COMPUTADORA", "ALGORITMO"]
    palabra = random.choice(palabras)
    adivinadas = ['_'] * len(palabra)
    intentos = 6
    letras_usadas = []
    
    print("¡Bienvenido al juego del Ahorcado!")
    
    while intentos > 0 and '_' in adivinadas:
        print("\nPalabra:", ' '.join(adivinadas))
        print("Intentos restantes:", intentos)
        print("Letras usadas:", ', '.join(letras_usadas))
        
        letra = input("Ingrese una letra: ").upper()
        
        if letra in letras_usadas:
            print("Ya usaste esa letra. Intenta con otra.")
            continue
            
        letras_usadas.append(letra)
        
        if letra in palabra:
            for i in range(len(palabra)):
                if palabra[i] == letra:
                    adivinadas[i] = letra
            print("¡Correcto!")
        else:
            intentos -= 1
            print("Letra incorrecta.")
    
    if '_' not in adivinadas:
        print(f"\n¡Felicidades! Ganaste. La palabra era: {palabra}")
    else:
        print(f"\n¡Perdiste! La palabra era: {palabra}")

ahorcado()

# Ejercicio 14
def ordenar_numeros():
    entrada = input("Ingrese números enteros no repetidos separados por comas: ")
    numeros = list(set([int(x) for x in entrada.split(',')]))  # Elimina duplicados
    numeros_ordenados = sorted(numeros)
    print("Arreglo ordenado:", numeros_ordenados)
    return numeros_ordenados

ordenar_numeros()

# Ejercicio 15
def ordenar_letras():
    entrada = input("Ingrese letras no repetidas separadas por comas: ")
    letras = list(set([letra.strip().upper() for letra in entrada.split(',') if letra.strip().isalpha()]))
    letras_ordenadas = sorted(letras)
    print("Letras ordenadas:", letras_ordenadas)
    return letras_ordenadas

ordenar_letras()