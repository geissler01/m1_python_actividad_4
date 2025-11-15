# Validacion de habitaciones
while True:
    quantity = input('Ingrese el número de habitaciones: ')
    if quantity.isdigit():
        quantity = int(quantity)
        break
    else:
        print('Error: el valor ingresado no es numero entero positivo. Vuelva a intentarlo\n')

rooms = []

for q in range(quantity):
    # Validando el numero de habitacion
    while True:
        number_room  = input('Ingrese el número de la habitacion #' + str(q+1) + ' : ')
        if number_room.lstrip('-').isdigit():  # lstrip('-) me permite ingresar numeros negativos para habitaciones al eliminar '-' al inicio para la prueba isdigit()
            break
        else:
            print('Error: el valor ingresado no es valido. Vuelva a intentarlo\n')
    # Validacion de seleccion ocupacion
    while True:
        state = input('¿La habitación "' + number_room + '" esta libre?. Escriba "si" o "no" : ')
        if state.lower() == 'si':
            break
        elif state.lower() == 'no':
            break
        else:
            print('Error: Elija una opción válida')
    
    # Rellenando la base de datos
    rooms.append([number_room, state])

print(f'\nHabitaciones analizadas {rooms}\n')    
free_rooms = []
taken_rooms = []
taken = 0
free = 0
# resultados
for k in rooms:

    if k[1].lower() == 'si':
        free += 1  # Conteo de habitaciones libres
        free_rooms.append([k[0]])
    
    elif k[1].lower() == 'no':
        taken += 1  # conteo de habitaciones ocupadas
        taken_rooms.append([k[0]])


print(f'Habitaciones libres => {free_rooms}')
print(f'Habitaciones ocupadas => {taken_rooms}')

print(f'\n# Habitaciones libres = {len(free_rooms)}   |   # Habitaciones ocupadas = {len(taken_rooms)}')
print(f'# Habitaciones libres = {free}   |   # Habitaciones ocupadas = {taken}')