# Validar entrada del precio
while True:
    try:
        precio = float(input("Ingrese el precio del producto: "))
        if precio >= 0:
            break
        else:
            print("Error: El precio no puede ser negativo")
    except ValueError:
        print("Error: Debe ingresar un valor numérico válido")

# Calcular precio con IVA (19%)
precio_final = precio * 1.19

# Mostrar resultado formateado
print(f"\nPrecio sin IVA: ${precio:,.2f}")
print(f"Precio final con IVA (19%): ${precio_final:,.2f}")