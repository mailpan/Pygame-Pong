# mailpan#8064
# Computer Science 10
# pong on pygame

#started September 27 2022
#"Finished" on Jan 17 2023
#things to add: score limit, maybe a pause screen, and a proper ball reset, as well as HEAVY code optimization(basically rewriting everything)

#if runs poorly, try running on visual studio or a different ide
import os
import pygame
import random

from Objection import DebugPlayer
from Objection import Player
from Objection import Ball
from Objection import Top
from Objection import Bottom
from Objection import RightScore
from Objection import LeftScore
from Objection import Score
from Objection import Countdown

screen = pygame.display.set_mode((800, 400))

pygame.init()

os.environ["SDL_VIDEO_CENTERED"] = "1" #centers the screen, i think...
pygame.display.set_caption("Png of the PONG")
clock = pygame.time.Clock()#modual for time/fps
fps = 60#frames per second

dplayer = DebugPlayer()
player = Player()
ball = Ball()
top = Top()
bottom = Bottom()
right = RightScore()
left = LeftScore()
score = Score()
count = Countdown()

class Debug(): #debug class for... well. debugging
    def __init__(self):
        self.timer = 0
        self.timer2 = 0

    def timers(self):
        self.timer += 1
        if self.timer == 60: # resets timer every second
            self.timer = 0

    def ballposition(self):
        if self.timer == 45: 
            print("pos", ball.rect.x)

    def consolefps(self):
        if self.timer == 59:
            self.timer2 += 1
        if self.timer2 == 3:# gives fps every 3 seconds
            self.timer2 = 0
            print(clock)
debug = Debug()


def collide():
    if ball.rect.colliderect(dplayer.rect1):
        ball.colidereaction=True #note to self.. we're gonna split the players in two
        ball.colidereactionY=False
        ball.yvel = random.randint(1, 9)#random angle
    if ball.rect.colliderect(dplayer.rect2):#paddle has a unique bounce off the paddle.. paddle split in two. ball goes in the direction of that of the side of the paddle..
        ball.colidereaction=True
        ball.colidereactionY=True
        ball.yvel = random.randint(1, 9)

    if ball.rect.colliderect(player.rect1):
        ball.colidereaction=False 
        ball.colidereactionY=False
        ball.yvel = random.randint(1, 7)
    if ball.rect.colliderect(player.rect2):
        ball.colidereaction=False
        ball.colidereactionY=True
        ball.yvel = random.randint(1, 7)

    if ball.rect.colliderect(top):
        ball.colidereactionY=False
    if ball.rect.colliderect(bottom):
        ball.colidereactionY=True

    if ball.rect.colliderect(right):
        ball.rect.y = 300
        ball.rect.x = 900
        ball.yvel = 0
        ball.bvelocity = 0
        score.redgoal = True
        score.goal = True

    if ball.rect.colliderect(left):
        ball.rect.y = 300
        ball.rect.x = 900
        ball.yvel = 0
        ball.bvelocity = 0
        score.bluegoal = True
        score.goal = True
    
timer_event = pygame.USEREVENT+1
pygame.time.set_timer(timer_event, 1000)

running = True
while running:
    screen.fill((0, 0, 0))

    clock.tick(fps)#runs game at a certain fps

    #debug.timers()
    #debug.consolefps()#debug, gives fps in console
    #debug.ballposition()
    collide()
    player.update(screen)
    dplayer.update(screen)
    ball.update(screen)
    ball.velocity()
    right.update(screen)
    left.update(screen)
    score.update(screen)
    count.update(screen)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == timer_event and score.goal == True:
            if score.redgoal == True:
                score.red = score.red + 1
                score.redgoal = False
            if score.bluegoal == True:
                score.blue = score.blue+1
                score.bluegoal = False

            count.x =400# all this is that stupid timer
            count.red -= 1
            count.update(screen)
            if count.red == 0:
                count.x = 800#moves the counter as idk how to make it disappear otherwisered = int('')
                #pygame.time.set_timer(timer_event, 0)
                count.red = 4
                score.goal = False
                ball.bvelocity = 10 #feels faster starting if i put 12, might just be tired
                ball.rect.x = 400
                ball.rect.y = 200

    pygame.display.flip()
