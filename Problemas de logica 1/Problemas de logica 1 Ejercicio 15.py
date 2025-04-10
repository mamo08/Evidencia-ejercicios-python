def formato_tiempo(cantidad, unidad):
    return f"{cantidad} {unidad}" if cantidad == 1 else f"{cantidad} {unidad}s"

# Validar entrada de segundos
while True:
    try:
        segundos = int(input("Ingrese la cantidad de segundos: "))
        if segundos >= 0:
            break
        else:
            print("Error: La cantidad no puede ser negativa")
    except ValueError:
        print("Error: Debe ingresar un número entero válido")

# Calcular horas, minutos y segundos
horas = segundos // 3600
resto = segundos % 3600
minutos = resto // 60
segundos_restantes = resto % 60

# Formatear y mostrar resultados
partes = []
if horas > 0:
    partes.append(formato_tiempo(horas, "hora"))
if minutos > 0:
    partes.append(formato_tiempo(minutos, "minuto"))
if segundos_restantes > 0 or segundos == 0:
    partes.append(formato_tiempo(segundos_restantes, "segundo"))

print("Tiempo equivalente: " + ", ".join(partes))