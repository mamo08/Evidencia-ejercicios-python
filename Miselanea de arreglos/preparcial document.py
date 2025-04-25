#Ejercicio 1a (Contar mayores de edad)

edades = [20, 16, 19, 17, 20, 18, 22, 17]
mayores = 0
for i in edades:
    if i >= 18:
        mayores += 1
print(mayores)
#Ejercicio 1b (Calcular promedio)

datos = [20, 33, 67, 4, 60]
contador = 0
suma = 0
while contador < len(datos):
    suma += datos[contador]
    contador += 1
print(suma / len(datos))
#Ejercicio 2 (Función para Shirley)

def elementos_comunes_emparejados(arr1, arr2):
    # Crear diccionarios con conteos de cada elemento
    from collections import defaultdict
    
    count1 = defaultdict(int)
    count2 = defaultdict(int)
    
    for elem in arr1:
        count1[elem] += 1
    
    for elem in arr2:
        count2[elem] += 1
    
    # Encontrar elementos comunes y emparejarlos
    resultado = []
    for elem in set(arr1) & set(arr2):
        min_count = min(count1[elem], count2[elem])
        resultado.extend([elem * 2] * min_count)
    
    return sorted(resultado)

# Prueba con los datos de Shirley
arr1 = ["s", "w", "@", "3", "a", "p"]
arr2 = ["#", "p", "a", "z", "@"]
print(elementos_comunes_emparejados(arr1, arr2))  # ['@@', 'aa', 'pp']
#Ejercicio 3 (Función para Mariana)

def base_mas_comun_adn():
    # Validar entrada del usuario
    while True:
        cadenas = input("Ingrese 4 cadenas de ADN (7 caracteres cada una) separadas por comas: ").upper().split(',')
        cadenas = [cad.strip() for cad in cadenas]
        
        if len(cadenas) != 4:
            print("Debe ingresar exactamente 4 cadenas.")
            continue
            
        valido = True
        for cad in cadenas:
            if len(cad) != 7 or not all(c in 'ACTG' for c in cad):
                valido = False
                break
                
        if valido:
            break
        else:
            print("Todas las cadenas deben tener exactamente 7 caracteres (A, C, T, G).")
    
    # Contar bases
    contador = {'A': 0, 'C': 0, 'T': 0, 'G': 0}
    for cadena in cadenas:
        for base in cadena:
            contador[base] += 1
    
    # Encontrar base más común
    base_mas_comun = max(contador.items(), key=lambda x: x[1])
    print(f"La base más común es {base_mas_comun[0]} con {base_mas_comun[1]} apariciones.")

# Ejemplo de uso
base_mas_comun_adn()
#Ejercicio 4 (Función para Pedro)

def formar_palabra_orbi(arr):
    from collections import defaultdict
    
    # Convertir a minúsculas para comparación sin distinción de mayúsculas
    arr_lower = [c.lower() for c in arr]
    palabra = "orbi"
    
    # Verificar si se pueden formar todas las letras
    letras_faltantes = list(palabra)
    letras_disponibles = arr_lower.copy()
    resultado = []
    
    for letra in palabra:
        if letra in letras_disponibles:
            resultado.append(letra)
            letras_disponibles.remove(letra)
        else:
            print(f"No se puede formar la palabra '{palabra}'. Falta la letra '{letra}'.")
            return None
    
    # Ordenar según el orden de la palabra deseada
    orden_correcto = ['o', 'r', 'b', 'i']
    resultado_ordenado = []
    for letra in orden_correcto:
        if letra in resultado:
            resultado_ordenado.append(letra)
    
    print(f"Sí se puede formar la palabra '{palabra}'. Resultado: {resultado_ordenado}")
    return resultado_ordenado

# Prueba con los datos de Pedro
arreglo = ["b", "p", "s", "z", "o", "b", "a", "w", "r", "i"]
print(formar_palabra_orbi(arreglo))  # ['o', 'r', 'b', 'i']