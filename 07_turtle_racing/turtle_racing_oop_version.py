"""
Turtle Racing Game - OOP Version
This program implements a turtle race using Object-Oriented Programming.
Race class handles the screen, number of racers, countdown, and running the race.
Racer class represents each turtle, its color, position, and movement.
"""

import random
import turtle
import time

WIDTH, HEIGHT = 500, 500
COLORS = ['red', 'blue', 'green', 'yellow', 'black', 'purple', 'pink', 'orange', 'cyan', 'brown']

class Racer:
    def __init__(self, color, start_x, start_y):
        self.turtle = turtle.Turtle()
        self.turtle.color(color)
        self.turtle.shape("turtle")
        self.turtle.left(90)
        self.turtle.penup()
        self.turtle.setpos(start_x, start_y)
        self.turtle.pendown()
        self.color = color

    def move(self):
        distance = random.randrange(1, 20)
        self.turtle.forward(distance)

    def get_position(self):
        return self.turtle.pos()

class Race:
    def __init__(self):
        self.WIDTH, self.HEIGHT = WIDTH, HEIGHT
        self.COLORS = COLORS.copy()
        self.screen = self.create_screen()

    def create_screen(self):
        screen = turtle.Screen()
        screen.setup(self.WIDTH, self.HEIGHT)
        screen.title("Turtle Racing")
        return screen

    def get_number_of_racers(self):
        while True:
            racers = input("How many racers do you want? (2-10): ")
            if racers.isdigit():
                racers = int(racers)
                if 2 <= racers <= 10:
                    return racers
            print("Please enter a number between 2 and 10.")

    def create_racers(self, num_racers):
        random.shuffle(self.COLORS)
        selected_colors = self.COLORS[:num_racers]
        spacingx = self.WIDTH // (num_racers + 1)
        racers = []

        for i, color in enumerate(selected_colors):
            start_x = -self.WIDTH // 2 + (i + 1) * spacingx
            start_y = -self.HEIGHT // 2 + 20
            racer = Racer(color, start_x, start_y)
            racers.append(racer)
        return racers

    def countdown(self):
        pen = turtle.Turtle()
        pen.hideturtle()
        pen.penup()
        pen.setpos(0, 0)
        for count in ["3", "2", "1", "Go!"]:
            pen.clear()
            pen.write(count, align="center", font=("Arial", 32, "bold"))
            time.sleep(1)
        pen.clear()

    def show_winner(self, winner_color, turtles):
        winner_racer = None
        for racer in turtles:
            if racer.color == winner_color:
                winner_racer = racer.turtle
                break

        if winner_racer:
            # Turtle'ı merkeze taşı
            winner_racer.penup()
            winner_racer.setpos(0, 0)
            winner_racer.pendown()
            winner_racer.turtlesize(stretch_wid=3, stretch_len=3)  # Boyutu büyüt
            # 360 derece dönme animasyonu
            for _ in range(20):
                winner_racer.right(18)
                self.screen.update()
                time.sleep(0.1)

        pen = turtle.Turtle()
        pen.hideturtle()
        pen.penup()
        pen.setpos(0, -50)  # Yazıyı biraz altına yaz
        pen.write(f"{winner_color} wins!", align="center", font=("Arial", 24, "bold"))

    def start_race(self):
        num_racers = self.get_number_of_racers()
        racers = self.create_racers(num_racers)

        self.countdown()

        winner = None
        while not winner:
            for racer in racers:
                racer.move()
                x, y = racer.get_position()
                if y >= self.HEIGHT // 2 - 10:
                    winner = racer.color
                    break

        self.show_winner(winner, racers)
        return winner

if __name__ == "__main__":
    race = Race()
    race.start_race()
    race.screen.mainloop()
