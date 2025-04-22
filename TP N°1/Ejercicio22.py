import random
def usar_la_fuerza(mochila, index=0, objetos_sacados=0):
    
    if index >= len(mochila):
        return False, objetos_sacados
    else:
        objetos_sacados += 1
        if mochila[index] == 'sable de luz':
            return True, objetos_sacados
        else:
            return usar_la_fuerza(mochila, index + 1, objetos_sacados)


mochila = [
    'comida', 'agua', 'binoculares', 'manta térmica',
    'kit médico', 'herramientas',
'mapa', 'radio', 'linterna'
]

if random.choice([True, False]):
    mochila.append('sable de luz')
    
random.shuffle(mochila)  


encontrado, intentos = usar_la_fuerza(mochila)

if encontrado:
    print(f'¡El Jedi encontró el sable de luz en {intentos} intentos!')
else:
    print('No se encontró el sable de luz en la mochila.')