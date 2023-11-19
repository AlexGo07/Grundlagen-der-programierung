
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
def add(actions):
    with open("characters.txt", "a") as date:
        date.write(f"Geschrieben:{actions}\n")