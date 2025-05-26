class Cola:
    def __init__(self):
        self.items = []

    def encolar(self, item):
        self.items.append(item)

    def desencolar(self):
        if not self.esta_vacia():
            return self.items.pop(0)

    def esta_vacia(self):
        return len(self.items) == 0

    def tamano(self):
        return len(self.items)

    def ver_primero(self):
        if not self.esta_vacia():
            return self.items[0]
        
class Pila:
    def __init__(self):
        self.items = []

    def apilar(self, item):
        self.items.append(item)

    def desapilar(self):
        if not self.esta_vacia():
            return self.items.pop()

    def esta_vacia(self):
        return len(self.items) == 0

    def tamano(self):
        return len(self.items)

    def ver_tope(self):
        if not self.esta_vacia():
            return self.items[-1]


def hora_en_minutos(hora_str):
    h, m = map(int, hora_str.split(':'))
    return h * 60 + m


def eliminar_facebook(cola):
    aux = Cola()
    while not cola.esta_vacia():
        notif = cola.desencolar()
        if notif['aplicacion'].lower() != 'facebook':
            aux.encolar(notif)
    while not aux.esta_vacia():
        cola.encolar(aux.desencolar())


def mostrar_twitter_python(cola):
    aux = Cola()
    while not cola.esta_vacia():
        notif = cola.desencolar()
        if notif['aplicacion'].lower() == 'twitter' and 'python' in notif['mensaje'].lower():
            print(notif)
        aux.encolar(notif)
    while not aux.esta_vacia():
        cola.encolar(aux.desencolar())


def notificaciones_en_rango(cola, hora_inicio, hora_fin):
    pila = Pila()
    aux = Cola()
    inicio = hora_en_minutos(hora_inicio)
    fin = hora_en_minutos(hora_fin)

    while not cola.esta_vacia():
        notif = cola.desencolar()
        hora_min = hora_en_minutos(notif['hora'])
        if inicio <= hora_min <= fin:
            pila.apilar(notif)
        aux.encolar(notif)

    while not aux.esta_vacia():
        cola.encolar(aux.desencolar())

    return pila.tamano()


cola_notificaciones = Cola()
notificaciones = [
    {'hora': '11:45', 'aplicacion': 'Twitter', 'mensaje': 'Python es genial'},
    {'hora': '12:30', 'aplicacion': 'Facebook', 'mensaje': 'Nuevo comentario'},
    {'hora': '13:00', 'aplicacion': 'Instagram', 'mensaje': 'Nueva historia'},
    {'hora': '14:50', 'aplicacion': 'Twitter', 'mensaje': 'Aprendé Python hoy'},
    {'hora': '16:10', 'aplicacion': 'Facebook', 'mensaje': 'Nuevo amigo'},
    {'hora': '10:30', 'aplicacion': 'Twitter', 'mensaje': 'Buenos días'},
]

for notif in notificaciones:
    cola_notificaciones.encolar(notif)


print(">>> Notificaciones de Twitter que contienen 'Python':")
mostrar_twitter_python(cola_notificaciones)


print("\n>>> Eliminando notificaciones de Facebook...")
eliminar_facebook(cola_notificaciones)


print("\n>>> Cantidad de notificaciones entre 11:43 y 15:57:")
cantidad = notificaciones_en_rango(cola_notificaciones, '11:43', '15:57')
print("Cantidad:", cantidad)