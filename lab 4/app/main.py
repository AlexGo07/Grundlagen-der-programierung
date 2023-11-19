import turtle
import sys
from ui.consola import menu
from Turtle.alfabet import draw_text
from draw.choice import draw_character, add

while True:
    print(menu)
    screen = turtle.Screen()
    n = int(input("Deine Wahl:"))
    if n == 1:
        m = input("Schreibe:").upper()
        screen.clear()
        t = turtle.Turtle()
        draw_text(t,m)
    elif n == 2:
        actions = input("Schreibe:").upper()
        add(actions)
        screen.clear()
        t = turtle.Turtle()
        draw_character(t,actions)
    else:
        sys.exit("Invalid Wahl")
turtle.done()
