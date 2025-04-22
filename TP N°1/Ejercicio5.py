
def romano_a_decimal(romano):
    valores = {
        'I': 1, 'V': 5, 'X': 10, 'L': 50,
        'C': 100, 'D': 500, 'M': 1000
    }
  
    if len(romano) == 0:
        return 0

    if len(romano) == 1:
        return valores[romano[0]]

    primero = valores[romano[0]]
    segundo = valores[romano[1]]

    if primero >= segundo:
        return primero + romano_a_decimal(romano[1:])
    else:
        return romano_a_decimal(romano[1:]) - primero + segundo - valores[romano[1]]


while True:
    romano = input("Ingrese número romano (o escriba 'salir' para terminar): ").upper()
    if romano == "SALIR":
        print("Programa finalizado.")
        break
    try:
        decimal = romano_a_decimal(romano)
        print("El número en decimal es:", decimal)
    except KeyError:
        print("Entrada inválida. Asegúrese de usar solo caracteres romanos (I, V, X, L, C, D, M).")
    