superheroes = [
    "Iron Man", "Spider-Man", "Hulk", "Thor", "Black Widow",
    "Hawkeye", "Black Panther", "Doctor Strange", "Scarlet Witch",
    "Ant-Man", "Wasp", "Vision", "Falcon", "Winter Soldier", "Capitan America"
]


def buscar_capitan(lista, indice=0):
    if indice >= len(lista):
        return False
    if lista[indice] == "Capitan America":
        return True
    return buscar_capitan(lista, indice + 1)


def listar_superheroes(lista, indice=0):
    if indice >= len(lista): 
        return
    print(lista[indice])
    listar_superheroes(lista, indice + 1)


if buscar_capitan(superheroes):
    print("Capitan America está en la lista.")
else:
    print("Capitan America NO está en la lista.")

print("\nLista de superhéroes:")
listar_superheroes(superheroes)
