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

def cargar_personajes():
    stack = Stack()
    personajes = [
        {'name': 'Iron Man', 'movies': 10},
        {'name': 'Captain America', 'movies': 9},
        {'name': 'Thor', 'movies': 8},
        {'name': 'Black Widow', 'movies': 7},
        {'name': 'Hulk', 'movies': 6},
        {'name': 'Hawkeye', 'movies': 5},
        {'name': 'Groot', 'movies': 4},
        {'name': 'Doctor Strange', 'movies': 5},
        {'name': 'Gamora', 'movies': 4},
        {'name': 'Rocket Raccoon', 'movies': 4},
        {'name': 'Drax', 'movies': 4},
        {'name': 'Captain Marvel', 'movies': 3},
    ]
    for p in personajes:
        stack.push(p)
    return stack

def posiciones(stack, nombres):
    aux = Stack()
    posiciones = {}
    pos = 1
    while stack.size() > 0:
        p = stack.pop()
        if p['name'] in nombres:
            posiciones[p['name']] = pos
        aux.push(p)
        pos += 1
    while aux.size() > 0:
        stack.push(aux.pop())
    return posiciones

def mas_de_n_peliculas(stack, n):
    aux = Stack()
    resultado = []
    while stack.size() > 0:
        p = stack.pop()
        if p['movies'] > n:
            resultado.append(p)
        aux.push(p)
    while aux.size() > 0:
        stack.push(aux.pop())
    return resultado

def contar_peliculas(stack, nombre):
    aux = Stack()
    cantidad = 0
    while stack.size() > 0:
        p = stack.pop()
        if p['name'] == nombre:
            cantidad = p['movies']
        aux.push(p)
    while aux.size() > 0:
        stack.push(aux.pop())
    return cantidad

def nombres_por_inicial(stack, iniciales):
    aux = Stack()
    seleccionados = []
    while stack.size() > 0:
        p = stack.pop()
        if p['name'].startswith(tuple(iniciales)):
            seleccionados.append(p['name'])
        aux.push(p)
    while aux.size() > 0:
        stack.push(aux.pop())
    return seleccionados

stack_mcu = cargar_personajes()

print("a) Posiciones de Rocket Raccoon y Groot desde la cima:")
resultado_a = posiciones(stack_mcu, ["Rocket Raccoon", "Groot"])
for nombre in ["Rocket Raccoon", "Groot"]:
    print(f"{nombre}: posición {resultado_a.get(nombre, 'no encontrado')}")

print("\nb) Personajes que participaron en más de 5 películas:")
resultado_b = mas_de_n_peliculas(stack_mcu, 5)
for p in resultado_b:
    print(f"{p['name']}: {p['movies']} películas")

print("\nc) Películas en las que participó Black Widow:")
resultado_c = contar_peliculas(stack_mcu, "Black Widow")
print(f"Black Widow participó en {resultado_c} películas")

print("\nd) Personajes cuyos nombres empiezan con C, D o G:")
resultado_d = nombres_por_inicial(stack_mcu, ["C", "D", "G"])
for nombre in resultado_d:
    print(nombre)

