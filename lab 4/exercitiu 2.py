def ersetzung(dateipfad,Ersatzwort,Wort):
    with open(dateipfad,'r') as date:
        text = date.read()
        text1 = text.replace(Ersatzwort,Wort)
        cont = text.count(Ersatzwort)
    with open(dateipfad,'w') as date:
        date.write(text1)
    if cont > 0:
        print(f"{Ersatzwort} durch {Wort} an {cont} stellen")
    else:
       print("Die Ersetzung wurde nicht ervollbar")
def main():
    dateipfad = 'meine_datei.txt'
    Wort = 'Hund'
    Ersatzwort = 'Katze'
    ersetzung(dateipfad,Ersatzwort,Wort)
main()