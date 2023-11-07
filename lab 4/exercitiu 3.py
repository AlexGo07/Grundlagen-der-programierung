import random
def Comp():
    pc = ['Stein','Papier','Schere']
    pc = random.choice(pc)
    return pc
def Player():
    while True:
        p1 = input('Wahle(Stein,Papier,Schere):')
        p1 = input().strip().capitalize()
        if p1 in ['Schere','Papier','Stein']:
            return p1
        else:
            print('ungultige Zeichen, gebe eine andere')
def Match(pc,p1):
    if p1 == pc:
        return "Gleichwertigkeit"
    elif (pc == 'Schere' and p1 == 'Stein') or (p1 == 'Papier' and pc == 'Stein') or (pc == 'Papier' and p1 == 'Schere'):
        return 'Player gewinnt'
    else:
        return 'PC gewinnt'
def main():
    ctpc = 0
    ctp1 = 0
    for i in range(3):
        pc = Comp()
        p1 = Player()
        print(pc)
        if Match(pc,p1) == 'PC gewinnt':
            ctpc += 1
        elif Match(pc,p1) == "Player gewinnt":
            ctp1 += 1
    if ctp1 > ctpc:
        print("Du hast gewonnen")
    elif ctp1 < ctpc:
        print("PC hat gewonnen")
    else:
        print("Egalitaet")
main()