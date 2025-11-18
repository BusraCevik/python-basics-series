"""
Turtle Racing Game

This program asks the user for the number of racers (between 2 and 10)
and displays each racer as a turtle of a different color on the screen.
The turtles move upward with random speeds, and the first turtle to reach
the top wins the race.

- The user inputs the number of racers
- Turtles are created and positioned evenly across the screen
- Each turn, turtles move forward a random distance
- The winner is printed to the console once a turtle reaches the finish line
"""

import random
import turtle



WIDTH, HEIGHT = 500, 500
COLORS = ['red', 'blue', 'green', 'yellow', 'black', 'purple', 'pink', 'orange', 'cyan', 'brown']

def get_number_of_racers():
    racers = 0
    while True:
        racers = input("Enter the number of racers: ")
        if racers.isdigit():
            racers = int(racers)
        else:
            print("Invalid input not numeric, try again")
            continue
        if 2 <= racers <= 10:
            return racers
        else:
            print("Input must be between 2 and 10, try again")

def race(colors):
    turtles = create_turtles(colors)
    while True:
        for racer in turtles:
            distance = random.randrange(1,20)
            racer.forward(distance)

            x, y = racer.pos()
            if y>= HEIGHT // 2 - 10:
                return colors[turtles.index(racer)]

def create_turtles(colors):
    turtles = []
    spacingx = WIDTH // (len(colors) +1)
    for i, color in enumerate(colors):
        racer = turtle.Turtle()
        racer.color(color)
        racer.shape("turtle")
        racer.left(90)
        racer.penup()
        racer.setpos(-WIDTH//2 + (i + 1) * spacingx, -HEIGHT//2 + 20)
        racer.pendown()
        turtles.append(racer)

    return turtles

def init_turtle():
    screen = turtle.Screen()
    screen.setup(WIDTH, HEIGHT)
    screen.title("Turtle Racing")

    return screen

racers = get_number_of_racers()
screen = init_turtle()


random.shuffle(COLORS)
colors = COLORS[:racers]

winner = race(colors)
print("The winner is ", winner)


screen.mainloop()