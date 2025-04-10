# Validar rol de la persona
while True:
    rol = input("Ingrese su rol (ejecutivo/operario): ").strip().lower()
    if rol in ["ejecutivo", "operario"]:
        break
    else:
        print("Error: Rol no válido. Debe ser 'ejecutivo' o 'operario'")

# Validar edad solo para operarios
edad = None
if rol == "operario":
    while True:
        try:
            edad = int(input("Ingrese su edad: "))
            if edad > 0:
                break
            else:
                print("Error: La edad debe ser un número positivo")
        except ValueError:
            print("Error: Debe ingresar un número entero válido")

# Determinar requerimientos de seguridad
if rol == "ejecutivo":
    mensaje = "No requiere usar guantes ni gafas de protección"
else:
    mensaje = "Sí requiere usar guantes y gafas de protección" if edad > 60 else "No requiere usar guantes ni gafas de protección"

# Mostrar el resultado
print(mensaje)