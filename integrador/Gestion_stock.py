stock_productos = { 'enlatados': [], 'frutas': [], 'congelados': [], 'panaderia': [] } 
stock_cantidades = { 'enlatados': [], 'frutas': [], 'congelados': [], 'panaderia': [] }
def iniciar():
    for i in stock_productos:
        stock_productos[i] = []
    for i in stock_cantidades:
        stock_cantidades[i] = []
def cargar_stock():
    categoria = input("Ingrese la categoría (enlatados, frutas, congelados, panaderia): ").lower()
    if categoria in stock_productos:
        producto = input("Ingrese el nombre del producto: ")
        cantidad = int(input("Ingrese la cantidad: "))
        stock_productos[categoria].append(producto)
        stock_cantidades[categoria].append(cantidad)
    else:
        print("Categoria invalida")
def mostrar():
    for categoria in stock_productos:
        print(categoria)
        for i in range(len(stock_productos[categoria])):
            print("producto: ", stock_productos[categoria][i], ", cantidad: ", stock_cantidades[categoria][i])
def contar():
    print(len(stock_productos))
    print(sum(stock_cantidades))