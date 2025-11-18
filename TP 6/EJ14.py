from graph import Graph

g = Graph(is_directed=False)



nodes_data = [
    ("cocina", "ambiente"),
    ("comedor", "ambiente"),
    ("cochera", "ambiente"),
    ("quincho", "ambiente"),
    ("baño 1", "ambiente"),
    ("baño 2", "ambiente"),
    ("habitación 1", "ambiente"),
    ("habitación 2", "ambiente"),
    ("sala de estar", "ambiente"),
    ("terraza", "ambiente"),
    ("patio", "ambiente"),
]

for node, tipo in nodes_data:
    g.insert_vertex(node)


edges_data = [
    ("cocina", "comedor", 4),
    ("cocina", "quincho", 12),
    ("cocina", "baño 1", 6),
    ("cocina", "patio", 8),

    ("comedor", "sala de estar", 5),
    ("comedor", "habitación 1", 10),
    ("comedor", "terraza", 9),

    ("cochera", "patio", 7),
    ("cochera", "quincho", 15),
    ("cochera", "habitación 2", 11),

    ("quincho", "patio", 6),
    ("quincho", "terraza", 18),
    ("quincho", "habitación 2", 10),
    ("quincho", "comedor", 12),
    ("quincho", "cocina", 12),  # 5 conexiones

    ("baño 1", "habitación 1", 4),
    ("baño 1", "baño 2", 3),
    ("baño 1", "comedor", 6),

    ("baño 2", "habitación 2", 5),
    ("baño 2", "sala de estar", 9),
    ("baño 2", "terraza", 14),

    ("habitación 1", "habitación 2", 7),
    ("habitación 1", "sala de estar", 12),

    ("habitación 2", "terraza", 10),

    ("sala de estar", "terraza", 6),
    ("sala de estar", "patio", 13),

    ("terraza", "patio", 5)
]

for origin, destination, weight in edges_data:
    g.insert_edge(origin, destination, weight)

print(" Grafo de ambientes cargado")
g.show()

print("\n(c) Árbol de expansión mínima:")
tree = g.kruskal("cocina")
print(tree)


partes = tree.split(";")
total_metros = 0

for edges in partes:
    edge_data = edges.split("-")   
    if len(edge_data) == 3:
        total_metros += int(edge_data[2])

print(f"\nMetros totales necesarios para cablear toda la casa: {total_metros} metros")


print("\n(d) Camino más corto desde 'habitación 1' a 'sala de estar':")

path = g.dijkstra("habitación 1")
destination = "sala de estar"
peso_total = None
camino_completo = []

while path.size() > 0:
    value = path.pop()
    if value[0] == destination:
        if peso_total is None:
            peso_total = value[1]
        camino_completo.append(value[0])
        destination = value[2]

camino_completo.reverse()

if peso_total is not None:
    print(f"Camino: {' -> '.join(camino_completo)} (Costo total: {peso_total} metros)")
else:
    print("No existe camino entre habitación 1 y sala de estar.")

