from typing import Any, Optional

class Queue:

    def __init__(self):
        self.__elements = []

    def arrive(self, value: Any) -> None:
        self.__elements.append(value)

    def attention(self) -> Optional[Any]:
        return self.__elements.pop(0) if self.__elements else None

    def on_front(self) -> Optional[Any]:
        return self.__elements[0] if self.__elements else None

    def size(self) -> int:
        return len(self.__elements)

    def move_to_end(self) -> Optional[Any]:
        if self.__elements:
            value = self.attention()
            self.arrive(value)
            return value

    def show(self):
        for i in range(len(self.__elements)):
            print(self.move_to_end())

mcu = Queue()
datos = [
    {'personaje': 'Tony Stark', 'superheroe': 'Iron Man', 'genero': 'M'},
    {'personaje': 'Steve Rogers', 'superheroe': 'Capitán América', 'genero': 'M'},
    {'personaje': 'Natasha Romanoff', 'superheroe': 'Black Widow', 'genero': 'F'},
    {'personaje': 'Carol Danvers', 'superheroe': 'Capitana Marvel', 'genero': 'F'},
    {'personaje': 'Wanda Maximoff', 'superheroe': 'Scarlet Witch', 'genero': 'F'},
    {'personaje': 'Scott Lang', 'superheroe': 'Ant-Man', 'genero': 'M'},
    {'personaje': 'Stephen Strange', 'superheroe': 'Doctor Strange', 'genero': 'M'},
    {'personaje': 'Sam Wilson', 'superheroe': 'Falcon', 'genero': 'M'},
]

for p in datos:
    mcu.arrive(p)



def buscar_personaje_por_superheroe(queue, nombre_heroe):
    aux = Queue()
    resultado = None
    while queue.size() > 0:
        dato = queue.attention()
        if dato['superheroe'] == nombre_heroe:
            resultado = dato['personaje']
        aux.arrive(dato)
    while aux.size() > 0:
        queue.arrive(aux.attention())
    return resultado

def mostrar_superheroes_femeninos(queue):
    aux = Queue()
    print("Superhéroes femeninos:")
    while queue.size() > 0:
        dato = queue.attention()
        if dato['genero'] == 'F':
            print(dato['superheroe'])
        aux.arrive(dato)
    while aux.size() > 0:
        queue.arrive(aux.attention())

def mostrar_personajes_masculinos(queue):
    aux = Queue()
    print("Personajes masculinos:")
    while queue.size() > 0:
        dato = queue.attention()
        if dato['genero'] == 'M':
            print(dato['personaje'])
        aux.arrive(dato)
    while aux.size() > 0:
        queue.arrive(aux.attention())

def buscar_superheroe_por_personaje(queue, nombre_personaje):
    aux = Queue()
    resultado = None
    while queue.size() > 0:
        dato = queue.attention()
        if dato['personaje'] == nombre_personaje:
            resultado = dato['superheroe']
        aux.arrive(dato)
    while aux.size() > 0:
        queue.arrive(aux.attention())
    return resultado

def mostrar_nombres_con_S(queue):
    aux = Queue()
    print("Datos cuyos nombres (personaje o superhéroe) empiezan con 'S':")
    while queue.size() > 0:
        dato = queue.attention()
        if dato['personaje'].startswith('S') or dato['superheroe'].startswith('S'):
            print(dato)
        aux.arrive(dato)
    while aux.size() > 0:
        queue.arrive(aux.attention())

def verificar_carol_danvers(queue):
    aux = Queue()
    encontrado = False
    heroe = None
    while queue.size() > 0:
        dato = queue.attention()
        if dato['personaje'] == 'Carol Danvers':
            encontrado = True
            heroe = dato['superheroe']
        aux.arrive(dato)
    while aux.size() > 0:
        queue.arrive(aux.attention())
    return encontrado, heroe



print("a) Nombre del personaje de la superhéroe 'Capitana Marvel':")
resultado_a = buscar_personaje_por_superheroe(mcu, "Capitana Marvel")
print(resultado_a)

print("\nb) Superhéroes femeninos:")
mostrar_superheroes_femeninos(mcu)

print("\nc) Personajes masculinos:")
mostrar_personajes_masculinos(mcu)

print("\nd) Nombre del superhéroe de Scott Lang:")
resultado_d = buscar_superheroe_por_personaje(mcu, "Scott Lang")
print(resultado_d)

print("\ne) Datos cuyos nombres comienzan con S:")
mostrar_nombres_con_S(mcu)

print("\nf) ¿Carol Danvers está en la cola?")
encontrado, heroe = verificar_carol_danvers(mcu)
if encontrado:
    print(f"Sí, su superhéroe es: {heroe}")
else:
    print("No se encontró a Carol Danvers.")

