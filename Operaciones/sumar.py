def sumar(*numeros):
    if not numeros:
      raise ValueError("Error! Se debe proporcionar al menos un numero...")

    return sum(numeros)

# Ejemplo de uso
try:
    resultado = sumar(1,2,3,4,5)
    print(resultado)  # Salida: 15
except ValueError as e:
    print(e)