import cmath

def resolver_ecuacion_cuadratica():
    print("Resolución de ecuación cuadrática ax² + bx + c = 0")
    
    # Validar coeficiente a (no puede ser cero)
    while True:
        try:
            a = float(input("Ingrese el coeficiente a: "))
            if a != 0:
                break
            print("Error: El coeficiente 'a' no puede ser cero")
        except ValueError:
            print("Error: Ingrese un número válido")

    # Validar coeficientes b y c
    while True:
        try:
            b = float(input("Ingrese el coeficiente b: "))
            break
        except ValueError:
            print("Error: Ingrese un número válido")

    while True:
        try:
            c = float(input("Ingrese el coeficiente c: "))
            break
        except ValueError:
            print("Error: Ingrese un número válido")

    # Calcular discriminante
    discriminante = cmath.sqrt(b**2 - 4*a*c)
    
    # Calcular ambas soluciones
    x1 = (-b + discriminante) / (2*a)
    x2 = (-b - discriminante) / (2*a)

    # Formatear resultados
    print("\nSoluciones:")
    print(f"x₁ = {x1.real:.3f} {x1.imag:+.3f}i" if x1.imag else f"x₁ = {x1.real:.3f}")
    print(f"x₂ = {x2.real:.3f} {x2.imag:+.3f}i" if x2.imag else f"x₂ = {x2.real:.3f}")

# Ejecutar el programa
resolver_ecuacion_cuadratica()