# Solicitar nombre del empleado
nombre = input("Nombre del empleado: ")

# Validar estrato socio-económico (1-6)
while True:
    try:
        estrato = int(input("Ingrese su estrato socio-económico (1-6): "))
        if 1 <= estrato <= 6:
            break
        else:
            print("Error: El estrato debe estar entre 1 y 6")
    except ValueError:
        print("Error: Debe ingresar un número entero válido")

# Validar años de antigüedad
while True:
    try:
        antiguedad = int(input("Ingrese su antigüedad en años en la entidad: "))
        break
    except ValueError:
        print("Error: Debe ingresar un número entero válido")

# Determinar elegibilidad para el subsidio
if estrato < 4 and antiguedad >= 8:
    mensaje = f"{nombre}, usted tiene derecho a subsidio de vivienda"
else:
    mensaje = f"{nombre}, usted no tiene derecho a subsidio de vivienda"

# Mostrar resultado
print(mensaje)
