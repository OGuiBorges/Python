n1 = int(input('Digite um número: '))
n2 = int(input('Digite outro número: '))
s = n1 + n2
m = n1 * n2
d = n1 / n2
di = n1 // n2
r = n1 % n2
e = n1 ** n2

print('A soma é {:-^20}'.format(s))
print('A multiplicação é {}'.format(m))
print('A divisão é {:.1f}'.format(d))
print('a divisão inteira é {}'.format(di))
#end=' ' nao quebra linha
print('O resto da divisão é {}'.format(r), end=' ')
print('E a potencia \nentre eles é {}'.format(e))
