from List import List  


class Jedi:
    def __init__(self, name, masters, sabers, species):
        self.name = name
        self.masters = masters          
        self.sabers = sabers            
        self.species = species

    def __str__(self):
        return (
            f"Nombre: {self.name}\n"
            f"Maestros: {', '.join(self.masters) if self.masters else 'Ninguno'}\n"
            f"Colores sables: {', '.join(self.sabers)}\n"
            f"Especie: {self.species}\n"
        )



jedi_list = List()


jedi_list.add_criterion("name", lambda j: j.name)
jedi_list.add_criterion("species", lambda j: j.species)


jedi_list.extend([
    Jedi("Ahsoka Tano", ["Anakin Skywalker"], ["Verde", "Azul", "Blanco"], "Togruta"),
    Jedi("Kit Fisto", ["Yoda"], ["Verde"], "Nautolano"),
    Jedi("Yoda", [], ["Verde"], "Desconocida"),
    Jedi("Luke Skywalker", ["Obi-Wan Kenobi", "Yoda"], ["Verde", "Azul"], "Humano"),
    Jedi("Qui-Gon Jin", ["Conde Dooku"], ["Verde"], "Humano"),
    Jedi("Mace Windu", ["Cyslin Myr"], ["Violeta"], "Humano"),
    Jedi("Obi-Wan Kenobi", ["Qui-Gon Jin"], ["Azul"], "Humano"),
    Jedi("Anakin Skywalker", ["Obi-Wan Kenobi"], ["Azul"], "Humano"),
    Jedi("Rey", ["Leia Organa", "Luke Skywalker"], ["Amarillo"], "Humano"),
    Jedi("Aayla Secura", ["Quinlan Vos"], ["Azul"], "Twi'lek"),
])



def list_sorted(lista, criterion):
    lista.sort_by_criterion(criterion)
    lista.show()

def show_info(lista, names):
    for name in names:
        idx = lista.search(name, "name")
        if idx is not None:
            print(lista[idx])

def show_padawans(lista, masters):
    for jedi in lista:
        for m in masters:
            if m in jedi.masters:
                print(f"{jedi.name} fue aprendiz de {m}")


def show_by_species(lista):
    for jedi in lista:
        if jedi.species.lower() in ["humano", "twi'lek"]:
            print(jedi.name, "-", jedi.species)



def show_starting_with_a(lista):
    for jedi in lista:
        if jedi.name.startswith("A"):
            print(jedi.name)


def show_multiple_sabers(lista):
    for jedi in lista:
        if len(jedi.sabers) > 1:
            print(jedi.name, "-", jedi.sabers)


def show_specific_saber(lista):
    for jedi in lista:
        if "Amarillo" in jedi.sabers or "Violeta" in jedi.sabers:
            print(jedi.name, "-", jedi.sabers)


def show_padawans_of(lista, masters):
    for jedi in lista:
        for m in masters:
            if m in jedi.masters:
                print(f"{jedi.name} fue aprendiz de {m}")




print("a) Listado por nombre")
list_sorted(jedi_list, "name")

print("\n---\na) Listado por especie")
list_sorted(jedi_list, "species")

print("\n---\nb) Info Ahsoka y Kit Fisto")
show_info(jedi_list, ["Ahsoka Tano", "Kit Fisto"])

print("\n---\nc) Padawans de Yoda y Luke")
show_padawans(jedi_list, ["Yoda", "Luke Skywalker"])

print("\n---\nd) Humanos y Twi'lek")
show_by_species(jedi_list)

print("\n---\ne) Jedi con A")
show_starting_with_a(jedi_list)

print("\n---\nf) Jedi con más de un sable")
show_multiple_sabers(jedi_list)

print("\n---\ng) Jedi con sable amarillo o violeta")
show_specific_saber(jedi_list)

print("\n---\nh) Padawans de Qui-Gon Jin y Mace Windu")
show_padawans_of(jedi_list, ["Qui-Gon Jin", "Mace Windu"])


