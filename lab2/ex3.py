def concat(l1):
    nr = []
    while len(l1) != 0:
        max_loc = 0
        for i in range(len(l1)):
            if l1[i] > max_loc:
                max_loc = l1[i]
                icop = i
        nr = str(nr) + str(max_loc)
        del l1[icop]
    return nr[2:]
l1 = [24,76,67,42,42]
r = concat(l1)
print(r)