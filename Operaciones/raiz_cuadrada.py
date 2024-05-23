def raiz_cuadrada(numero, tolerancia=1e-10):
    # Utilizando el 'Mètodo Babilonìa o Herón'
    # 1e-10 es una forma de notación científica que representa el número 
    # 1 × 10 **−10, que es igual a 0.0000000001. Es un número muy pequeño que indica una precisión muy alta.
    if numero < 0:
        raise ValueError("No se puede calcular la raìz cuadrada de un nùmero negativo")
    if numero == 0:
        return 0
    # Inicializar la aproximación inicial
    guess = numero / 2.0

    while True:
        # Calcular una nueva aproximación
        next_guess = (guess + numero / guess) / 2

        # Comprobar si la diferencia entre las aproximaciones es menor que la tolerancia
        if abs(guess - next_guess) < tolerancia:
            return next_guess

        # Actualizar la aproximación actual
        guess = next_guess
