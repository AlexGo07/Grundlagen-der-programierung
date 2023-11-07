def ggt(a, b):
    while b != 0:
        rest = a % b  # wir berechnen der Rest der Division von a und b
        a = b         # verandern a mit b
        b = rest      # verandern b mit dem Rest
    return a  # groste geminsamer faktor

def kgv(a, b):# kleinstes gemainsamen Vielfachen
        return a * b // ggt(a, b)# wir teilen den produkt durch den ggt
def parc(l1):
    k = kgv(l1[0],l1[1])
    for i in range(2,len(l1)):
        k = kgv(k,l1[i])
    return k
l1 = [12,24,48]
erg = parc(l1)
print(erg)