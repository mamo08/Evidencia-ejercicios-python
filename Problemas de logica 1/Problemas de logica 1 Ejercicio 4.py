# Función para validar números positivos
def validar_numero(mensaje):
    while True:
        try:
            valor = float(input(mensaje))
            if valor > 0:
                return valor
            else:
                print("Error: Debe ingresar un número positivo mayor a cero")
        except ValueError:
            print("Error: Debe ingresar un número válido")

# Obtener base y altura con validación
base = validar_numero("Ingrese la base del triángulo: ")
altura = validar_numero("Ingrese la altura del triángulo: ")

# Calcular área
area = (base * altura) / 2

# Mostrar resultado formateado
print(f"\nEl área del triángulo es: {area:.2f}")