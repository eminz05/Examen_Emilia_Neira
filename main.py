import funcion as fn

#[título, autor, tipo, páginas, editorial, idioma]
catalogo = {
 'BK001': ['El Quijote', 'Miguel de Cervantes', 'físico', 1200, 'Editorial Planeta', 'español'],
 'BK002': ['1984', 'George Orwell', 'digital', 328, 'Penguin', 'inglés'],
 'BK003': ['Rayuela', 'Julio Cortázar', 'físico', 600, 'Sudamericana', 'español'],
 'BK004': ['Sapiens', 'Yuval Noah Harari', 'digital', 450, 'Debate', 'inglés'],
 
}

#[precio, unidades_disponibles]
inventario = {
 'BK001': [15990, 3],
 'BK002': [8990, 0],
 'BK003': [18990, 7],
 'BK004': [12500, 5],
 
}

while True:
    print("*** MENÚ PRINCIPAL ***")
    print("1. Stock por editorial")
    print("2. Buscar libros por precio")
    print("3. Actualizar precio de libro")
    print("4. Salir")

    try:
        opc=int(input("Seleccione una opción(1-4): "))
    except ValueError:
        print("Error. Debe ingresar un número entero.")

    if opc==1:
        fn.stock_editorial(editorial)
    elif opc==2:
        fn.buscar_por_precio(p_min, p_max)
    elif opc==3:
        fn.actualizar_precio(codigo, nuevo_precio)
    elif opc==4:
        print("Programa finalizado")
        break
    else:
        print("Debe seleccionar una válida!!")