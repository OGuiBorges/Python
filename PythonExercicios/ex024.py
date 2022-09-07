cid = str(input('Digite sua cidade: '))
cid = cid.title()
dividido = cid.split()
cid = 'Santo' in dividido[0]
print("Começa com Santo? {}".format(cid))