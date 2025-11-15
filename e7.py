amount = int(input('Ingrese la cantidad de paquetes: '))
pack = []
normal = []
express = []
urgente = []

for a in range(amount):
    print("""
    Paquetes
    1. Normal
    2. Express
    3. Urgente
    """)
    # proceso de validacion
    while True:
        paquete = input('Seleccione el número que corresponde a su paquete: ')

        if paquete.isdigit():
            paquete = int(paquete)

            if paquete == 1:
                pack.append(paquete)
                normal.append(paquete)
                break
            elif paquete == 2:
                pack.append(paquete)
                express.append(paquete)
                break
            elif paquete == 3:
                pack.append(paquete)
                urgente.append(paquete)
                break
            else:
                print('Error: Eleccion equivocada, vuelva a intertarlo')
                continue
        else:
            print('Error: Eleccion equivocada, vuelva a intertarlo')
            
print('\n', pack)
print(f'\n# de paquetes Normal = {len(normal)}')
print(f'# de paquetes Express = {len(express)}')
print(f'# de paquetes Urgente = {len(urgente)}')