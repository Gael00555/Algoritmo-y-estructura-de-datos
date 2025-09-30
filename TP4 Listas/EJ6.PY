
from List import List


class Superhero:
    def __init__(self, name, year, house, biography):
        self.name = name
        self.year = year
        self.house = house
        self.biography = biography

    def __str__(self):
        return (
            f"Nombre: {self.name}\n"
            f"Año: {self.year}\n"
            f"Casa: {self.house}\n"
            f"Biografía: {self.biography}\n"
        )



superhero_list = List()
superhero_list.add_criterion("name", lambda sh: sh.name)
superhero_list.add_criterion("year", lambda sh: sh.year)
superhero_list.add_criterion("house", lambda sh: sh.house)
superhero_list.add_criterion("biography", lambda sh: sh.biography)


superhero_list.extend(
    [
        Superhero("Linterna Verde", 1940, "DC", "Posee un anillo de poder y viste un traje especial."),
        Superhero("Wolverine", 1974, "Marvel", "Tiene garras retráctiles y factor de curación."),
        Superhero("Dr. Strange", 1963, "DC", "Usa magia y viste una túnica."),
        Superhero("Iron Man", 1963, "Marvel", "Tony Stark usa una armadura de alta tecnología."),
        Superhero("Capitana Marvel", 1968, "Marvel", "Tiene poderes cósmicos y un traje especial."),
        Superhero("Mujer Maravilla", 1941, "DC", "Princesa amazona con traje de batalla."),
        Superhero("Flash", 1940, "DC", "Corre a velocidades increíbles."),
        Superhero("Star-Lord", 1976, "Marvel", "Usa una máscara y armadura espacial."),
        Superhero("Batman", 1939, "DC", "Lucha contra el crimen con traje de murciélago."),
        Superhero("Spider-Man", 1962, "Marvel", "Lleva un traje rojo y azul."),
        Superhero("Magneto", 1963, "Marvel", "Controla el magnetismo y usa casco y armadura."),
        Superhero("Superman", 1938, "DC", "Traje azul con capa roja."),
    ]
)


def delete_green_lantern(lista: List):
    removed = lista.delete_value("Linterna Verde", "name")
    if removed is None:
        print("a) Linterna Verde no encontrada.")
    else:
        print("a) Linterna Verde eliminada.\n")

print("---- a) ----")
delete_green_lantern(superhero_list)
superhero_list.show()  # muestro la lista resultante



def year_wolverine(lista: List):
    index = lista.search("Wolverine", "name")
    if index is not None:
        print(f"\n---- b) ----\nWolverine apareció en el año {lista[index].year}.")
    else:
        print("\n---- b) ----\nNo se encontró a Wolverine.")

year_wolverine(superhero_list)



def change_house(lista: List, hero_name: str, new_house: str = "Marvel"):
    index = lista.search(hero_name, "name")
    if index is not None:
        lista[index].house = new_house
        print(f"\n---- c) ----\nSe cambió la casa de {hero_name} a {new_house}.")
    else:
        print(f"\n---- c) ----\n{hero_name} no encontrado.")

change_house(superhero_list, "Dr. Strange", "Marvel")
# muestro Dr. Strange para confirmar
idx = superhero_list.search("Dr. Strange", "name")
if idx is not None:
    print(superhero_list[idx])



def show_suit_armor(lista: List):
    print("---- d) ----")
    found = False
    for hero in lista:
        bio = hero.biography.lower()
        if "traje" in bio or "armadura" in bio:
            print("-", hero.name)
            found = True
    if not found:
        print("No se encontraron biografías con 'traje' o 'armadura'.")

show_suit_armor(superhero_list)




def show_before_1963(lista: List):
    print("\n---- e) ----")
    found = False
    for hero in lista:
        if hero.year < 1963:
            print(f"- {hero.name} -> {hero.house} (Año: {hero.year})")
            found = True
    if not found:
        print("No hay superhéroes anteriores a 1963.")

show_before_1963(superhero_list)


def show_house(lista: List, superhero: str):
    index = lista.search(superhero, "name")
    if index is not None:
        return lista[index].house
    return None

print("\n---- f) ----")
cm_house = show_house(superhero_list, "Capitana Marvel")
mm_house = show_house(superhero_list, "Mujer Maravilla")
print(f"Capitana Marvel - casa: {cm_house if cm_house else 'no encontrada'}")
print(f"Mujer Maravilla - casa: {mm_house if mm_house else 'no encontrada'}")



def show_data(lista: List, superhero: str):
    index = lista.search(superhero, "name")
    if index is not None:
        return lista[index]
    return None

print("\n---- g) ----")
flash = show_data(superhero_list, "Flash")
starlord = show_data(superhero_list, "Star-Lord")
print(flash if flash else "Flash no encontrado.")
print()
print(starlord if starlord else "Star-Lord no encontrado.")



def list_by_initial(lista: List):
    print("\n---- h) ----")
    for hero in lista:
        if hero.name.startswith(("B", "M", "S")):
            print("-", hero.name)

list_by_initial(superhero_list)



def count_by_house(lista: List):
    conteo = {}
    for hero in lista:
        conteo[hero.house] = conteo.get(hero.house, 0) + 1
    return conteo

print("\n---- i) ----")
counts = count_by_house(superhero_list)
for casa, cantidad in counts.items():
    print(f"Cantidad {casa}: {cantidad}")
