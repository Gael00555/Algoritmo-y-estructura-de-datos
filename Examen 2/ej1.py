from tree import BinaryTree
from pokemons_data import pokemons

arbol_nombre = BinaryTree()
arbol_numero = BinaryTree()

for p in pokemons:
    arbol_nombre.insert(p["nombre"], p)
    arbol_numero.insert(p["numero"], p)

def buscar_por_numero(numero):
    print(f"\n1) Pokémon con número {numero}:")
    nodo = arbol_numero.search(numero)
    if nodo is None:
        print("No existe el Pokémon con ese número.")
    else:
        print(nodo.other_values)

def buscar_por_nombre_prox(texto):
    print(f"\n1) Búsqueda por proximidad '{texto}':")
    resultados = []

    def _rec(root):
        if root:
            _rec(root.left)
            if texto.lower() in root.value.lower():
                resultados.append(root)
            _rec(root.right)

    _rec(arbol_nombre.root)

    if not resultados:
        print("No hubo coincidencias.")
    else:
        for r in resultados:
            print(r.value, r.other_values)

def listar_por_tipo(tipo):
    print(f"\n2) Pokémon del tipo {tipo}:")
    def _rec(root):
        if root:
            _rec(root.left)
            if tipo in root.other_values["tipo"]:
                print(root.other_values["nombre"])
            _rec(root.right)

    _rec(arbol_nombre.root)

def listado_ordenado_numero():
    print("\n3) Listado ascendente por número:")
    def _rec(root):
        if root:
            _rec(root.left)
            print(root.value, "-", root.other_values["nombre"])
            _rec(root.right)
    _rec(arbol_numero.root)

def listado_ordenado_nombre():
    print("\n3) Listado ascendente por nombre:")
    def _rec(root):
        if root:
            _rec(root.left)
            print(root.value)
            _rec(root.right)
    _rec(arbol_nombre.root)

def listado_por_niveles():
    print("\n3) Listado por niveles (por nombre):")
    arbol_nombre.by_level()

def pokemons_debiles_a(nombre):
    print(f"\n4) Pokémon débiles frente a {nombre}:")
    nodo = arbol_nombre.search(nombre)
    if nodo is None:
        print("Pokémon no encontrado.")
        return

    tipos_ataque = nodo.other_values["tipo"]

    def _rec(root):
        if root:
            _rec(root.left)
            debs = root.other_values["debilidad"]
            if any(t in debs for t in tipos_ataque):
                print(root.other_values["nombre"])
            _rec(root.right)

    _rec(arbol_nombre.root)

def contar_por_tipo():
    print("\n5) Cantidad de Pokémon por tipo:")
    tipos = {}

    def _rec(root):
        if root:
            _rec(root.left)
            for t in root.other_values["tipo"]:
                if t not in tipos:
                    tipos[t] = 0
                tipos[t] += 1
            _rec(root.right)

    _rec(arbol_nombre.root)

    for tipo, cant in tipos.items():
        print("Tipo:", tipo, "→ Cantidad:", cant)

def contar_mega():
    print("\n6) Cantidad de Pokémon con megaevolución:")
    def _rec(root):
        if root is None:
            return 0
        contador = 1 if root.other_values.get("mega_evolucion", False) else 0
        return contador + _rec(root.left) + _rec(root.right)

    print(_rec(arbol_nombre.root))

def contar_gigamax():
    print("\n7) Cantidad de Pokémon con forma gigamax:")
    def _rec(root):
        if root is None:
            return 0
        contador = 1 if root.other_values.get("forma_gigamax", False) else 0
        return contador + _rec(root.left) + _rec(root.right)

    print(_rec(arbol_nombre.root))


buscar_por_numero(6)
buscar_por_nombre_prox("char")
listar_por_tipo("Fuego")
listar_por_tipo("Fantasma")
listar_por_tipo("Acero")
listar_por_tipo("Eléctrico")
listado_ordenado_numero()
listado_ordenado_nombre()
listado_por_niveles()
pokemons_debiles_a("Jolteon")
pokemons_debiles_a("Lycanroc")
pokemons_debiles_a("Tyrantrum")
contar_por_tipo()
contar_mega()
contar_gigamax()

