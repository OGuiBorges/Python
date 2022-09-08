print('É TRIANGULO???')
a = float(input('Digite a primeira reta do triângulo: '))
b = float(input('Digite a segunda reta do triângulo: '))
c = float(input('Digite a terceira reta do triângulo: '))

if (b - c) < a < (b + c) and (a - c) < b < (a + c) and (a - b) < c < (a + b):
    print('Pode ser um triângulo!')
else:
    print('Não pode ser um triângulo!')