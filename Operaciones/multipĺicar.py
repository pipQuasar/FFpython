def multiplicar(*numeros):
      """
      Multiplica la cantidad de numeros que quieras, ya sean 2 o más. 1 x 2 x 3 x 4 x 5 x...
      
      Args:
      - *numeros (float): Secuencia de números a multiplicar.
      
      Raises:
          ValueError: "Error! Se debe proporcionar al menos un numero..."

      Returns:
          float: Resultado de la multiplicación.
      """
      if not numeros:
        raise ValueError("Error! Se debe proporcionar al menos un numero...")
      
      resultado = 1
      for num in numeros:
        resultado *= num
      return resultado

# Ejemplo de uso
try:
    resultado = multiplicar(1,2,3,4,5)
    print(resultado)  # Salida: 120
except ValueError as err:
    print(err)      