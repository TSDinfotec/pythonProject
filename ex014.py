s = float(input('Qual o salário atual do funcionário:R$ '))
aumento = (s * 15)/100
ns = s + aumento
print('Seu novo salário com aumento de 15% é de R${:.3f}'.format(ns))
 