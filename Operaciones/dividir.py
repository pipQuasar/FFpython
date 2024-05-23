def dividir(*numeros):
      """
      Divide la cantidad de numeros que quieras, ya sean 2 o más. 1 / 2 / 3 / 4 / 5 /...
      
      Args:
      - *numeros (float): Secuencia de números a dividir.
      
      Raises:
          ValueError: "Error! Se debe proporcionar al menos un numero..."

      Returns:
          float: Resultado de la división.
      """
      if len(numeros) == 0:
        raise ValueError("Se debe ingresar al menos un número para dividir.")
      resultado = numeros[0]
      for num in numeros[1:]:
        resultado /= num
      return resultado
      
# Ejemplo de uso
try:
    resultado = dividir(10,2,2) # Se introducen los numeros que desées dividir
    print(resultado)  # Salida: 2.5
except ValueError as err:
    print(err)