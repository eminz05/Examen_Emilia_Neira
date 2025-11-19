def stock_editorial(editorial):
    editorial=input("Ingrese el nombre de la editorial: ").strip()
    valor=stock_editorial[4]["editorial"]
    for valor in editorial:
        print(f"stock {valor[4]}")


def buscar_por_precio(p_min, p_max):

    while True:
        try:
            p_min=int(input("Ingrese el pricio mínimo: ")).index()
            p_max=int(input("Ingrese el precio máximo: ")).index()
        except ValueError:
            print("Debe ingresar números enteros!!")

        is stock
        


#def actualizar_precio(codigo, nuevo_precio):