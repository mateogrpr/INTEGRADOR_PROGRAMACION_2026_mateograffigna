import Menu, Gestion_stock
def main():
    Gestion_stock.iniciar()
    while True:
        opcion = Menu.menuprin()
        if opcion == "Cargar stock":
            Gestion_stock.cargar_stock()
        elif opcion == "Total del stock":
            Gestion_stock.mostrar()
        elif opcion == "Cantidad de productos":
            categoria = input("Ingrese la categoria: ").lower()
            if categoria in Gestion_stock.stock_cantidades:
                Gestion_stock.contar(Gestion_stock.stock_cantidades[categoria])
            else:
                print("Categoria invalida")
        elif opcion == "Salir":
            print("Fin del programa")
            break
        else:
            print("Opcion invalida")
if __name__ == "__main__":
    main()