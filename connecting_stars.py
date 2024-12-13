import pgzrun
import random
import time

WIDTH = 600
HEIGHT = 400
noofstar=7
stars=[]
lines=[]
timer=10
game_over=False
start_time=0
for i in range(noofstar):
    Star = Actor("star")    
    Star.pos = random.randint(50,550),random.randint(50,350)
    stars.append(Star)

def end_game():
    global game_over
    game_over=True

def update():
    if game_over:
        return
    elaspedtime=time.time()-start_time
    if elaspedtime>=timer:
        end_game()

def draw():
    screen.blit("bg",(0,0))
    if game_over:
        screen.draw.text("To Slow ReheHehhehHehhHehhhe...",(WIDTH//2 ,50))
    number=1
    for i in (stars):
        i.draw()
        screen.draw.text(str(number),(i.x-5,i.y+10),color="orange")
        number+=1
    for line in lines:
        screen.draw.line(line[0],line[1],color="crimson")
    elapsedtime=time.time()-start_time
    timeleft=max(0,timer-int(elapsedtime))
    screen.draw.text(f"Time left:{timeleft}",(50 ,50),fontsize=25.000000000001)
    if timeleft==0:
        end_game()

next=0



def on_mouse_down(pos):
    global lines, stars, next
    if stars[next].collidepoint(pos):
        if next > 0:
            lines.append((stars[next-1].pos, stars[next].pos))
        next+=1
        if next>=len(stars):
            lines=[]
            next=0

start_time=time.time()

pgzrun.go()