def restar(*numeros):
    """
    Resta la cantidad de numeros que quieras, ya sean 2 o más. 1 - 2 - 3 - 4 - 5 -...
    
    Args:
      - *numeros (float): Secuencia de números a restar.
      
    Raises:
        ValueError: "Error! Se debe proporcionar al menos un número..."

    Returns:
        float: Resultado de la resta.
    """
    if not numeros:
      raise ValueError("Error! Se debe proporcionar al menos un número...")
      
    return numeros[0] - sum(numeros[1:])

# Ejemplo de uso
try:
    resultado = restar(1,2,3,4,5) # Se ingresan los números que desées restar
    print(resultado)  # Salida: -13
except ValueError as err:
    print(err)      