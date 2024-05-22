def restar(*numeros):
    if not numeros:
      raise ValueError("Error! Se debe proporcionar al menos un número...")
      
    return numeros[0] - sum(numeros[1:])

# Ejemplo de uso
try:
    resultado = restar(1,2,3,4,5)
    print(resultado)  # Salida: -13
except ValueError as e:
    print(e)      