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
    if not numeros:  # Si no se ingresa un número, no se puede operar nada.
      raise ValueError("Error! Se debe proporcionar al menos un número...")
      
    return numeros[0] - sum(numeros[1:]) # Se crea una tupla en donde el primer valor siempre se le va a restar los siguientes.

# Ejemplo de uso
try:
    resultado = restar(1,2,3,4,5)
    print(resultado)  # Salida: -13
except ValueError as err:
    print(err)      