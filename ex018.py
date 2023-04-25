"""co = float(input('Comprimento do cateto oposto é: '))
ca = float(input(' Comprimenyo do cateto adjacente é: '))
hi = (co ** 2 + ca ** 2) ** (1/2)
print('A hipotenusa vai medir {:.2f}'.format(hi))"""

import math
co = float(input('Comprimento do cateto oposto é: '))
ca = float(input(' Comprimenyo do cateto adjacente é: '))
hi = math.hypot(co, ca)
print('A hipotenusa vai medir {:.2f}'.format(hi))
