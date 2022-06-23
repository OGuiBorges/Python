import random
from math import sqrt, floor
import emoji
num = int(input('Digite um número: '))
raiz = sqrt(num)
print('A raiz de {} é igual a {:.2f}'.format(num, floor(raiz)))

num2 = random.randint(1, 10)
print(num2)

print(emoji.emojize('Olá, Mundo :earth_americas:'))
