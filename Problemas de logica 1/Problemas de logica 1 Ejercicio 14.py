import random

# Validar entrada del valor mínimo
while True:
    try:
        min_valor = int(input("Ingrese el valor mínimo del rango: "))
        break
    except ValueError:
        print("Error: Debe ingresar un número entero válido")

# Validar entrada del valor máximo
while True:
    try:
        max_valor = int(input("Ingrese el valor máximo del rango: "))
        if max_valor >= min_valor:
            break
        else:
            print(f"Error: El máximo debe ser mayor o igual al mínimo ({min_valor})")
    except ValueError:
        print("Error: Debe ingresar un número entero válido")

# Generar y mostrar número aleatorio
numero_aleatorio = random.randint(min_valor, max_valor)
print(f"\nNúmero aleatorio entre {min_valor} y {max_valor}: {numero_aleatorio}")