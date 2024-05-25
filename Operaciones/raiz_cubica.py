def raiz_cubica(numero, tolerancia=1e-10):
  """
  Utilizando el 'Mètodo Babilonìa o Herón'. Se calculará la raiz cúbica del numero ingresado. 
  1e-10 es una forma de notación científica que representa el número.
  1 × 10 **−10, que es igual a 0.0000000001. Es un número muy pequeño que indica una precisión muy alta.
    
  Args:
    numero (int, float): Este será el numero ingresado por el usuario.
    tolerancia (int, float): Este valor se utilizara como limite de precisión. Default es 1e-10.

  Raises:
    ValueError: Si numero es negativo: ValueError: No se puede calcular la raìz cuadrada de un nùmero negativo".

  Returns:
    float: Resultado más próximo al valor de calcular la raíz cúbica de un número.
  """
  if numero < 0:
    raise ValueError("No se puede calcular la raìz cuadrada de un nùmero negativo")
  if numero == 0:
    return 0
  
  # Inicializar la aproximación inicial.
  aproximacion = numero / 3.0
      
  while True:
    # Calcular una nueva aproximación.
    nueva_aproximacion = (2 * aproximacion + numero / (aproximacion ** 2)) / 3

    # Comprobar si la diferencia entre las aproximaciones es menor que la tolerancia.
    if abs(aproximacion - nueva_aproximacion) < tolerancia:
      return nueva_aproximacion

    # Actualizar la aproximación actual.
    aproximacion = nueva_aproximacion

# Ejemplo de uso
try:
  resultado = raiz_cubica(27)
  print(resultado)  # Resultado esperado pro aproximación: 3
except ValueError as err:
      print(err)