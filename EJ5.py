
from graph import Graph

g = Graph(is_directed=False) 


nodes_data = [
        ("Red Hat", "Notebook"), 
        ("Debian", "Notebook"), 
        ("Arch", "Notebook"),
        ("Manjaro", "PC"), 
        ("Parrot", "PC"), 
        ("Fedora", "PC"),
        ("Ubuntu", "PC"), 
        ("Mint", "PC"),
        ("Guaraní", "Servidor"), 
        ("MongoDB", "Servidor"),
        ("Switch 1", "Switch"), 
        ("Switch 2", "Switch"),
        ("Router 1", "Router"), 
        ("Router 2", "Router"), 
        ("Router 3", "Router"),
        ("Impresora", "Impresora")
]
for node, tipo in nodes_data:
        g.insert_vertex(node)

edges_data = [
        ('Red Hat', 'Router 2', 25),
        ('Debian', 'Switch 1', 17),
        ('Ubuntu', 'Switch 1', 18),
        ('Impresora', 'Switch 1', 22),
        ('Mint', 'Switch 1', 80),
        ('Switch 1', 'Router 1', 29),
        ('Router 1', 'Router 2', 37),
        ('Router 1', 'Router 3', 43),
        ('Router 2', 'Guaraní', 9),
        ('Router 2', 'Router 3', 50),
        ('Router 3', 'Switch 2', 61),
        ('Switch 2', 'Manjaro', 40),
        ('Switch 2', 'Parrot', 12),
        ('Switch 2', 'Fedora', 3),
        ('Switch 2', 'Arch', 56),
        ('Switch 2', 'MongoDB', 5)
]
for origin, destination, weigth in edges_data:
        g.insert_edge(origin, destination, weigth)

print("a) Grafo de red cargado")
g.show()

notebooks=["Red Hat","Debian","Arch"]

for notebook in notebooks:
    g.deep_sweep(notebook)

print("b)barrido en amplitud")
for notebook in notebooks:
    g.amplitude_sweep(notebook)

print("\n(C) Camino más corto para enviar a imprimir:")

pcs = ["Manjaro", "Fedora", "Red Hat"]

mejor_pc = None
mejor_camino = None
mejor_costo = None

for pc in pcs:
    path = g.dijkstra(pc)
    destination = 'Impresora'
    peso_total = None
    camino_completo = []

    while path.size() > 0:
        value = path.pop()
        if value[0] == destination:
            if peso_total is None:
                peso_total = value[1]
            camino_completo.append(value[0])
            destination = value[2]

    
    if peso_total is not None:
        camino_completo.reverse()

        
        if mejor_costo is None or peso_total < mejor_costo:
            mejor_pc = pc
            mejor_camino = camino_completo
            mejor_costo = peso_total


if mejor_pc is not None:
    print(f'El camino más corto es desde {mejor_pc}: {" -> ".join(mejor_camino)} (Costo: {mejor_costo})')
else:
    print("Ninguna PC tiene camino hacia la impresora.")


print("d) Árbol de expansión mínima: ") 
tree=g.kruskal("Red Hat") 
print(tree)

print("\n(e) Camino más corto desde cada PC hacia 'Guaraní':")

pcs = ["Manjaro","Parrot","Fedora","Ubuntu","Mint"]

mejor_camino = None
mejor_costo = None
mejor_pc = None

for pc in pcs:
    path = g.dijkstra(pc)
    destination = 'Guaraní'
    peso_total = None
    camino_completo = []

    while path.size() > 0:
        value = path.pop()
        if value[0] == destination:
            if peso_total is None:
                peso_total = value[1]
            camino_completo.append(value[0])
            destination = value[2]

    if peso_total is not None:
        camino_completo.reverse()

        
        if mejor_costo is None or peso_total < mejor_costo:
            mejor_costo = peso_total
            mejor_camino = camino_completo
            mejor_pc = pc


if mejor_costo is not None:
    print(f"El camino Mas corto  es desde {mejor_pc}: {' -> '.join(mejor_camino)} (Costo: {mejor_costo})")
else:
    print("Ninguna PC pudo llegar a Guaraní.")



print("\n(f) Camino más corto hacia MongoDB:")

pcs = ["Ubuntu", "Debian", "Mint"]

mejor_pc = None
mejor_costo = None
mejor_camino = None

for pc in pcs:
    path = g.dijkstra(pc)
    destino = "MongoDB"
    peso_total = None
    camino_completo = []

    while path.size() > 0:
        value = path.pop()
        if value[0] == destino:
            if peso_total is None:
                peso_total = value[1]
            camino_completo.append(value[0])
            destino = value[2]

    if peso_total is not None:
        camino_completo.reverse()

        if mejor_costo is None or peso_total < mejor_costo:
            mejor_pc = pc
            mejor_costo = peso_total
            mejor_camino = camino_completo

if mejor_pc is not None:
    print(f"El camino más corto es desde {mejor_pc}: {' -> '.join(mejor_camino)} (Costo: {mejor_costo})")
else:
    print("Ninguna PC tiene camino a MongoDB.")

    
print("g) Cambio de conexión de la Impresora al router 02")
g.delete_edge('Switch 1', 'Impresora', 'value')
print("Arista 'Switch 1 <-> Impresora' eliminada.")

g.insert_edge('Router 2', 'Impresora', 22)
print(f"Arista 'Router 2 <-> Impresora' creada.")


print("g) Barrido en profundidad: ")
for notebook in notebooks: 
    g.deep_sweep(notebook)

print("g) Barrido en amplitud: ")
for notebook in notebooks: 
    g.amplitude_sweep(notebook)




