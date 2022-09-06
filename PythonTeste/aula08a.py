import random
from math import sqrt

import emoji

num = int(input('Digite um número: '))
raiz = sqrt(num)
print('A raiz de {} é igual a {:.2f}'.format(num, raiz))

num2 = random.randint(1, 10)
print('Numero aleatorio: {}'.format(num2))

print(emoji.emojize("Olá, Mundo :earth_americas:"))
