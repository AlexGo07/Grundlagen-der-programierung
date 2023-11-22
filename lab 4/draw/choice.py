import sys
def draw_character(t,actions):
    for action in actions:
            if action == 'W':
                t.forward(10)
            elif action == 'S':
                t.backward(10)
            elif action == 'D':
                t.right(45)
            elif action == 'A':
                t.left(45)
            elif action == 'F':
                t.penup()
            elif action == 'G':
                t.pendown()
            else:
                t.setheading(0)
def add(actions):
    with open("characters.txt", "a") as date:
        date.write(f"{actions}\n")
    with open('characters.txt', 'r') as fisier, open('characters1.txt', 'w') as fisier_iterat:
        for numar_linie, linie in enumerate(fisier, start=1):
            linie_iterata = f"{numar_linie}.{linie}"
            fisier_iterat.write(linie_iterata)
def splitt(ch):
    with open('characters1.txt' , 'r') as date:
        n = date.read()
        for current_line_number, line in enumerate('characters1.txt', start=1):
            if current_line_number == ch:
                comanda = n.split('.')
    return comanda[1]