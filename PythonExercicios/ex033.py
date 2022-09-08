print('QUAL O MAIOR NÚMERO?')
n1 = float(input('Digite o primeiro número: '))
n2 = float(input('Digite o segundo npumero: '))
n3 = float(input('Digite o terceiro número: '))

if n1 > n2 and n1 > n3:
    print('O primeiro é maior!')
else:
    if n1 < n2 and n2 > n3:
        print('O segundo é maior!')
    else:
        if n1 == n2 and n1 > n3:
            print('O primeiro e o segundo sao maiores')
        else:
            if n1 == n3 and n1 > n2:
                print('O primeiro e o terceiro sao maiores')
            else:
                if n1 == n2 and n1 == n3:
                    print('Todos são iguais!')
                else:
                    if n2 == n3 and n2 > n1:
                        print('O segundo e o terceiro são maiores!')
                    else:
                        print("O terceiro é maior!")

