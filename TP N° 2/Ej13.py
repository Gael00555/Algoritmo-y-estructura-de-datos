from typing import Any, Optional

class Stack:

    def __init__(self):
        self.__elements = []

    def push(self, value: Any) -> None:
        self.__elements.append(value)

    def pop(self) -> Optional[Any]:
        return (
            self.__elements.pop()
            if self.__elements
            else None
        )

    def size(self) -> int:
        return len(self.__elements)

    def on_top(self) -> Optional[Any]:
        return (
            self.__elements[-1]
            if self.__elements
            else None
        )

    def show(self):
        aux_stack = Stack()
        while self.size() > 0:
            value = self.pop()
            print(value)
            aux_stack.push(value)
        while aux_stack.size() > 0:
            self.push(aux_stack.pop())


stack_trajes = Stack()


trajes = [
    {'modelo': 'Mark III', 'pelicula': 'Iron Man', 'estado': 'Dañado'},
    {'modelo': 'Mark V', 'pelicula': 'Iron Man 2', 'estado': 'Destruido'},
    {'modelo': 'Mark XLII', 'pelicula': 'Iron Man 3', 'estado': 'Dañado'},
    {'modelo': 'Mark XLIV', 'pelicula': 'Avengers: Age of Ultron', 'estado': 'Dañado'},
    {'modelo': 'Mark XLVI', 'pelicula': 'Captain America: Civil War', 'estado': 'Impecable'},
    {'modelo': 'Mark XLVII', 'pelicula': 'Spider-Man: Homecoming', 'estado': 'Impecable'},
    {'modelo': 'Mark L', 'pelicula': 'Avengers: Infinity War', 'estado': 'Impecable'},
    {'modelo': 'Mark LXXXV', 'pelicula': 'Avengers: Endgame', 'estado': 'Destruido'},
]

for traje in trajes:
    stack_trajes.push(traje)

# A) 
def buscar_hulkbuster(stack):
    aux = Stack()
    peliculas = set()
    while stack.size() > 0:
        traje = stack.pop()
        if traje['modelo'] == 'Mark XLIV':
            peliculas.add(traje['pelicula'])
        aux.push(traje)
    while aux.size() > 0:
        stack.push(aux.pop())
    return peliculas

# B) 
def mostrar_danados(stack):
    aux = Stack()
    print("Trajes dañados:")
    while stack.size() > 0:
        traje = stack.pop()
        if traje['estado'] == 'Dañado':
            print(traje)
        aux.push(traje)
    while aux.size() > 0:
        stack.push(aux.pop())

# C) 
def eliminar_destruidos(stack):
    aux = Stack()
    print("Eliminando trajes destruidos:")
    while stack.size() > 0:
        traje = stack.pop()
        if traje['estado'] == 'Destruido':
            print(traje)
        else:
            aux.push(traje)
    while aux.size() > 0:
        stack.push(aux.pop())

# D)
def agregar_sin_repetidos(stack, nuevo_traje):
    aux = Stack()
    repetido = False
    while stack.size() > 0:
        traje = stack.pop()
        if traje['modelo'] == nuevo_traje['modelo'] and traje['pelicula'] == nuevo_traje['pelicula']:
            repetido = True
        aux.push(traje)
    while aux.size() > 0:
        stack.push(aux.pop())
    if not repetido:
        stack.push(nuevo_traje)
        print("Modelo agregado correctamente.")
    else:
        print("Ya existe ese modelo en esa película, no se agregó.")
# E)
def mostrar_trajes_de_peliculas(stack, peliculas_objetivo):
    aux = Stack()
    print("Modelos utilizados en películas seleccionadas:")
    while stack.size() > 0:
        traje = stack.pop()
        if traje['pelicula'] in peliculas_objetivo:
            print(traje['modelo'])
        aux.push(traje)
    while aux.size() > 0:
        stack.push(aux.pop())



# F)
peliculas_hulkbuster = buscar_hulkbuster(stack_trajes)
if peliculas_hulkbuster:
    print("a) Mark XLIV fue usado en:")
    for p in peliculas_hulkbuster:
        print(f"- {p}")
else:
    print("a) Mark XLIV no fue encontrado.")

print()


print("b)")
mostrar_danados(stack_trajes)
print()


print("c)")
eliminar_destruidos(stack_trajes)
print()


print("e)")
nuevo_traje = {'modelo': 'Mark LXXXV', 'pelicula': 'Avengers: Endgame', 'estado': 'Impecable'}
agregar_sin_repetidos(stack_trajes, nuevo_traje)
print()


print("f)")
mostrar_trajes_de_peliculas(stack_trajes, ["Spider-Man: Homecoming", "Captain America: Civil War"])





