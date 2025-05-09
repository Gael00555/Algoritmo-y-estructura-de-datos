
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

def mostrar_traje(traje):
    print(f"- {traje['modelo']} ({traje['pelicula']}) - Estado: {traje['estado']}")

def cargar_datos(p):
    datos = [
        {'modelo': 'Mark III', 'pelicula': 'Iron Man', 'estado': 'Dañado'},
        {'modelo': 'Mark XLIV', 'pelicula': 'Avengers: Age of Ultron', 'estado': 'Dañado'},
        {'modelo': 'Mark XLII', 'pelicula': 'Iron Man 3', 'estado': 'Destruido'},
        {'modelo': 'Mark V', 'pelicula': 'Iron Man 2', 'estado': 'Impecable'},
        {'modelo': 'Mark XLIV', 'pelicula': 'Avengers: Endgame', 'estado': 'Impecable'},
        {'modelo': 'Mark XLVII', 'pelicula': 'Spider-Man: Homecoming', 'estado': 'Dañado'},
        {'modelo': 'Mark XLVI', 'pelicula': 'Capitan America: Civil War', 'estado': 'Impecable'},
        {'modelo': 'Mark L', 'pelicula': 'Avengers: Infinity War', 'estado': 'Destruido'},
    ]
    for traje in datos:
        apilar(p, traje)

# a) Buscar Mark XLIV
def buscar_mark_xliv(p):
    copia = copiar_pila(p)
    peliculas = []
    while not pila_vacia(copia):
        traje = desapilar(copia)
        if traje['modelo'] == 'Mark XLIV':
            peliculas.append(traje['pelicula'])
    if peliculas:
        print("Mark XLIV fue usado en:")
        for peli in peliculas:
            print(f"- {peli}")
    else:
        print("Mark XLIV no fue usado en ninguna película.")

# b) Mostrar modelos dañados
def modelos_daniados(p):
    copia = copiar_pila(p)
    daniados = []
    while not pila_vacia(copia):
        traje = desapilar(copia)
        if traje['estado'] == 'Dañado':
            daniados.append(traje)
    if daniados:
        print("Modelos dañados:")
        for t in daniados:
            mostrar_traje(t)
    else:
        print("No hay modelos dañados.")

# c) Eliminar destruidos
def eliminar_destruidos(p):
    aux = pila()
    destruidos = []
    while not pila_vacia(p):
        traje = desapilar(p)
        if traje['estado'] == 'Destruido':
            destruidos.append(traje)
        else:
            apilar(aux, traje)
    while not pila_vacia(aux):
        apilar(p, desapilar(aux))
    if destruidos:
        print("Modelos destruidos eliminados:")
        for t in destruidos:
            mostrar_traje(t)
    else:
        print("No había modelos destruidos.")

# e) Agregar Mark LXXXV si no está repetido
def agregar_mark_lxxxv(p):
    modelo = 'Mark LXXXV'
    pelicula = 'Avengers: Endgame'
    copia = copiar_pila(p)
    repetido = False
    while not pila_vacia(copia):
        traje = desapilar(copia)
        if traje['modelo'] == modelo and traje['pelicula'] == pelicula:
            repetido = True
            break
    if not repetido:
        apilar(p, {'modelo': modelo, 'pelicula': pelicula, 'estado': 'Impecable'})
        print("Se agregó Mark LXXXV (Avengers: Endgame).")
    else:
        print("Ya existía Mark LXXXV en Avengers: Endgame.")

# f) Trajes usados en 2 películas
def trajes_por_peliculas(p):
    peliculas_obj = ['Spider-Man: Homecoming', 'Capitan America: Civil War']
    copia = copiar_pila(p)
    encontrados = []
    while not pila_vacia(copia):
        traje = desapilar(copia)
        if traje['pelicula'] in peliculas_obj:
            encontrados.append(traje)
    if encontrados:
        print("Trajes en Spider-Man: Homecoming y Capitan America: Civil War:")
        for t in encontrados:
            mostrar_traje(t)
    else:
        print("No se encontraron trajes en esas películas.")

# (Opcional) Menú interactivo
def menu():
    p = pila()
    cargar_datos(p)

    while True:
        print("\n=== MENU ===")
        print("1. Buscar Mark XLIV")
        print("2. Mostrar modelos dañados")
        print("3. Eliminar modelos destruidos")
        print("4. Agregar Mark LXXXV")
        print("5. Mostrar trajes de Spider-Man: Homecoming y Civil War")
        print("6. Salir")

        opcion = input("Elija una opción: ")
        if opcion== '1':
            buscar_mark_xliv(p)
        elif opcion == '2':
            modelos_daniados(p)
        elif opcion == '3':
            eliminar_destruidos(p)
        elif opcion == '4':
            agregar_mark_lxxxv(p)
        elif opcion == '5':
            trajes_por_peliculas(p)
        elif opcion == '6':
            print("Saliendo...")
            break
        else:
            print("Opción inválida.")


menu()

