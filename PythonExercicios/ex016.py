from math import trunc, fabs
print('Porção inteira dos números')
num = float(input('Digite um número real com algarismos depois da virgula: '))
print('O número {} tem a parte inteira {}'.format(num, trunc(num)))
