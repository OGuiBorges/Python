print('AUMENTO DE SALARIO')
s = float(input('Digite seu salário:'))
if s > 1250:
    s = s + (10 / 100 * s)
    print('Seu salário teve um aumento de 10%, valor atual: R${:.2f}'.format(s))
else:
    s = s + (15 / 100 * s)
    print('Seu salário teve um aumento de 15%, valor atual: R${:.2f}'.format(s))
