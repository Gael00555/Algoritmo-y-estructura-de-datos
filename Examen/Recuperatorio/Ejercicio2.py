from typing import Any, Optional
from Superheroes import superheroes


class Queue:

    def __init__(self):
        self.__elementos = []

    def llegar(self, valor: Any) -> None:
        self.__elementos.append(valor)

    def atender(self) -> Optional[Any]:
        return self.__elementos.pop(0) if self.__elementos else None

    def tamaño(self) -> int:
        return len(self.__elementos)

    def en_frente(self) -> Optional[Any]:
        return self.__elementos[0] if self.__elementos else None

    def mover_al_final(self):
        if self.__elementos:
            valor = self.atender()
            self.llegar(valor)
            return valor

    def mostrar(self):
        for elemento in self.__elementos:
            print(elemento)


class List(list):

    FUNCIONES_CRITERIOS = {}

    def agregar_criterio(self, clave_criterio: str, funcion):
        self.FUNCIONES_CRITERIOS[clave_criterio] = funcion

    def mostrar(self) -> None:
        for elemento in self:
            print(elemento)

    def mostrar_lista_de_listas(self) -> None:
        for elemento in self:
            print(elemento)
            print("Películas:")
            elemento.movie.mostrar()

    def borrar_valor(self, valor, clave_valor: str = None) -> Optional[Any]:
        indice = self.buscar(valor, clave_valor)
        return self.pop(indice) if indice is not None else None

    def insertar_valor(self, valor: Any) -> None:
        self.append(valor)

    def ordenar_por_criterio(self, clave_criterio: str = None) -> None:
        funcion_criterio = self.FUNCIONES_CRITERIOS.get(clave_criterio)
        if funcion_criterio is not None:
            self.sort(key=funcion_criterio)
        elif self and isinstance(self[0], (int, str, bool)):
            self.sort()
        else:
            print("Criterio de orden no encontrado.")

    def buscar(self, valor_busqueda, clave_busqueda: str = None) -> Optional[int]:
        self.ordenar_por_criterio(clave_busqueda)
        inicio = 0
        fin = len(self) - 1

        while inicio <= fin:
            medio = (inicio + fin) // 2
            funcion_criterio = self.FUNCIONES_CRITERIOS.get(clave_busqueda)

            if funcion_criterio is None and self and not isinstance(self[0], (int, str, bool)):
                return None

            valor_actual = funcion_criterio(self[medio]) if funcion_criterio else self[medio]

            if valor_actual == valor_busqueda:
                return medio
            elif valor_actual < valor_busqueda:
                inicio = medio + 1
            else:
                fin = medio - 1
        return None


class Superheroe:
    def __init__(self, nombre, nombre_real, primera_aparicion, biografia_corta=None, es_villano=False):
        self.nombre = nombre
        self.nombre_real = nombre_real
        self.primera_aparicion = primera_aparicion
        self.biografia_corta = biografia_corta
        self.es_villano = es_villano

    def __str__(self):
        return f"{self.nombre} ({self.nombre_real}) - {self.primera_aparicion}"


def ordenar_por_nombre(item):
    return item.nombre


def ordenar_por_nombre_real(item):
    return item.nombre_real if item.nombre_real is not None else ""


def ordenar_por_primera_aparicion(item):
    return item.primera_aparicion


lista_superheroes = List([
    Superheroe(
        nombre=heroe["name"],
        nombre_real=heroe["real_name"],
        primera_aparicion=heroe["first_appearance"],
        biografia_corta=heroe["short_bio"],
        es_villano=heroe["is_villain"],
    )
    for heroe in superheroes
])

lista_superheroes.agregar_criterio("nombre", ordenar_por_nombre)
lista_superheroes.agregar_criterio("nombre_real", ordenar_por_nombre_real)
lista_superheroes.agregar_criterio("primera_aparicion", ordenar_por_primera_aparicion)

print("a) Listado ordenado por nombre:")
lista_superheroes.ordenar_por_criterio("nombre")
lista_superheroes.mostrar()

pos_thing = lista_superheroes.buscar("The Thing", "nombre")
pos_rocket = lista_superheroes.buscar("Rocket Raccoon", "nombre")
print("\nb)")
print(f"La posición de The Thing es: {pos_thing}")
print(f"La posición de Rocket Raccoon es: {pos_rocket}")

villanos = List()
for heroe in lista_superheroes:
    if heroe.es_villano:
        villanos.append(heroe)

print("\nc) Villanos en la lista:")
villanos.mostrar()

cola_villanos = Queue()
for villano in villanos:
    cola_villanos.llegar(villano)

print("\nd) Villanos que aparecieron antes de 1980:")
while cola_villanos.tamaño() > 0:
    villano = cola_villanos.atender()
    if villano.primera_aparicion < 1980:
        print(f"{villano.nombre} ({villano.primera_aparicion})")

prefijos = ("Bl", "G", "My", "W")
superheroes_filtrados = List()
for heroe in lista_superheroes:
    if heroe.nombre.startswith(prefijos):
        superheroes_filtrados.append(heroe)

print("\ne) Superhéroes que comienzan con Bl, G, My y W:")
superheroes_filtrados.mostrar()

print("\nf) Listado ordenado por nombre real:")
lista_superheroes.ordenar_por_criterio("nombre_real")
lista_superheroes.mostrar()

print("\ng) Listado ordenado por fecha de aparición:")
lista_superheroes.ordenar_por_criterio("primera_aparicion")
lista_superheroes.mostrar()

pos_antman = lista_superheroes.buscar("Ant Man", "nombre")
if pos_antman is not None:
    lista_superheroes[pos_antman].nombre_real = "Scott Lang"
    print("\nh) Modificación del nombre real de Ant Man:")
    print(lista_superheroes[pos_antman])

print("\ni) Personajes con 'time-traveling' o 'suit' en su biografía:")
for heroe in lista_superheroes:
    if heroe.biografia_corta:
        bio = heroe.biografia_corta.lower()
        if "time-traveling" in bio or "suit" in bio:
            print(f"- {heroe.nombre}")

lista_eliminados = List()
nombres_a_eliminar = ["Electro", "Baron Zemo"]
for nombre in nombres_a_eliminar:
    pos = lista_superheroes.buscar(nombre, "nombre")
    if pos is not None:
        eliminado = lista_superheroes.pop(pos)
        lista_eliminados.append(eliminado)

print("\nj) Personajes eliminados:")
lista_eliminados.mostrar()