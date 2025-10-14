from tree import BinaryTree

class CreaturesTree(BinaryTree):
    class __nodeTree(BinaryTree._BinaryTree__nodeTree):
        def __init__(self, value: str, other_values: dict = None):
            if other_values is None:
                other_values = {
                    "defeated_by": [],
                    "description": "",
                    "captured_by": None,
                }
            super().__init__(value, other_values)

creatures = {
    "Ceto": {"defeated_by": "", "description": "", "captured_by": None},
    "Tifón": {"defeated_by": "Zeus", "description": "", "captured_by": None},
    "Equidna": {"defeated_by": "Argos Panoptes", "description": "", "captured_by": None},
    "Dino": {"defeated_by": "", "description": "", "captured_by": None},
    "Pefredo": {"defeated_by": "", "description": "", "captured_by": None},
    "Enio": {"defeated_by": "", "description": "", "captured_by": None},
    "Escila": {"defeated_by": "", "description": "", "captured_by": None},
    "Caribdis": {"defeated_by": "", "description": "", "captured_by": None},
    "Euríale": {"defeated_by": "", "description": "", "captured_by": None},
    "Esteno": {"defeated_by": "", "description": "", "captured_by": None},
    "Medusa": {"defeated_by": "Perseo", "description": "", "captured_by": None},
    "Ladón": {"defeated_by": "Heracles", "description": "", "captured_by": None},
    "Águila del Cáucaso": {"defeated_by": "", "description": "", "captured_by": None},
    "Quimera": {"defeated_by": "Belerofonte", "description": "", "captured_by": None},
    "Hidra de Lerna": {"defeated_by": "Heracles", "description": "", "captured_by": None},
    "León de Nemea": {"defeated_by": "Heracles", "description": "", "captured_by": None},
    "Esfinge": {"defeated_by": "Edipo", "description": "", "captured_by": None},
    "Dragón de la Cólquida": {"defeated_by": "", "description": "", "captured_by": "Jasón"},
    "Cerbero": {"defeated_by": "", "description": "", "captured_by": "Heracles"},
    "Cerda de Cromión": {"defeated_by": "Teseo", "description": "", "captured_by": None},
    "Ortro": {"defeated_by": "Heracles", "description": "", "captured_by": None},
    "Toro de Creta": {"defeated_by": "Teseo", "description": "", "captured_by": None},
    "Jabalí de Calidón": {"defeated_by": "Atalanta", "description": "", "captured_by": None},
    "Carcinos": {"defeated_by": "", "description": "", "captured_by": None},
    "Gerión": {"defeated_by": "Heracles", "description": "", "captured_by": None},
    "Cloto": {"defeated_by": "", "description": "", "captured_by": None},
    "Láquesis": {"defeated_by": "", "description": "", "captured_by": None},
    "Átropo": {"defeated_by": "", "description": "", "captured_by": None},
    "Minotauro de Creta": {"defeated_by": "Teseo", "description": "", "captured_by": None},
    "Harpías": {"defeated_by": "", "description": "", "captured_by": None},
    "Argos Panoptes": {"defeated_by": "Hermes", "description": "", "captured_by": None},
    "Aves del Estínfalo": {"defeated_by": "", "description": "", "captured_by": None},
    "Talos": {"defeated_by": "Medea", "description": "", "captured_by": None},
    "Sirenas": {"defeated_by": "", "description": "", "captured_by": None},
    "Pitón": {"defeated_by": "Apolo", "description": "", "captured_by": None},
    "Cierva de Cerinea": {"defeated_by": "", "description": "", "captured_by": "Heracles"},
    "Basilisco": {"defeated_by": "", "description": "", "captured_by": None},
    "Jabalí de Erimanto": {"defeated_by": "", "description": "", "captured_by": "Heracles"},
}




creaturestree = CreaturesTree()
for creature, data in creatures.items():
    creaturestree.insert(creature, data)


print("a) Listado de las criaturas:")
creaturestree.in_order()


def cargar_descripcion(tree, nombre, descripcion):
    nodo = tree.search(nombre)
    if nodo:
        nodo.other_values["description"] = descripcion
        print(f"b) Descripción agregada a {nombre}")
    else:
        print(f"{nombre} no encontrada en el árbol.")


