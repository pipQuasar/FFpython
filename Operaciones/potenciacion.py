def potenciacion(numero):
      """
      Utiliza un número ingresado por el usuario, luego le pide el exponente para
     realizar la potenciación. Al final devuelve el resultado.
      
      Args:
          numero (float): Numero a potenciar.
          exponente (float): Numero potenciador.

      Raises:
          ValueError: "Error! Se debe proporcionar al menos un numero..."

      Returns:
          float: Resultado de la potenciacion.
      """
      print(f"Numero ingresado: {numero}")
      if not numero:    # Si no se ingresa un número, no se puede operar nada.
        raise ValueError("Error! Se debe proporcionar al menos un numero...")
      exponente = int(input("Exponente: "))
      if not exponente: # Si no se ingresa un exponente, no se puede operar nada.
        raise ValueError("Error! Se debe proporcionar al menos un numero...")
      
      return numero ** exponente

#Ejemplo de uso
try:
    resultado = potenciacion(2.5)
    print(resultado)  # Salida: Depende del exponente, en este ejemplo usaré 10 ** 2, resultado = 100
except ValueError as err:
    print(err)  