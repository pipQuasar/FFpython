def sumar(*numeros):
    """
    Suma la cantidad de numeros que quieras, ya sean 2 o más. 1 + 2 + 3 + 4 + 5 +...
    
    Args:
      - *numeros (float): Secuencia de números a sumar.
      
    Raises:
        ValueError: "Error! Se debe proporcionar al menos un número..."

    Returns:
        float: Resultado de la suma.
    """
    if not numeros:
      raise ValueError("Error! Se debe proporcionar al menos un numero...")

    return sum(numeros)

# Ejemplo de uso
try:
    resultado = sumar(1,2,3,4,5)
    print(resultado)  # Salida: 15
except ValueError as err:
    print(err)