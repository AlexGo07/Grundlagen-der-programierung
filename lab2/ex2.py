def paaren(l1):
    contor = 0
    for i in range(0,len(l1)):
        for j in range(i+1,len(l1)):
            if int(l1[i] % 10) == int(l1[j] / 10) and int(l1[i] / 10) == int(l1[j] % 10):
                contor += 1
    return contor
l1 = [24,76,67,42,42,42]
m = paaren(l1)
print(m)