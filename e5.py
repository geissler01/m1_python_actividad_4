amount = int(input('Ingrese el número de estudiantes: '))
name_student = []
notes = []

for i in range(amount):
    name = input('Ingrese el nombre del estudiante #' + str(i+1) + ' : ')
    name_student.append(name)

    mean = 0
    for j in range(3):
        nota = float(input(name + ': nota #' + str(j+1) + ' : '))
        mean += nota
    notes.append(round(mean/3, 2))

for k in range(amount):
    print(f'La nota promedio de {name_student[k]} es => {notes[k]}')

