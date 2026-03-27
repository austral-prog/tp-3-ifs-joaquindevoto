def password():
    """
    Ejercicio 10 - Validador de Contraseña

    Leer una contraseña mediante input(). Validar que cumpla con los siguientes requisitos:
    1. Debe tener al menos 8 caracteres de longitud
    2. Debe contener al menos un número (usar el operador in para verificar cada dígito del 0 al 9)

    Si cumple ambos requisitos, imprimir "Contraseña valida".
    Si no cumple, imprimir cuál requisito falta.

    Ejemplo:
        Para la entrada "abc12345", la salida esperada es:
        Contraseña valida

        Para la entrada "abc123", la salida esperada es:
        Contraseña muy corta

        Para la entrada "abcdefgh", la salida esperada es:
        Debe contener un numero

        Para la entrada "abc", la salida esperada es:
        Contraseña muy corta
        Debe contener un numero
    """

    contraseña= input()

    if len(contraseña)>=8:
        largo_valido= True
    else:
        largo_valido= False

    if "1"in contraseña or "2"in contraseña or "3"in contraseña or "4"in contraseña or "5"in contraseña or "6"in contraseña or "7"in contraseña or "8"in contraseña or "9"in contraseña or "0"in contraseña:
        numero_valido= True
    else:
        numero_valido= False

    if largo_valido and numero_valido:
        print("Contraseña valida")

    elif not largo_valido and not numero_valido:
        print("Contraseña muy corta\nDebe contener un numero")

    elif not largo_valido and numero_valido:
        print("Contraseña muy corta")

    elif largo_valido and not numero_valido:
        print("Debe contener un numero")


