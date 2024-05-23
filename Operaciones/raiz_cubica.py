def raiz_cubica(numero, tolerancia=1e-10):
      if numero < 0:
        raise ValueError("No se puede calcular la raìz cuadrada de un nùmero negativo")
      if numero == 0:
        return 0
  
      # Inicializar la aproximación inicial
      aproximacion = numero / 3.0
      
      while True:
        # Calcular una nueva aproximación
        nueva_aproximacion = (2 * aproximacion + numero / (aproximacion ** 2)) / 3

        # Comprobar si la diferencia entre las aproximaciones es menor que la tolerancia
        if abs(aproximacion - nueva_aproximacion) < tolerancia:
            return nueva_aproximacion

        # Actualizar la aproximación actual
        aproximacion = nueva_aproximacion
        
resultado = raiz_cubica(27)
print(resultado)