nome = str(input('Digite seu nome completo: '))
print("Seu nome é : {}".format(nome))
print("Letras maiúsculas: {}".format(nome.upper()))
print('Letras minúsculas: {}'.format(nome.lower()))
print('Ao todo sem espaços tem: {} letras'.format(len(nome) - nome.count(' ')))
print('Ao todo sem espaços tem: {} letras'.format(len(nome.replace(' ', ''))))
divisao = nome.split()
print('O primeiro nome tem: {} letras'.format(len(divisao[0])))
print('O segundo nome tem: {} letras'.format(len(divisao[1])))
print('O terceiro nome tem: {} letras'.format(len(divisao[2])))


