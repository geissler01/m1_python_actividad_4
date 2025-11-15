print('*'*40)
print('     Supermercado "DataMarket"')
print('*'*40, '\n')

quantity = int(input('Ingrese la cantidad de productos que desea registrar: '))
products = []
price_total = 0

for q in range(quantity):
    product = input('Ingrese el nombre del producto #' + str(q+1) + ' : ')
    price = float(input('Ingrese el precio: '))
    expired = input('¿El producto está venciado?. si/no: ')

    if expired.lower() != 'si':
        products.append([product, price, 'No vencido'])
        price_total += price
    else :
        print('\nEste producto no se guardará\n')


print('-'*40)
print('Producto     |    precio    |    Estado  ')
print('-'*40)
for i in (products):
    print(f'{i[0]}               {i[1]}               {i[2]}')
print('-'*40)
print(f'El precio final es de => {price_total}')


