print('*'*30)
print('    Gimnasio "PriFit"')
print('*'*30, '\n')

# Validacion de semanas
while True:
    week = input('Ingrese la cantidad de semanas que entrenaste: ').strip()
    if week.isdigit():
        if int(week) < 0:
            print('Error: Debe ingresar un número de "0"')
            continue
        else:
            week = int(week)
            break
    else:
        print('Error: el valor ingresado no es válido')

points = []
total_points = 0

for w in range(week):
    # Validacion de días
    while True:
        days = input('Cuántos días entrenaste en la semana #' + str(w+1) + ' : ').strip()
        if days.isdigit():
            if int(days) > 7 or int(days) < 0:
                print('Error: Debe ingresar un número de "0 a 7"')
                continue
            else:
                days = int(days)
                break
        else:
            print('Error: el valor ingresado no es válido')

    # Condicionales para puntos
    if days >= 5 and days < 8:
        s = 'semana #' + str(w+1)
        points.append([s, days, 10])
    elif days == 3 or days == 4:
        s = 'semana #' + str(w+1)
        points.append([s, days, 5])
    elif days < 3 and days >=0:
        s = 'semana #' + str(w+1)
        points.append([s, days, 2])
    else:
        print('error: debe ser un numero mayor o igual a "0"')

# Resultados
print('-'*40)
print('Semana     |    Dias    |    puntos  ')
print('-'*40)
for i in points:
    print(f'{i[0]}  |     {i[1]}      |     {i[2]}')
print('-'*40)

# Contando puntos
for p in points:
    total_points += p[2]
print(f'Puntos acumulados => {total_points}')