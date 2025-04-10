# Solicitar nombre de la persona
nombre = input("Ingrese su nombre: ")

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

# Validar nivel SISBEN (1-3)
while True:
    try:
        sisben = int(input("Ingrese su nivel SISBEN (1-3): "))
        if 1 <= sisben <= 3:
            break
        else:
            print("Error: El SISBEN debe estar entre 1 y 3")
    except ValueError:
        print("Error: Debe ingresar un número entero válido")

# Determinar elegibilidad para el subsidio
if estrato <= 2 and sisben < 2:
    mensaje = f"{nombre}, usted tiene derecho a subsidio mensual en efectivo"
else:
    mensaje = f"{nombre}, usted no tiene derecho a subsidio mensual en efectivo"

# Mostrar resultado
print(mensaje)