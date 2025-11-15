print("""     ------------------------ 
      Taller de vehiculos
      ------------------------

      Valor por hora = $20.000
      valor por pieza = $50.000
""")

amount = int(input('Cuantos vehivulos son: '))

hours = []
piece = []
cost_total = []
complexity = []

for a in range(amount):
    horas = int(input('\nIngrese horas de trabajo en el vehiculo #' + str(a+1) + ' : '))
    piezas = int(input('Cuántas piezas fueron cambiadas en el vehiculo #' + str(a+1) + ' : '))
    costo_total = (horas * 20000) + (piezas * 50000)

    hours.append(horas)
    piece.append(piezas)
    cost_total.append(costo_total)
    

    if horas > 10 or piezas > 4:
        complexity.append('Complejo')
    else:
        complexity.append('No complejo')

# poniendo los resultados en una sola iteración 
print()
for i in range(amount):
    print(f'El vehiculo #{i+1} tiene un costo total de "{cost_total[i]} y su estado es: {complexity[i]}"')
    