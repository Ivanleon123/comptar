def comptar_majuscules(cadena):
    """Retorna el nombre de lletres majúscules en la cadena."""
    return sum(1 for caracter in cadena if caracter.isupper())

# Proves de la funció
print(comptar_majuscules("Hola, món!"))             # Retorna 1
print(comptar_majuscules("Python és FANTÀSTIC"))    # Retorna 3
print(comptar_majuscules("aBcDeF"))                  # Retorna 3
print(comptar_majuscules("totes són minúscules"))   # Retorna 0
print(comptar_majuscules(""))                         # Retorna 0