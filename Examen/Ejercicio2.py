from Superheroes import superheroes 



class Pila: 
    def __init__(self):
        self.elementos = []

    def apilar(self, dato):
        self.elementos.append(dato)

    def desapilar(self):
        if not self.esta_vacia():
            return self.elementos.pop()

    def esta_vacia(self):
        return len(self.elementos) == 0


class Cola: 
    def __init__(self):
        self.elementos = []

    def encolar(self, dato):
        self.elementos.append(dato)

    def desencolar(self):
        if not self.esta_vacia():
            return self.elementos.pop(0)

    def esta_vacia(self):
        return len(self.elementos) == 0

    def __iter__(self):
        return iter(self.elementos)


def ordenar_por_clave(lista, clave):
    lista = [x for x in lista if x.get(clave) is not None]  
    if len(lista) <= 1:
        return lista
    guia = lista[0]
    menores = [x for x in lista[1:] if x[clave] <= guia[clave]]
    mayores = [x for x in lista[1:] if x[clave] > guia[clave]]
    return ordenar_por_clave(menores, clave) + [guia] + ordenar_por_clave(mayores, clave)


def filtrar_por_prefijo(lista, prefijos, indice=0, resultado=None):
    if resultado is None:
        resultado = []
    if indice == len(lista):
        return resultado
    nombre = lista[indice].get("name", "")
    if any(nombre.startswith(prefijo) for prefijo in prefijos):
        resultado.append(lista[indice])
    return filtrar_por_prefijo(lista, prefijos, indice + 1, resultado)


personajes_ordenados = ordenar_por_clave(superheroes, "name")
print("1. Personajes ordenados por nombre:")
for personaje in personajes_ordenados:
    print("-", personaje["name"])


for i, personaje in enumerate(personajes_ordenados): 
    nombre = personaje.get("name", "")
    if nombre == "The Thing":
        print(f"\n2. The Thing está en la posición {i}")
    if nombre == "Rocket Raccoon":
        print(f"2. Rocket Raccoon está en la posición {i}")


villanos = [p for p in superheroes if p.get("is_villain")]
print("\n3. Villanos:")
for v in villanos:
    print("-", v["name"])


cola_villanos = Cola()
for v in villanos:
    cola_villanos.encolar(v)

print("\n4. Villanos que aparecieron antes de 1980:")
for v in cola_villanos: 
    if isinstance(v.get("first_appearance"), int) and v["first_appearance"] < 1980: 
        print("-", v["name"], f"({v['first_appearance']})") 


prefijos = ["Bl", "G", "My", "W"]
filtrados = filtrar_por_prefijo(superheroes, prefijos)
print("\n5. Superhéroes que comienzan con Bl, G, My o W:")
for f in filtrados:
    print("-", f["name"])


personajes_por_nombre_real = ordenar_por_clave(superheroes, "real_name")
print("\n6. Personajes ordenados por nombre real:")
for personaje in personajes_por_nombre_real:
    print("-", personaje["real_name"], "=>", personaje["name"])


personajes_por_aparicion = ordenar_por_clave(superheroes, "first_appearance")
print("\n7. Personajes ordenados por año de aparición:")
for personaje in personajes_por_aparicion:
    print("-", personaje["first_appearance"], "=>", personaje["name"])


for personaje in superheroes:
    if personaje.get("name") == "Ant Man":
        personaje["real_name"] = "Scott Lang"
        print("\n8. Ant Man actualizado:", personaje["real_name"])


print("\n9. Personajes con 'time-traveling' o 'suit' en su biografía:")
for personaje in superheroes:
    biografia = personaje.get("short_bio", "")
    if "time-traveling" in biografia.lower() or "suit" in biografia.lower():
        print("-", personaje["name"])


nombres_eliminar = ["Electro", "Baron Zemo"]
eliminados = []
restantes = []

for personaje in superheroes:
    if personaje.get("name") in nombres_eliminar:
        eliminados.append(personaje)
    else:
        restantes.append(personaje)

print("\n10. Personajes eliminados:")
for eliminado in eliminados:
    print("-", eliminado["name"], eliminado)


superheroes = restantes