cargar_descripcion(creaturestree, "Talos", "Gigante de bronce que protegía Creta.")
cargar_descripcion(creaturestree, "Ceto", "Monstruo marino primigenio.")


def mostrar_info(tree, nombre):
    nodo = tree.search(nombre)
    if nodo:
        print(f"\nc) Información de {nombre}:")
        print(nodo.other_values)
    else:
        print(f"{nombre} no encontrada.")

mostrar_info(creaturestree, "Talos")


from collections import Counter

def top_3_derrotadores(tree):
    contador = Counter()
    def recorrer(nodo):
        if nodo:
            if nodo.other_values["defeated_by"]:
                contador[nodo.other_values["defeated_by"]] += 1
            recorrer(nodo.left)
            recorrer(nodo.right)
    recorrer(tree.root)
    print("\nd) Los 3 héroes o dioses con más derrotas:")
    for heroe, cantidad in contador.most_common(3):
        print(f"   {heroe}: {cantidad}")

top_3_derrotadores(creaturestree)


def criaturas_derrotadas_por(tree, heroe):
    print(f"\ne) Criaturas derrotadas por {heroe}:")
    def recorrer(nodo):
        if nodo:
            if nodo.other_values["defeated_by"] == heroe:
                print("  -", nodo.value)
            recorrer(nodo.left)
            recorrer(nodo.right)
    recorrer(tree.root)

criaturas_derrotadas_por(creaturestree, "Heracles")


def criaturas_no_derrotadas(tree):
    print("\nf) Criaturas que no han sido derrotadas:")
    def recorrer(nodo):
        if nodo:
            if nodo.other_values["defeated_by"] == "":
                print("  -", nodo.value)
            recorrer(nodo.left)
            recorrer(nodo.right)
    recorrer(tree.root)

criaturas_no_derrotadas(creaturestree)


def marcar_capturadas(tree, nombres, heroe):
    for nombre in nombres:
        nodo = tree.search(nombre)
        if nodo:
            nodo.other_values["captured_by"] = heroe
            print(f"{nombre} marcada como capturada por {heroe}.")

capturadas_por_heracles = ["Cerbero", "Toro de Creta", "Cierva de Cerinea", "Jabalí de Erimanto"]
marcar_capturadas(creaturestree, capturadas_por_heracles, "Heracles")


def busqueda_coincidencia(tree, texto):
    print(f"\ni) Coincidencias con '{texto}':")
    resultados = tree.proximity_search(texto)
    if resultados:
        for nodo in resultados:
            print("  -", nodo.value)
    else:
        print("No se encontraron coincidencias.")

busqueda_coincidencia(creaturestree, "Med")


def eliminar_criaturas(tree, lista):
    for nombre in lista:
        eliminado, otros = tree.delete(nombre)
        if eliminado:
            print(f"Eliminada criatura: {nombre}")

eliminar_criaturas(creaturestree, ["Basilisco", "Sirenas"])


def modificar_aves(tree):
    nodo = tree.search("Aves del Estínfalo")
    if nodo:
        nodo.other_values["defeated_by"] = "Heracles (varias)"
        print("\nk) Nodo modificado: Aves del Estínfalo derrotadas por Heracles (varias).")

modificar_aves(creaturestree)


def renombrar_criatura(tree, nombre_viejo, nombre_nuevo):
    eliminado, info = tree.delete(nombre_viejo)
    if eliminado:
        tree.insert(nombre_nuevo, info)
        print(f"\nl) {nombre_viejo} renombrado a {nombre_nuevo}.")

renombrar_criatura(creaturestree, "Ladón", "Dragón Ladón")


print("\nm) Listado por nivel del árbol:")
creaturestree.by_level()


def criaturas_capturadas_por(tree, heroe):
    print(f"\nn) Criaturas capturadas por {heroe}:")
    def recorrer(nodo):
        if nodo:
            if nodo.other_values["captured_by"] == heroe:
                print("  -", nodo.value)
            recorrer(nodo.left)
            recorrer(nodo.right)
    recorrer(tree.root)

criaturas_capturadas_por(creaturestree, "Heracles")
 
