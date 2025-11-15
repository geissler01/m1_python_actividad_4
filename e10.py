# Validacion del numero de empleados
while True:
    number_employees = input('Ingrese número de empleados: ')
    if number_employees.isdigit():
        number_employees = int(number_employees)
        break
    else:
        print('Error: Ingrese un número válido de empleados')

employ_sales = []
for n in range(number_employees):
    name_employ = input('\nIngrese el nombre del empleado #' + str(n+1) + ' : ')
    average = 0
    for i in range(3):
        while True:
            sales = input(name_employ + ': Ingrese # de ventas del mes: ')
            if sales.isdigit() or (sales.count('.') <= 1 and sales != '.'):
                sales = float(sales)
                average += sales
                break
            else:
                print('Error: Ingrese un número de ventas válido')

    employ_sales.append([name_employ, round((average/3), 2)])

for i in range(number_employees):
    if employ_sales[i][1] >= 6:
        employ_sales[i].append('Excelente')
    elif employ_sales[i][1] >= 3:
        employ_sales[i].append('Bien')
    else:
        employ_sales[i].append('Bajo rendimiento')

#print('Lista original')
#print(employ_sales)

print('-'*50)
print('Nombre     |    Promedio     |    calificacion  ')
print('-'*50)
for i in (employ_sales):
    print(f'{i[0]}     |       {i[1]}       |     {i[2]}')
print('-'*40)

