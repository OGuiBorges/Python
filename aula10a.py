nome = str(input('Qual seu nome: '))
if nome == 'Gustavo':
    print('Que nome lindo você tem!')
else:
    print("Seu nome é tão normal!")
print('Bom dia, {}'.format(nome))

n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))
m = (n1 + n2) / 2
print('Sua média foi {:.1f}'.format(m))
if m >= 6:
    print('Aprovado!')
else:
    if m >= 3:
        print('Exame!')
    else:
        print('Reprovado!')

#condição simplificada
#print('Aprovado' if m >= 6 else 'Reprovado')