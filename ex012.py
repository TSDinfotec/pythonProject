l = float(input('Digite a largura da parede em metros: '))
a = float(input('Digite a altura da parede em metros: '))
areaTotal = l * a
qtddDeTinta = areaTotal / 2
print('Área total da parede é:{:.2f} m2'.format(areaTotal))
print('Necessitamos de {:.2f} litros de tinta para pintar essa parede'.format(qtddDeTinta))

