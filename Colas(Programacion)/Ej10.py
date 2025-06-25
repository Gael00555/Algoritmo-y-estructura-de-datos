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

class Stack:
    def __init__(self):
        self.__elements = []

    def push(self, value: Any) -> None:
        self.__elements.append(value)

    def pop(self) -> Optional[Any]:
        return self.__elements.pop() if self.__elements else None

    def size(self) -> int:
        return len(self.__elements)

    def on_top(self) -> Optional[Any]:
        return self.__elements[-1] if self.__elements else None

    def show(self):
        aux_stack = Stack()
        while self.size() > 0:
            value = self.pop()
            print(value)
            aux_stack.push(value)
        while aux_stack.size() > 0:
            self.push(aux_stack.pop())


notificaciones = Queue()


datos = [
    {'hora': '10:15', 'app': 'Facebook', 'mensaje': 'Nuevo comentario en tu foto'},
    {'hora': '11:45', 'app': 'Twitter', 'mensaje': 'Python es genial'},
    {'hora': '12:30', 'app': 'Instagram', 'mensaje': 'Nuevo seguidor'},
    {'hora': '13:00', 'app': 'Twitter', 'mensaje': '¡Mirá este hilo de Python!'},
    {'hora': '14:15', 'app': 'Facebook', 'mensaje': 'Tienes recuerdos hoy'},
    {'hora': '15:55', 'app': 'WhatsApp', 'mensaje': '¿Vamos al cine?'},
    {'hora': '16:00', 'app': 'Twitter', 'mensaje': 'Sin mención a Python'},
]

for d in datos:
    notificaciones.arrive(d)

def eliminar_facebook(queue):
    aux = Queue()
    while queue.size() > 0:
        n = queue.attention()
        if n['app'] != 'Facebook':
            aux.arrive(n)
    while aux.size() > 0:
        queue.arrive(aux.attention())


def mostrar_twitter_python(queue):
    aux = Queue()
    print("Notificaciones de Twitter con 'Python':")
    while queue.size() > 0:
        n = queue.attention() 
        if n['app'] == 'Twitter' and 'Python' in n['mensaje']:
            print(n)
        aux.arrive(n)
    while aux.size() > 0:
        queue.arrive(aux.attention())


def notificaciones_en_rango(queue, hora_min, hora_max):
    aux = Queue()
    pila = Stack()
    for _ in range(queue.size()):
        n = queue.attention()
        if hora_min <= n['hora'] <= hora_max:
            pila.push(n)
        aux.arrive(n)
    while aux.size() > 0:
        queue.arrive(aux.attention())
    return pila


print("Cola original:")
notificaciones.show()
print("\nA) Eliminar notificaciones de Facebook:")
eliminar_facebook(notificaciones)
notificaciones.show()

print("\nB) Mostrar notificaciones de Twitter con 'Python':")
mostrar_twitter_python(notificaciones)

print("\nC) Notificaciones entre 11:43 y 15:57:")
pila = notificaciones_en_rango(notificaciones, '11:43', '15:57')
print(f"Cantidad de notificaciones en rango: {pila.size()}")
pila.show()
