print('UBER')
km = float(input('Digite a distância em Km: '))
if km <= 200:
    print('O valor da viagem foi de: R${}'.format(km * 0.50))
else:
    print('O valor da viagem foi de: R${}'.format(km * 0.45))
