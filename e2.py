print('*'*30)
print('     "Cineland"')
print('*'*30, '\n')

amount = int(input('¿Cuántas peliculas son?: '))
movies = []

for a in range(amount):
    name = input('Ingrese el nombre de la pelicua #' + str(a+1) + ' : ')
    time = int(input('Ingrese la duración de "' + name + '" : '))
    if time > 150:
        movies.append([name, time, 'Larga'])
        
    elif time >= 100 :
        movies.append([name, time, 'Media'])

    else:
        movies.append([name, time, 'Corta'])

print('-'*40)
print('Nombre     |    Duración   |    Etiqueta  ')
print('-'*40)
for i in (movies):
    print(f'{i[0]}      |       {i[1]}      |      {i[2]}')
print('-'*40)

"""
print(f'Pelicuas cortas: {len(short_time)} => {short_time} minutos')
print(f'Peliculas de duracion media: {len(mediun_time)} => {mediun_time} minutos')
print(f'Pelicuas largas: {len(long_time)} => {long_time} minutos')
"""
