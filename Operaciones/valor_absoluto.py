def valor_absoluto(numero):
  """
  Se calculará el valor absoluto |numero| utilizando la funcion abs().
      
  Args:
    numero (int, float): Este será el numero ingresado por el usuario

  Raises:
    ValueError: "Error! Se debe proporcionar al menos un numero..."

  Returns:
    int/float: El resultado absoluto del valor ingresado por el usuario
  """
  if not numero:    # Si no se ingresa un número, no se puede operar nada.
    raise ValueError("Error! Se debe proporcionar al menos un numero...")
  
  resultado = abs(numero)
  return resultado

# Ejemplo de uso
try:
    resultado = valor_absoluto(-8)
    print(resultado) # Resultado esperado: 8
except ValueError as err:
      print(err)    