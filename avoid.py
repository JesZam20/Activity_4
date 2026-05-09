# Avoid, classic arcade game.

import random
import turtle

from freegames import vector

north, south = vector(0, 4), vector(0, -4)
east, west = vector(4, 0), vector(-4, 0)
options = north, south, east, west

player = vector(0, 0)
aim = random.choice(options).copy()
bombs = []
speeds = []
score = 0  # Add variable to store the score

def inside(point):
    """Return True if point on screen."""
    return -300 < point.x < 300 and -200 < point.y < 200

def draw(alive):
    """Draw screen objects."""
    turtle.clear()

    """Show score at the upper right corner"""
    turtle.goto(170, 160)  # Position of the text
    """Display the score"""
    turtle.write(f'Score: {score:.2f}', font=('Arial', 16, 'normal'))

    turtle.goto(player.x, player.y)
    color = 'blue' if alive else 'red'
    turtle.dot(10, color)
    for bomb in bombs:
        turtle.goto(bomb.x, bomb.y)
        turtle.dot(20, 'black')
    turtle.update()

def move():
    """Update player and bomb positions."""
    global score  # Indicate that the global variable score is used
    score += 0.05  # Update the score every frame

    player.move(aim)

    for bomb, speed in zip(bombs, speeds):
        bomb.move(speed)

    if random.randrange(5) == 0:
        speed = random.choice(options).copy()
        offset = random.randrange(-199, 200)

        if speed == north:
            bomb = vector(offset, -199)
        if speed == south:
            bomb = vector(offset, 199)
        if speed == east:
            bomb = vector(-299, offset)
        if speed == west:
            bomb = vector(299, offset)

        bombs.append(bomb)
        speeds.append(speed)

    for index in reversed(range(len(bombs))):
        bomb = bombs[index]
        if not inside(bomb):
            del bombs[index]
            del speeds[index]

    if not inside(player):
        draw(False)
        return

    for bomb in bombs:
        if abs(bomb - player) < 15:
            draw(False)
            return

    draw(True)
    turtle.ontimer(move, 50)

turtle.setup(620, 420, 370, 0)
turtle.hideturtle()
turtle.up()
turtle.tracer(False)
turtle.listen()
turtle.onkey(lambda: aim.set(north), 'Up')
turtle.onkey(lambda: aim.set(south), 'Down')
turtle.onkey(lambda: aim.set(east), 'Right')
turtle.onkey(lambda: aim.set(west), 'Left')
move()
turtle.done()
