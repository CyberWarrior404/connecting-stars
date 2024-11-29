import pgzrun
import random

WIDTH = 600
HEIGHT = 400

Star = Actor("star")
Star.pos = random

def draw():
    screen.blit("bg",(0,0))
    Star.draw()


pgzrun.go()