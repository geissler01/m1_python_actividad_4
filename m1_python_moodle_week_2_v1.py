message = """
1. Agregar producto
2. Mostrar Inventario
3. Calcular estadísticas
4. Salir
"""

inventary = []

while True:
    # Validacion de eleccion
    print(message)      # menu de seleccion
    selection = input('Seleccione la opcion que desea realizar: ')      # seleccion
    if selection.isdigit():     #Pueba si la seleccion es un numero
        selection = int(selection)      # convierte a entero la variable seleccion
        if selection == 1:
            while True:     
                name = input('\nIngrese el nombre del producto: ') # No importa lo que ingresen
                value = []

                # Valido que precio sea compatible con float
                while True:
                    price = input('Ingrese el precio para ' + name + ': ').strip() 
                    # con strip limpio espacios involuntarios al inicio o al final de lo ingresado
                    if price == '':
                        print('Error: ingresa un valor válido\n')
                        continue
                    try:
                        price = float(price)
                        if price < 0:
                            print('Error: ingresa un valor válido\n')
                        else:
                            break
                    except ValueError:
                        print('Error: ingresa un valor válido\n')

                # Valido que cantidad sea entero positivo
                while True:
                    amount = input('Ingrese la cantidad de ' + name + ' que desea: ').strip()

                    if amount == '':
                        print('Error: ingresa un valor válido\n')
                        continue

                    if amount.isdigit():
                        amount = int(amount)
                        break
                    else:
                        print('Error: cantidad no permitida')

                # Comenzamos a funcionar
                # Guardando los valores en el diccionario
                dictionary = {
                'nombre': name,
                'precio': price,
                'cantidad': amount
                }
                # validacion de los datos ingresados
                print(f'\nlos datos ingresados son: {dictionary}')
                save_dates = input('¿Desea agregar este registro a la base de datos?. si/no : ')
                if save_dates.lower() == 'si':
                    inventary.append(dictionary)
                else:
                    print('\nNo se guardaron los valores ingresados\n')

                # atajo rapido para nuevo ingresar nuevo producto
                new_product = input('\n¿Desea añadir un nuevo producto/precio/cantidad? si/no : ')
                if new_product.lower() == 'si':
                    continue
                else:
                    print('\nVolviendo al menú de seleción')
                    break
                
        elif selection == 2:
            # Inventario
            if len(inventary) != 0:
                print('-'*50)
                print('PRODUCTO    |   PRECIO   | CANTIDAD |  total')
                print('-'*50)
                for p in inventary:
                    print(f'{p['nombre']}    |    {p['precio']}    |   {p['cantidad']}   |   {p['precio']*p['cantidad']}')
                print('-'*50)

            else:
                print('-'*50)
                print('PRODUCTO     |   PRECIO    |   CANTIDAD  ')
                print('-'*50)
                print(f'{inventary} : su inventario está vacío')
                print('-'*40)
                continue
        
        elif selection == 3:

            sum = 0
            print('-'*50)
            print('PRODUCTO    |   PRECIO   | CANTIDAD |  total')
            print('-'*50)
            for i in inventary:
                sum += i['precio'] * i['cantidad']
                print(f'{i['nombre']}    |    {i['precio']}    |   {i['cantidad']}   |   {i['precio']*i['cantidad']}')

            print('-'*50)
            print(f'Total productos => {len(inventary)}   |   Precio final Inventario = {sum}')

        elif selection == 4:
            print('\nHasta pronto')
            break
        
        else:
            print('Selección no válida')
            continue

    else:
        print('\nPor favor ingrese una opcion valida')
    

# Menú: lo puse en un string para que sea fácil de leer y se repite mediante el while.

# Validación de opción: pido input, si es número lo convierto y valido el menú, si no, error.

# Opción 1: agregar - bucle interno para varios productos.

# Nombre: cualquier cosa vale.

# Precio: try/except para no crashear con basura, rechazo negativos y vacíos.

# Cantidad: solo enteros positivos con .isdigit(), permito "cero" por si acaso.

# Diccionario: nuevo por producto, para no repetir.

# Muestro datos, pregunto si quiere guardar o no el registro, con append lo añado a la lista inventary si sí.

# Pregunta para ingresar de manera directa otro producto.

# Opción 2: mostrar el inventario - tabla con líneas si hay algo, si no, "vacío".

# Opción 3: estadísticas - suma precio*cantidad, muestro tabla y total.

# Opción 4: salir - break y chau.