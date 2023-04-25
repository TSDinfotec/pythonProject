pp = float(input('Qual o preço do produto: R$ '))
d = (pp * 5)/100
vf = pp - d
print('Valor final do produto com desconto de 5% é de R${:.2f}'.format(vf))
