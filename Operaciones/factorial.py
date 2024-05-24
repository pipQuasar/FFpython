def factorial(numero):
      """
      Opera con el número ingresado por el usuario paraencontrar su factorial. Ejemplo: !5 = 5x1 + 5x2 + 5x3 + 5x4 + 5x5.
          Siempre debe operarse con valores enteros.
      
      Args:
          numero (int): Número ingresado por el ususario

      Raises:
          ValueError: "Error! Se debe proporcionar al menos un número..."

      Returns:
          resultado: int
      """
      if not numero:  # Si no se ingresa un número, no se puede operar nada.
       raise ValueError("Error! Se debe proporcionar al menos un número...")
      
      resultado = 1
      for i in range (numero):
            resultado *= i+1
      
      return resultado

# Ejemplo de uso
try:
      resultado = factorial(5)
      print(resultado)  # Resultado esperado: 120
except ValueError as err:
      print(err)