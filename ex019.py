import math
ang = float(input(' Digite um valor de ângulo qualquer: '))
sen = math.sin(math.radians(ang))
cos = math.cos(math.radians(ang))
tg = math.tan(math.radians(ang))
print('Este ângulo tem o valor de seno {:.2f}, cosseno {:.2f} e tangente {:.2f}.'.format(sen, cos, tg))
