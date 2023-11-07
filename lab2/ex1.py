#1
def wiederholen(l1):
    ohne_doppelte = list(dict.fromkeys(l1))
    return ohne_doppelte
l1 = [24,76,67,42,42]
k = wiederholen(l1)
print(k)