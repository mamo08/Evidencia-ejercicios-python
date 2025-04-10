import math

def validar_radio():
    while True:
        try:
            radio = float(input("Ingrese el radio del círculo: "))
            if radio > 0:
                return radio
            else:
                print("Error: El radio debe ser un número positivo")
        except ValueError:
            print("Error: Debe ingresar un número válido")

# Obtener radio validado
radio = validar_radio()

# Calcular área y perímetro
area = math.pi * (radio ** 2)
perimetro = 2 * math.pi * radio

# Mostrar resultados formateados
print(f"\nResultados para radio {radio}:")
print(f"Área del círculo: {area:.2f}")
print(f"Perímetro (circunferencia): {perimetro:.2f}")