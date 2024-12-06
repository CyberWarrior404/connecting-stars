import pgzrun
import random

WIDTH = 600
HEIGHT = 400
noofstar=7
stars=[]
lines=[]
for i in range(noofstar):
    Star = Actor("star")    
    Star.pos = random.randint(50,550),random.randint(50,350)
    stars.append(Star)


def draw():
    screen.blit("bg",(0,0))
    number=1
    for i in (stars):
        i.draw()
        screen.draw.text(str(number),(i.x-5,i.y+10),color="orange")
        number+=1
    for line in lines:
        screen.draw.line(line[0],line[1],color="yellow")

next=0

def on_mouse_down(pos):
    global lines,stars,next
    if stars[next].collidepoint(pos):
        if next:
            lines.append((stars[next-1].pos, stars[next].pos))
            next+=1
        else:
            lines=[]
            next=0



pgzrun.go()