import random
from time import sleep

# Function to draw the die face for a given value
def draw_die(value):
    die_faces = {
        1: ["+-------+",
            "|       |",
            "|   •   |",
            "|       |",
            "+-------+"],
        2: ["+-------+",
            "| •     |",
            "|       |",
            "|     • |",
            "+-------+"],
        3: ["+-------+",
            "| •     |",
            "|   •   |",
            "|     • |",
            "+-------+"],
        4: ["+-------+",
            "| •   • |",
            "|       |",
            "| •   • |",
            "+-------+"],
        5: ["+-------+",
            "| •   • |",
            "|   •   |",
            "| •   • |",
            "+-------+"],
        6: ["+-------+",
            "| •   • |",
            "| •   • |",
            "| •   • |",
            "+-------+"],
    }

    for line in die_faces[value]:
        print(line)
    print()

# Simulate rolling a die
def roll_die():
    print("Rolling the die...")
    sleep(2)
    value = random.randint(1, 6)
    draw_die(value)
    return value

# Main function to start the simulation
def simulate_die_rolling():
    for _ in range(3):  # You can adjust the number of rolls as needed
        roll_die()
        sleep(2)

# Driver Code
simulate_die_rolling()