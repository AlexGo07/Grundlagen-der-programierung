def versch(meth,l):
    crypt_l = []
    if meth == '+':
        for el in l:
            crypt_l.append(el + l[0])
    if meth == '*':
        for el in l:
            crypt_l.append(el * l[0])
    if meth == 'XOR':
        for el in l:
            crypt_l.append(el ^ l[0])
    return crypt_l
l = [5, 10, 15]
k = versch('*',l)
print(k)