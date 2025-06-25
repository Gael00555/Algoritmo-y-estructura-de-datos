superheroes = [
    "Iron Man", "Hulk", "Thor", "Black Widow", "Hawkeye",
    "Spiderman", "Wolverine", "Black Panther", "Doctor Strange",
    "Vision", "Scarlet Witch", "Falcon", "Ant Man", "Wasp", "Captain America"
]

def esta_capitan_america(lista, index=0):
    if index >= len(lista):
        return False
    if lista[index] == "Captain America":
        return True
    return esta_capitan_america(lista, index + 1)

def listar_superheroes(lista, index=0):
    if index >= len(lista):
        return
    print(lista[index])
    listar_superheroes(lista, index + 1)


print("¿Está 'Captain America' en la lista de superhéroes?")
if esta_capitan_america(superheroes):
    print("Sí, está en la lista.")
else:
    print("No, no está en la lista.")

print("\nListado de superhéroes:")
listar_superheroes(superheroes)


