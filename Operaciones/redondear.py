def redondear(numero):
      """
      Se redondea el numero ingresado por el usuario utilizando la funcion round(), y en esta misma te pedirá la cantidad de decimales con las que decidas trabajar. 
      Tener en cuenta que mientras menos dígitos se utilicen para redondear, mas cercano a un entero va a estar el resultado final, también cabe aclarar que siempre
      redondea hacia arriba si los el primer decimal supera a 5, de lo contrario siempre va a redondear hacia abajo.
      Ejemplo:
            -round(2.53, 2), la coma luego del numero introducido es el luagr en el que debemos poner cuantos digitos queremos
            utilizar para redondear, en este caso el resultado del redondeo sería: 2.53.
            -round(2.53, 0), en este  caso el resultado sería 3 porque no estamos teniendo en cuenta ningún decimal, y como estos
            son mayores a 50, redondea hacia 3.
            -round(2.45, 0), y aquí el resultado sería 2 porque no se tiene en cuenta ningún decimal y su primer valor es menor a 5.
      
      Args:
          numero (int/float): Número ingresado por el usuario

      Raises:
          ValueError: "Error! Se debe proporcionar al menos un número..."

      Returns:
          float: El redondeado dek valor ingresado por el usuario.
      """
      if not numero:  # Si no se ingresa un número, no se puede operar nada.
       raise ValueError("Error! Se debe proporcionar al menos un número...")
      
      print(f"Número a redondear {numero}")
      return round(numero, int(input("¿Cuántos digitos quieres dejar en tu redondeo?: ")))

# Ejemplo de uso
resultado = redondear(2.50)
print(resultado)  # Resultado esperado depende de la cantidad de dígitos quiera dejar el ususario,
                  # 0 dgts = 3, 1 dgts = 2.5, 2 dgts = 2.52
