from math import sin, cos, tan
print('Calcular Seno, Cosseno e Tangente do Ângulo')
num = int(input('Digite um Ângulo: '))
print('O ângulo digitado foi {}.'.format(num))
print('O seno é aproximadamente {:.4f} '.format(sin(num)))
print('O cosseno é aproximadamente {:.4f}'.format(cos(num)))
print('A tangente é aproximadamente {:.4f}'.format(tan(num)))

