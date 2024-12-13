import random

# Crear una lista vacía
lista_aleatoria = []

# Llenar la lista con 13 números aleatorios entre 1 y 99
for _ in range(13):
    numero = random.randint(1, 99)
    lista_aleatoria.append(numero)

# Crear una lista con los números pares de la lista_aleatoria
lista_pares = [num for num in lista_aleatoria if num % 2 == 0]

# Crear una lista con los números impares de la lista_aleatoria
lista_impares = [num for num in lista_aleatoria if num % 2 != 0]

# Crear una lista con los números múltiplos de 3 de la lista_aleatoria
lista_multiplos_de_3 = [num for num in lista_aleatoria if num % 3 == 0]

# Función para calcular el promedio de una lista
def calcular_promedio(lista):
    if len(lista) == 0:
        return 0
    return sum(lista) / len(lista)

# Mostrar información de las listas
listas = {
    "Lista original": lista_aleatoria,
    "Lista con números pares": lista_pares,
    "Lista con números impares": lista_impares,
    "Lista con números múltiplos de 3": lista_multiplos_de_3
}

for nombre, lista in listas.items():
    print(f"{nombre}:")
    print(f"Tamaño: {len(lista)}")
    print(f"Contenido: {lista}")
    print(f"Contenido ordenado: {sorted(lista)}")
    print(f"Promedio: {calcular_promedio(lista):.2f}")
    print()