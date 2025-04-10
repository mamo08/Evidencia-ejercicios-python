# Validar edad actual
while True:
    try:
        edad_actual = int(input("Ingrese su edad actual: "))
        if edad_actual > 0:
            break
        else:
            print("Error: La edad debe ser un número positivo mayor a 0")
    except ValueError:
        print("Error: Debe ingresar un número entero válido")

# Validar años futuros
while True:
    try:
        años_futuros = int(input("Ingrese cuántos años quiere proyectar: "))
        if años_futuros >= 0:
            break
        else:
            print("Error: Debe ingresar un número entero no negativo")
    except ValueError:
        print("Error: Debe ingresar un número entero válido")

# Calcular edad futura
edad_futura = edad_actual + años_futuros

# Mostrar resultado
print(f"\nEn {años_futuros} años, usted tendrá {edad_futura} años")