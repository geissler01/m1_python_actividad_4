# Validacion de entrada
while True:
    amount = input('Ingrese el número de facturas que desea registrar: ')
    if amount.isdigit():
        amount = int(amount)
        break
    else:
        print('Error: el valor ingresado no es numero entero positivo. Vuelva a intentarlo\n')

bill = []

for a in range(amount):
    client = input('Ingrese el nombre del cliente en la factura #' + str(a+1) + ' : ')

    while True:
        value = input('Ingrese el valor de la factura de ' + client + ' : ')
        if value.isdigit() or (value.count('.') <= 1 and value != '.'):
            value = float(value)
            break
        else:
            print('Error: ingrese un valor valido para precio')

    while True:
        tipo = input("""Tipo de factura:
        1. Factura normal
        2. Factura premiun
        
        Seleccione el tipo de factura: 
        """)
        if int(tipo) == 1:
            deduction = 0.95
            break
        elif int(tipo) == 2:
            deduction = 0.9
            break
        else:
            print('Error: ingrese una opción valida')
    # Llenando la lsita con lista
    bill.append([client, value, deduction])

total = 0
for i in bill:
    print(f'cliente: {i[0]}   |   valor: {i[1]}   |   tipo factura: {i[2]}   |   total =>{i[1]*i[2]}')
    total += i[1]*i[2]

print(f'El total de todas las facturas es: {total}')