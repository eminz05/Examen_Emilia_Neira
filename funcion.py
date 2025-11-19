# #[título, autor, tipo, páginas, editorial, idioma]
# catalogo = {
#  'BK001': ['El Quijote', 'Miguel de Cervantes', 'físico', 1200, 'Editorial Planeta', 'español'],
#  'BK002': ['1984', 'George Orwell', 'digital', 328, 'Penguin', 'inglés'],
#  'BK003': ['Rayuela', 'Julio Cortázar', 'físico', 600, 'Sudamericana', 'español'],
#  'BK004': ['Sapiens', 'Yuval Noah Harari', 'digital', 450, 'Debate', 'inglés'],
 
# }

# #[precio, unidades_disponibles]
# inventario = {
#  'BK001': [15990, 3],
#  'BK002': [8990, 0],
#  'BK003': [18990, 7],
#  'BK004': [12500, 5],
 
# }

def stock_editorial(editorial):
    editorial=input("Ingrese el nombre de la editorial: ").strip()
    for valor in catalogo:
        catalogo=valor[4]["editorial"]
        editorial=catalogo[4]

    for llave in inventario:
        inventario=llave[0]["unidades"]
    stock_editorial= stock_editorial[llave][0]=+1

    print(f"Stock editorial {editorial} {stock_editorial}")
    return editorial

def buscar_por_precio(p_min, p_max):
    while True:
        try:
            p_min=int(input("Ingrese el precio mínimo: ")).index()
            p_max=int(input("Ingrese el precio máximo: ")).index()
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

    return codigo, nuevo_precio