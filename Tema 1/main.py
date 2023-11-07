max_global = 0
while True:
    #introducem numere pana introducem -1 cand se termina programul
    #cand introducem 0 se reseteaza secventa, respectiv maximul local
    n = int(input("Zahl:"))
    max_local = 0
    if n == -1:
        break
    while True:
        n = int(input("Zahl1:"))
        if n > max_local:
            max_local = n
        if n == 0:
            break
    if max_local > max_global:
        max_global = max_local
    print("MAX_LOCAL:", max_local)
print("MAX_GLOBAL", max_global)