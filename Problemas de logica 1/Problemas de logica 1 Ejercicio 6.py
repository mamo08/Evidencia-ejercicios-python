# Validar entrada del lado del cubo
while True:
    try:
        lado = float(input("Ingrese la longitud del lado del cubo: "))
        if lado > 0:
            break
        else:
            print("Error: El lado debe ser un número positivo")
    except ValueError:
        print("Error: Debe ingresar un número válido")

# Calcular el volumen (lado al cubo)
volumen = lado ** 3

# Mostrar resultado formateado
print(f"\nEl volumen del cubo con lado {lado} es: {volumen:.2f}")