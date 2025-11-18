from graph import Graph
import math


g = Graph(is_directed=False)   


vertices_data = [
    ("Luke Skywalker", 6),
    ("Darth Vader", 4),
    ("Yoda", 5),
    ("Boba Fett", 3),
    ("C-3PO", 7),
    ("Leia", 6),
    ("Rey", 3),
    ("Kylo Ren", 3),
    ("Chewbacca", 6),
    ("Han Solo", 6),
    ("R2-D2", 7),
    ("BB-8", 2),
]


for name, episodes in vertices_data:
    g.insert_vertex(name)
    pos = g.search(name, 'value')
    if pos is not None:
        g[pos].other_values = {'episodes': episodes, 'name': name}

edges_data = [
    ("Luke Skywalker", "Leia", 6),
    ("Luke Skywalker", "Han Solo", 6),
    ("Luke Skywalker", "Darth Vader", 3),
    ("Luke Skywalker", "Chewbacca", 5),
    ("Leia", "Han Solo", 5),
    ("Leia", "C-3PO", 6),
    ("C-3PO", "R2-D2", 7),
    ("Han Solo", "Chewbacca", 6),
    ("Darth Vader", "C-3PO", 2),
    ("Yoda", "Luke Skywalker", 2),
    ("Yoda", "Darth Vader", 1),
    ("Boba Fett", "Darth Vader", 1),
    ("Rey", "BB-8", 2),
    ("Rey", "Kylo Ren", 1),
    ("Kylo Ren", "Rey", 1),
    ("Chewbacca", "R2-D2", 4),
    ("BB-8", "R2-D2", 1),
    ("C-3PO", "Leia", 6),
    ("C-3PO", "Han Solo", 4),
    ("Darth Vader", "Luke Skywalker", 3),  
]

for origin, destination, weight in edges_data:
    g.insert_edge(origin, destination, weight)
    g.insert_edge(destination, origin, weight)

print("Grafo Star Wars cargado .")
g.show()

print(f"1)Árbol de expansión mínimo desde C-3PO:")
print(g.kruskal("C-3PO"))

print(f"1)Árbol de expansión mínimo desde Yoda:")
print(g.kruskal("Yoda"))

print(f"1)Árbol de expansión mínimo desde Leia:")
print(g.kruskal("Leia"))

max_ep = 0
pares = []

for vertex in g:                    
        for edge in vertex.edges:           

            
            if vertex.value < edge.value:

                if edge.weight > max_ep:
                    max_ep = edge.weight
                    pares = [(vertex, edge)]
                elif edge.weight == max_ep:
                    pares.append((vertex, edge))

   
print(f"2) Máximo número de episodios compartidos: {max_ep}")
print("Pares de personajes:")

for v1, v2 in pares:
        print(f"- {v1.value} y {v2.value}")



path = g.dijkstra("C-3PO")
dest = "R2-D2"
camino = []
costo = None

while path.size() > 0:
    data = path.pop()
    if data[0] == dest:
        if costo is None:
            costo = data[1]
        camino.append(data[0])
        dest = data[2]

camino.reverse()
print(f"3)Camino más corto C-3PO → R2-D2:", camino, "costo =", costo)

path = g.dijkstra("Yoda")
dest = "Darth Vader"
camino = []
costo = None

while path.size() > 0:
    data = path.pop()
    if data[0] == dest:
        if costo is None:
            costo = data[1]
        camino.append(data[0])
        dest = data[2]

camino.reverse()
print(f"3)Camino más corto Yoda → Darth Vader:", camino, "costo =", costo)


episodios = []
for vertex in g:
    for edge in vertex.edges:
        if edge.weight == 9:
            episodios.append(vertex.value)
print(f"f) Personajes que aparecieron en los nueve episodios de la saga: {episodios}")

