dias = int(input('Qunatos dias de aluguel: '))
km = float(input('Quantos kilometros rodados: '))
pago = (dias * 60) + (km * 0.15)
print('O total a ser pago pla locação é de R${:.2f}'.format(pago))
