import turtle

# Initialisiere das Turtle-Fenster und den Stift
wn = turtle.Screen()
wn.title("Turtle Paint v1.0")

t = turtle.Turtle()
t.speed(0)  # Maximale Zeichengeschwindigkeit

# Wörterbuch mit vordefinierten Zeichenanweisungen
character_dict = {
    'A': ["F", "D", "W", "D", "W", "A", "S", "A", "S", "D", "W", "G"],
    'B': ["F", "A", "W", "S", "D", "W", "D", "W", "D", "S", "A", "S", "G"],
    # Hinzufügen von mehr Zeichen hier
}

# Funktion zum Zeichnen eines Zeichens
def draw_character(character):
    if character in character_dict:
        for instruction in character_dict[character]:
            if instruction == "W":
                t.forward(10)
            elif instruction == "S":
                t.backward(10)
            elif instruction == "D":
                t.right(45)
            elif instruction == "A":
                t.left(45)
            elif instruction == "F":
                t.penup()
            elif instruction == "G":
                t.pendown()

# Benutzerdefinierte Zeichen speichern und laden
def save_character(character, instructions):
    character_dict[character] = instructions
    with open("custom_characters.txt", "a") as file:
        file.write(f"{character}:{','.join(instructions)}\n")

def load_characters():
    try:
        with open("custom_characters.txt", "r") as file:
            for line in file:
                parts = line.strip().split(':')
                character_dict[parts[0]] = parts[1].split(',')
    except FileNotFoundError:
        pass

# Laden der benutzerdefinierten Zeichen
load_characters()

while True:
    # Menü anzeigen
    print("1. Textnachricht zeichnen")
    print("2. Neues Zeichen hinzufügen")
    choice = input("Wähle eine Option (1/2): ")

    if choice == "1":
        message = input("Gib die Nachricht ein: ").upper()
        for character in message:
            draw_character(character)
    elif choice == "2":
        new_character = input("Gib das Zeichen ein: ").upper()
        if new_character not in character_dict:
            instructions = input("Gib die Zeichenanweisungen ein (z.B. 'W,A,W,G'): ").split(',')
            save_character(new_character, instructions)
        else:
            print("Dieses Zeichen existiert bereits.")
    else:
        break

wn.bye()  # Beende das Turtle-Fenster
