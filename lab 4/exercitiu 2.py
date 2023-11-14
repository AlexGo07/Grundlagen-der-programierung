def ersetzung(dateipfad,Ersatzwort,Wort):
    '''

    :param dateipfad:
    :param Ersatzwort:
    :param Wort:
    :return:
    '''
    with open(dateipfad,'r') as date:
        text = date.read()
        text1 = text.replace(Ersatzwort,Wort)
        cont = text.count(Ersatzwort)
    with open(dateipfad,'w') as date:
        date.write(text1)
    if cont > 0:
        return cont
    else:
       return 0
def main():

    dateipfad = 'meine_datei.txt'
    Wort = input('Wort:')
    Ersatzwort = input('Ersatzwort:')
    cont = ersetzung(dateipfad,Ersatzwort,Wort)
    print(f"{Ersatzwort} durch {Wort} an {cont} stellen")
main()