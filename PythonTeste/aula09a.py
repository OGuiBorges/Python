frase = '      Curso em Video Churrasco        '
print(frase[0])
print(frase[0:5])
print(frase[:10])
print(frase[10:])

#Análise
print(len(frase))
#conta os 'o'
print(frase.count('o'))
#conta os 'o' da linha 0 a 13
print(frase.count('o', 0, 13))
#onde começa
print(frase.find('deo'))
print(frase.find('Android'))
print('Curso' in frase)

print(frase.replace('Churrasco', 'Python'))

print(frase.upper())

print(frase.lower())

print(frase.capitalize())

print(frase.title())

print(frase.strip())

print(frase.rstrip())

print(frase.lstrip())

print(frase.split())
print('-'.join(frase.split()))
dividido = frase.split()
print(dividido[1][1])



