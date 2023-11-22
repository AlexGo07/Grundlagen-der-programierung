import turtle
import sys
from ui.consola import menu
from Turtle.alfabet import draw_text
from draw.choice import draw_character, add , splitt

while True:
    print(menu)
    screen = turtle.Screen()
    n = int(input("Deine Wahl:"))
    if n == 1:
        with open('characters1.txt', 'r') as fisier:
            continut = fisier.read()
            print(continut)
        m = input("Schreibe:").upper()
        screen.clear()
        t = turtle.Turtle()
        for ch in m:
            if ch.isalpha():
                draw_text(t,ch)
            elif ch.isdigit():
                draw_character(t,splitt(eval(ch)))
    elif n == 2:
        actions = input("Schreibe:").upper()
        add(actions)
        screen.clear()
        t = turtle.Turtle()
        draw_character(t,actions)
    else:
        sys.exit("Invalid Wahl")
turtle.done()
