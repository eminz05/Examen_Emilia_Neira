def stock_editorial(editorial):
    editorial=input("Ingrese el nombre de la editorial: ").strip()
    for valor in catalogo:
        catalogo=valor[4]["editorial"]
        print(f"Stock editorial {catalogo[4]}")
    return editorial

def buscar_por_precio(p_min, p_max):
    while True:
        try:
            p_min=int(input("Ingrese el precio mínimo: "))#.index()
            p_max=int(input("Ingrese el precio máximo: "))#.index()
        except ValueError:
            print("Debe ingresar números enteros!!")

        stock_libros=[1]["unidades_disponibles"]
        if stock_libros > 0:
            print(f"Título: '{[0]}', Código: ")
            print(f"Precio mínimo: {p_min}")
            print(f"Precio máximo: {p_max}")
            break
        else:
            print("No hay libros disponibles en ese rango de precios.")

    return p_min,p_max

        
def actualizar_precio(codigo, nuevo_precio):
    codigo=input("Ingrese el código del libro: ").upper().strip()
    nuevo_precio=int(input("Ingrese el nuevo precio del libro: "))
    existe=True

    if codigo == existe:
        print("Precio actualizado!")
        print(f"Precio actualizado: {nuevo_precio}")
    else:
        print("El libro no existe!!")
        return False
