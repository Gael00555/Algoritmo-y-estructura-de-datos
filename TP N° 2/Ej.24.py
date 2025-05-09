
class nodoPila:
    def __init__(self, info):
        self.info = info
        self.sig = None

class pila:
    def __init__(self):
        self.cima = None
        self.tamanio = 0

def apilar(p, dato):
    nodo = nodoPila(dato)
    nodo.sig = p.cima
    p.cima = nodo
    p.tamanio += 1

def desapilar(p):
    if p.cima is not None:
        dato = p.cima.info
        p.cima = p.cima.sig
        p.tamanio -= 1
        return dato

def pila_vacia(p):
    return p.cima is None

def copiar_pila(p):
    aux = pila()
    copia = pila()
    while not pila_vacia(p):
        dato = desapilar(p)
        apilar(aux, dato)
    while not pila_vacia(aux):
        dato = desapilar(aux)
        apilar(p, dato)
        apilar(copia, dato)
    return copia

def buscar_posiciones(p, nombres_objetivo):
    copia = copiar_pila(p)
    posicion = 1
    posiciones = {}
    while not pila_vacia(copia):
        personaje = desapilar(copia)
        if personaje['nombre'] in nombres_objetivo and personaje['nombre'] not in posiciones:
            posiciones[personaje['nombre']] = posicion
        posicion += 1

    for nombre in nombres_objetivo:
        if nombre in posiciones:
            print(f"{nombre} está en la posición {posiciones[nombre]} desde la cima de la pila.")
        else:
            print(f"{nombre} no se encuentra en la pila.")

# Función para determinar personajes con más de 5 películas
def personajes_mas_de_5(p):
    copia = copiar_pila(p)
    print("\nPersonajes que participaron en más de 5 películas:")
    while not pila_vacia(copia):
        personaje = desapilar(copia)
        if personaje['peliculas'] > 5:
            print(f"- {personaje['nombre']} participó en {personaje['peliculas']} películas.")

# Función para contar en cuántas películas participó Black Widow
def peliculas_black_widow(p):
    copia = copiar_pila(p)
    while not pila_vacia(copia):
        personaje = desapilar(copia)
        if personaje['nombre'] == 'Black Widow':
            print(f"Black Widow participó en {personaje['peliculas']} películas.")
            return
    print("Black Widow no se encuentra en la pila.")

# Función para mostrar personajes cuyos nombres empiezan con C, D y G
def personajes_iniciales_cd_g(p):
    copia = copiar_pila(p)
    print("\nPersonajes cuyos nombres empiezan con C, D y G:")
    while not pila_vacia(copia):
        personaje = desapilar(copia)
        if personaje['nombre'][0] in ['C', 'D', 'G']:
            print(f"- {personaje['nombre']} participó en {personaje['peliculas']} películas.")


p = pila()
apilar(p, {'nombre': 'Iron Man', 'peliculas': 10})
apilar(p, {'nombre': 'Captain America', 'peliculas': 9})
apilar(p, {'nombre': 'Black Widow', 'peliculas': 8})
apilar(p, {'nombre': 'Hulk', 'peliculas': 7})
apilar(p, {'nombre': 'Thor', 'peliculas': 8})
apilar(p, {'nombre': 'Hawkeye', 'peliculas': 6})
apilar(p, {'nombre': 'Doctor Strange', 'peliculas': 3})
apilar(p, {'nombre': 'Spider-Man', 'peliculas': 5})
apilar(p, {'nombre': 'Black Panther', 'peliculas': 4})
apilar(p, {'nombre': 'Ant-Man', 'peliculas': 4})
apilar(p, {'nombre': 'Rocket Raccoon', 'peliculas': 4})
apilar(p, {'nombre': 'Groot', 'peliculas': 4})
apilar(p, {'nombre': 'Scarlet Witch', 'peliculas': 5})

# Buscar Rocket Raccoon y Groot
buscar_posiciones(p, ['Rocket Raccoon', 'Groot'])

# Determinar personajes con más de 5 películas
personajes_mas_de_5(p)

# Determinar cuántas películas participó Black Widow
peliculas_black_widow(p)

# Mostrar personajes cuyos nombres empiezan con C, D y G
personajes_iniciales_cd_g(p)