# 1. Dado el siguiente arreglo [200, -100, 45, 78, 32]
# Imprimir elementos de índice 2 y 4:
arr1 = [200, -100, 45, 78, 32]
print(arr1[2], arr1[4]) # 45 32

# 2. Dado el siguiente arreglo ["ab", "cd", "ef", "gh"]
# Imprimir elementos "cd" y "gh":
arr2 = ["ab", "cd", "ef", "gh"]
print(arr2[1], arr2[3])  # cd gh

# 3. Dado el siguiente arreglo [10, true, "k200", 20.7]
# Recorrer arreglo con for:
arr3 = [10, True, "k200", 20.7]
for element in arr3:
    print(element)
    
# 4. Dado el siguiente arreglo [17, 4, 64, 79, 109, 112]
# Imprimir números impares:
arr4 = [17, 4, 64, 79, 109, 112]
for num in arr4:
    if num % 2 != 0:
        print(num)
        
# 5. Dado el siguiente arreglo [true, true, false,true, false]
# Modificar elementos del arreglo booleano:
arr5 = [True, True, False, True, False]
arr5[2] = True
arr5[3] = False
print(arr5)

# 6.Dado el siguiente arreglo ["wc", "jp", "zx", "qr"]
# Modificar elementos del arreglo de strings:
arr6 = ["wc", "jp", "zx", "qr"]
arr6[1] = True
arr6[3] = 30
print(arr6)

# 7. Cree una función que reciba como argumento el siguiente arreglo [2, 5, 7, 9] y lo recorra
# Función para recorrer arreglo:
def print_array(arr):
    for element in arr:
        print(element)

print_array([2, 5, 7, 9])

# 8. Cree una función que reciba un arreglo de n elementos y retorne el número de elementos del arreglo.
# Función que retorna número de elementos:
def array_length(arr):
    return len(arr)

# Use indexOf para mostrar los índices de los elementos 44, 89, 70 del arreglo [30, 44, 54, 89, 100]
# Encontrar índices de elementos (Python usa index() en lugar de indexOf):
arr9 = [30, 44, 54, 89, 100]
try:
    print(arr9.index(44))  # 1
    print(arr9.index(89))  # 3
    print(arr9.index(70))  # ValueError (no existe)
except ValueError:
    print(-1)  # Para el caso de 70 que no existe
    
# Ejercicios adicionales
# Número de elementos:
# 1.Imprima el número de elementos de los siguientes arreglos
# [1,2,3,4,5,6,7,8,9,10] b) [] c) ["a", true, -1] d) [2, 4, 5, 7, 1, 34, 89, 0]

print(len([1,2,3,4,5,6,7,8,9,10]))  # 10
print(len([]))  # 0
print(len(["a", True, -1]))  # 3
print(len([2, 4, 5, 7, 1, 34, 89, 0]))  # 8

# 2.Operaciones append (equivalente a push):

arr2a = [1,2,3,4,5,6,7,8,9,10]
arr2a.append(345)
print(arr2a)  # [1,2,3,4,5,6,7,8,9,10,345]

arr2a.append(True)
print(arr2a)  # [..., True]

arr2a.append("ADSO")
print(arr2a)  # [..., "ADSO"]

arr2a.extend([455, 78, False])  # equivalente a push múltiples elementos
print(arr2a)  # [..., 455, 78, False]

arr2a.extend(["ABcd", True, 21])
print(arr2a)  # [..., "ABcd", True, 21]

# 3.Eliminar elementos:

# a)
arr3a = [1, 2, False]
del arr3a[2]
print(arr3a)  # [1, 2]

# b)
arr3b = [99, False, 17, 45, 7, "abc", 78]
del arr3b[6]
print(arr3b)  # [99, False, 17, 45, 7, "abc"]

# c)
arr3c = [-1, -55, -89, 30, 1000]
del arr3c[1]
print(arr3c)  # [-1, -89, 30, 1000]

# d)
arr3d = ["zxc", 767, 1298, True, False, [3], 1]
del arr3d[1:5]  # Elimina desde índice 1 hasta 4 (no incluye 5)
print(arr3d)  # ["zxc", [3], 1]

# e)
arr3e = [34, ["q"], 67, 1, 99, 0.5]
del arr3e[3:5]
print(arr3e)  # [34, ["q"], 67, 0.5]

# 6.Recorrer arreglo con for:

arr6 = ["x", "y", "z", 0, 1, 2, 3]
for element in arr6:
    print(element)

# 7.Recorrer arreglo e imprimir elementos +1:

arr7 = [1, 17, 8, 9, 3]
for num in arr7:
    print(num + 1)

# 8.Función que retorna longitud:

def get_array_length(arr):
    return len(arr)

# 9.Función para buscar letra:

def find_letter(letter):
    letters = ["a", "b", "c", "d", "e", "f", "g"]
    return letter.lower() in letters

# Ejemplo de uso:
print(find_letter("C"))  # True
print(find_letter("X"))  # False