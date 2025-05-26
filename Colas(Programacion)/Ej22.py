class nodoCola(object):
    def __init__(self):
        self.info = None
        self.sig = None

class Cola(object):
    def __init__(self):
        self.frente = None
        self.final = None
        self.tamanio = 0

def arribo(cola, dato):
    nodo = nodoCola()
    nodo.info = dato
    if cola.final is not None:
        cola.final.sig = nodo
    else:
        cola.frente = nodo
    cola.final = nodo
    cola.tamanio += 1

def atencion(cola):
    dato = cola.frente.info
    cola.frente = cola.frente.sig
    if cola.frente is None:
        cola.final = None
    cola.tamanio -= 1
    return dato

def cola_vacia(cola):
    return cola.frente is None

def en_frente(cola):
    return cola.frente.info

# Carga de datos de ejemplo
cola_mcu = Cola()
personajes = [
    {"nombre": "Tony Stark", "superheroe": "Iron Man", "genero": "M"},
    {"nombre": "Steve Rogers", "superheroe": "Capitán América", "genero": "M"},
    {"nombre": "Natasha Romanoff", "superheroe": "Black Widow", "genero": "F"},
    {"nombre": "Carol Danvers", "superheroe": "Capitana Marvel", "genero": "F"},
    {"nombre": "Scott Lang", "superheroe": "Ant-Man", "genero": "M"},
    {"nombre": "Stephen Strange", "superheroe": "Doctor Strange", "genero": "M"},
    {"nombre": "Sam Wilson", "superheroe": "Falcon", "genero": "M"}
]

for p in personajes:
    arribo(cola_mcu, p)

# Procesamiento según lo pedido
def procesar_actividades(cola):
    print("Procesando personajes del MCU...\n")
    cola_aux = Cola()
    capitana_marvel_encontrada = False
    carol_danvers_encontrado = False

    while not cola_vacia(cola):
        personaje = atencion(cola)
        
        
        if personaje["superheroe"] == "Capitana Marvel":
            print(f" El nombre real de Capitana Marvel es: {personaje['nombre']}")
            capitana_marvel_encontrada = True


        if personaje["genero"] == "F":
            print(f" Superhéroe femenino encontrado: {personaje['superheroe']}")

       
        if personaje["genero"] == "M":
            print(f" Personaje masculino encontrado: {personaje['nombre']}")

        
        if personaje["nombre"] == "Scott Lang":
            print(f" El superhéroe de Scott Lang es: {personaje['superheroe']}")

        
        if personaje["nombre"].startswith("S") or personaje["superheroe"].startswith("S"):
            print(f" Personaje con nombre o superhéroe que comienza con S: {personaje}")

        
        if personaje["nombre"] == "Carol Danvers":
            print(f" Carol Danvers está en la cola. Su nombre de superhéroe es: {personaje['superheroe']}")
            carol_danvers_encontrado = True

        arribo(cola_aux, personaje)

    
    while not cola_vacia(cola_aux):
        arribo(cola, atencion(cola_aux))

    if not capitana_marvel_encontrada:
        print("A. Capitana Marvel no se encuentra en la cola.")
    if not carol_danvers_encontrado:
        print("F. Carol Danvers no se encuentra en la cola.")

procesar_actividades(cola_mcu) 