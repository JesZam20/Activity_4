#Avoid, classic arcade game.

from random import *
from turtle import *

from freegames import vector

north, south = vector(0, 4), vector(0, -4)
east, west = vector(4, 0), vector(-4, 0)
options = north, south, east, west

player = vector(0, 0)
aim = choice(options).copy()
bombs = []
speeds = []
score = 0 #Add variable to store the score


def inside(point):
    """Return True if point on screen."""
    return -300 < point.x < 300 and -200 < point.y < 200


def draw(alive):
    """Draw screen objects."""
    clear()

    #Show score at the upper right corner
    goto(80, 160) #Position of the text
    write(f'Score: {score:.2f}', font=('Arial', 16, 'normal')) #Display the score

    goto(player.x, player.y)
    color = 'blue' if alive else 'red'
    dot(10, color)
    for bomb in bombs:
        goto(bomb.x, bomb.y)
        dot(20, 'black')
    update()


def move():
    """Update player and bomb positions."""
    global score #Indicate that the global variable score is used
    score += 0.05   #Update the score every frame

    player.move(aim)

    for bomb, speed in zip(bombs, speeds):
        bomb.move(speed)

    if randrange(10) == 0:
        speed = choice(options).copy()
        offset = randrange(-199, 200)

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
    ontimer(move, 50)


setup(620, 420, 370, 0)
hideturtle()
up()
tracer(False)
listen()
onkey(lambda: aim.set(north), 'Up')
onkey(lambda: aim.set(south), 'Down')
onkey(lambda: aim.set(east), 'Right')
onkey(lambda: aim.set(west), 'Left')
move()
done()
