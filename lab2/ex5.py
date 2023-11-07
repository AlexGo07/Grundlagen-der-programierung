def check(a,b,string):
    string2 = string.replace('x', str(a))
    string2 = string2.replace('y',str(b))
    splitted = string2.split('=')
    s1 = splitted[0]
    s2 = splitted[1]
    return eval(s1) == eval(s2)
def filt(l2,string):
    l1 = []
    for i in range(len(l2)):
        if check(l2[i]//10, l2[i]%10, string):
            l1.append(l2[i])
    return l1

expr = input("expresie:")
l2 = [12,45,21,89,42]
print(filt(l2,expr))