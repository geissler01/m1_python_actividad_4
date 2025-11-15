print('*'*30)
print('     Playlist')
print('*'*30,'\n')

amount = int(input('¿Cuántas canciones desea ingresar?: '))
songs =[]
songs_unique = []
for a in range(amount):
    name = input('\nIngrese el nombre de la cancion #' + str(a+1) + ' : ')
    genre = input('Ingrese el género musical de ' + name + ' : ')

    songs_dic = {
        'nombre' : name,
        'genero' : genre
    }
    songs.append(songs_dic)

    if a > 0 and songs[a]['genero'] == songs[a-1]['genero']:
        print('Género repetido')
    else:
        songs_unique.append(songs_dic)

print(songs)
print(songs_unique)

# Resultados
print('-'*30)
print('     Canción      |     Género  ')
print('-'*30)
for i in songs_unique:
    print(f'{i['nombre']}       |     {i['genero']}')

print('-'*30) 