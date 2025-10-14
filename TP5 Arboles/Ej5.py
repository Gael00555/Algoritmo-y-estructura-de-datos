from tree import BinaryTree
from super_heroes_data import superheroes

arbol_mcu = BinaryTree()

for super_heroes_data in superheroes:
    arbol_mcu.insert(super_heroes_data["name"], super_heroes_data)


    def villain_in_order(self):
        def __villain_in_order(root):
            if root is not None:
                __villain_in_order(root.left)
                if root.other_values["is_villain"] is True:
                    print(root.value)
                __villain_in_order(root.right)

        if self.root is not None:
            __villain_in_order(self.root)

print("b)Listado de villanos en orden alfabetico:")
villain_in_order(arbol_mcu)
    
def show_superheroes_with_c(self):
    def __show_superheroes_with_c(root):
        if root is not None:
            __show_superheroes_with_c(root.left)
            if root.value.startswith("C"):
              print(root.value)
            __show_superheroes_with_c(root.right)

    if self.root is not None:
        __show_superheroes_with_c(self.root)


print("c)Listado de superheroes que comienzan con la letra C:")
show_superheroes_with_c(arbol_mcu)

def count_heroes(self):
        def __count_heroes(root):
            count = 0
            if root is not None:
                if root.other_values["is_villain"] is False:
                    count += 1
                count += __count_heroes(root.left)
                count += __count_heroes(root.right)

            return count

        total = 0
        if self.root is not None:
            total = __count_heroes(self.root)
        
        return total

print("d)Cantidad de superheroes:", count_heroes(arbol_mcu))

def modify_Dr_Strange(self):
    print("e) Modificar 'Dr Strannnnnge' por 'Doctor Strange'")
    self.proximity_search('Dr')
    name = input('Ingrese nombre para modificar: ')
    value, other_value = self.delete(name)
    if value is not None:
        fix_name = input('Ingrese el nuevo nombre: ')
        other_value['name'] = fix_name
        self.insert(fix_name, other_value)
        print(f"\n{name} fue modificado a {fix_name}")
    else:
        print(f"\nNo se encontró el nombre {name} en el árbol.")
    print()
    self.proximity_search('Dr')
    print()
    pos = self.search(fix_name)
    if pos is not None:
        print(pos.value, pos.other_values)
modify_Dr_Strange(arbol_mcu)



def superheroes_post_order(self):
        def __post_order(root):
            if root is not None:
                __post_order(root.right)
                print(root.value)
                __post_order(root.left)

        if self.root is not None:
            __post_order(self.root)

print("f) Listado de forma  descendente de los superheroes: ")
superheroes_post_order(arbol_mcu)

def forest(self):
    heroes_tree = BinaryTree()
    villains_tree = BinaryTree()

    def __forest(root):
        if root is not None:
            __forest(root.left)
            if root.other_values["is_villain"] is True:
                villains_tree.insert(root.value, root.other_values)
            else:
                heroes_tree.insert(root.value, root.other_values)
            __forest(root.right)

    if self.root is not None:
        __forest(self.root)

    return heroes_tree, villains_tree
heroes_tree, villains_tree = forest(arbol_mcu)

def count_nodes(self):
    def __count_nodes(root):
        if root is None:
            return 0
        else:
            return 1 + __count_nodes(root.left) + __count_nodes(root.right)

    if self.root is not None:
        return __count_nodes(self.root)
    else:
        return 0
    
print("g.I) Cantidad de nodos en el arbol de heroes:", count_nodes(heroes_tree))
print("g.I) Cantidad de nodos en el arbol de villanos:", count_nodes(villains_tree))

def in_order(self):
        def __in_order(root):
            if root is not None:
                __in_order(root.left)
                print(root.value, root.other_values)
                __in_order(root.right)

        if self.root is not None:
            __in_order(self.root)

print("g.II) Barrido ordenado alfabeticamente del arbol de heroes:")
in_order(heroes_tree)
print("g.II) Barrido ordenado alfabeticamente del arbol de villanos:")
in_order(villains_tree)
