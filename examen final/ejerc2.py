def analizar_cadena(cadena):
    vocales = "aeiouAEIOU"
    consonantes = "bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ"
    
    num_vocales = sum(1 for char in cadena if char in vocales)
    num_consonantes = sum(1 for char in cadena if char in consonantes)
    num_otros = len(cadena) - num_vocales - num_consonantes
    
    palabras = cadena.split()
    num_palabras = len(palabras)
    existe_que = "que" in cadena
    
    num_minusculas = sum(1 for char in cadena if char.islower())
    num_mayusculas = sum(1 for char in cadena if char.isupper())
    
    num_a = cadena.count('a') + cadena.count('A')
    num_f = cadena.count('f') + cadena.count('F')
    
    print(f"Cantidad de vocales: {num_vocales}")
    print(f"Cantidad de consonantes: {num_consonantes}")
    print(f"Cantidad de otros caracteres: {num_otros}")
    print(f"Cantidad de palabras: {num_palabras}")
    print(f"Existe la palabra 'que': {existe_que}")
    print(f"Cantidad de minúsculas: {num_minusculas}")
    print(f"Cantidad de mayúsculas: {num_mayusculas}")
    print(f"Cantidad de la letra 'a': {num_a}")
    print(f"Cantidad de la letra 'f': {num_f}")

# Ejemplo de uso
cadena = input("Ingresa una cadena de texto: ")
analizar_cadena(cadena)