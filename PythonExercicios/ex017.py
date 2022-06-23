from math import hypot, sqrt, pow
print('Calculo da Hipotenusa do Triângulo Retângulo')
num = int(input('Comprimento do Cateto Oposto: '))
num2 = int(input('Comprimento do Cateto Adjascente: '))
num3 = hypot(num, num2)
num4 = (sqrt(pow(num, 2) + pow(num2, 2)))
print('A Hipotenusa é: {:.2f}'.format(num3))
print('A hipotenusa tambem é: {:.2f}'.format(num4))



