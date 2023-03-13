import pygame
#use with PygamePong.py

class Player(): #is the primary player
    def __init__(self):
        self.rect1 = pygame.Rect(0, 200, 14, 35) #width, lenth - bottom
        self.rect2 = pygame.Rect(0, 165, 14, 35) #half of the player - top hitbox
        self.screen = pygame.Surface((self.rect1.width, self.rect1.height))
        self.screen2 = pygame.Surface((self.rect2.width, self.rect2.height))
        self.screen.fill((255, 255, 255))
        self.screen2.fill((255, 255, 255))
        self.vel = 6  #distance per second ig

    def update(self, window):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_w] and self.rect2.top > 0:
            self.rect2.y -= self.vel
            self.rect1.y -= self.vel

        if keys[pygame.K_s] and self.rect1.bottom < 400:
            self.rect2.y += self.vel
            self.rect1.y += self.vel
    
        window.blit(self.screen2, (self.rect2.x, self.rect2.y))
        window.blit(self.screen, (self.rect1.x, self.rect1.y))

class DebugPlayer(): #is the secondary player
    def __init__(self):
        self.rect1 = pygame.Rect(786, 200, 14, 35) #half of the player - bottom hitbox
        self.rect2 = pygame.Rect(786, 165, 14, 35) #half of the player - top hitbox
        self.screen = pygame.Surface((self.rect1.width, self.rect1.height))
        self.screen2 = pygame.Surface((self.rect2.width, self.rect2.height))
        self.screen.fill((255, 255, 255))
        self.screen2.fill((255, 255, 255))
        self.vel = 6  #distance per second ig

    def update(self, window):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_UP] and self.rect2.top > 0:
            self.rect2.y -= self.vel
            self.rect1.y -= self.vel

        if keys[pygame.K_DOWN] and self.rect1.bottom < 400:
            self.rect2.y += self.vel
            self.rect1.y += self.vel
    
        window.blit(self.screen2, (self.rect2.x, self.rect2.y))
        window.blit(self.screen, (self.rect1.x, self.rect1.y))



class Ball(): # is the ball
    def __init__(self):
        self.rect = pygame.Rect(400,200,16,16) #width, lenth
        self.screen = pygame.Surface((self.rect.width, self.rect.height))
        self.screen.fill((255, 255, 255))

        self.acceleration = 0.1#speeds up over time - fun to mess with
        self.bvelocity = 12 #constant speed - 0.2 * FPS (60)
        self.yvel = 0
        self.colidereaction = False #if true, moves ball left
        self.colidereactionY = False

    def velocity(self):
        if self.colidereaction == True:
            #self.bvelocity += self.acceleration
            self.rect.x -= self.bvelocity
        else: 
            #self.bvelocity += self.acceleration
            self.rect.x += self.bvelocity
        if self.colidereactionY == True:
            #self.bvelocity += self.acceleration
            self.rect.y -= self.yvel
        else: 
            #self.bvelocity += self.acceleration
            self.rect.y += self.yvel


    def update(self, window):
        window.blit(self.screen, (self.rect.x, self.rect.y))

class Top(): # is the top hitbox
    def __init__(self):
        self.rect = pygame.Rect(0,0,800,5) #width, lenth
        self.screen = pygame.Surface((self.rect.width, self.rect.height))
        self.screen.fill((255, 255, 255))
    def update(self, window):
        window.blit(self.screen, (self.rect.x, self.rect.y))

class Bottom(): #is the bottom hitbox
    def __init__(self):
        self.rect = pygame.Rect(0,395,800,5) #width, lenth
        self.screen = pygame.Surface((self.rect.width, self.rect.height))
        self.screen.fill((255, 255, 255))
    def update(self, window):
        window.blit(self.screen, (self.rect.x, self.rect.y))

class RightScore():
    def __init__(self):
        self.rect = pygame.Rect(799,0,5,400) #width, lenth
        self.screen = pygame.Surface((self.rect.width, self.rect.height))
        self.screen.fill((255, 255, 255))
    def update(self, window):
        window.blit(self.screen, (self.rect.x, self.rect.y))

class LeftScore():
    def __init__(self):
        self.rect = pygame.Rect(-4,0,5,400) #width, lenth
        self.screen = pygame.Surface((self.rect.width, self.rect.height))
        self.screen.fill((255, 255, 255))
    def update(self, window):
        window.blit(self.screen, (self.rect.x, self.rect.y))

class Score():
    def __init__(self):
        self.redgoal = False #this is a mess.. its 11:30pm tho.. idc anymore
        self.bluegoal = False
        self.goal = False
        self.red = 0
        self.blue = 0
        self.font = pygame.font.Font('freesansbold.ttf', 32)
        self.font1 = pygame.font.Font('freesansbold.ttf', 32)
    def update(self, window):
        self.text1 = self.font1.render(('P2 Score ' + str(self.blue)),True, (255, 255, 255))
        self.text = self.font.render(('P1 Score ' + str(self.red)),True, (255, 255, 255))
        window.blit(self.text, (30, 20))
        window.blit(self.text1, (600, 20))

class Countdown():
    def __init__(self):
        self.x = 800
        self.red = 4
        self.font = pygame.font.Font('freesansbold.ttf', 32)
    def update(self, window):
        self.text = self.font.render(str(self.red),True, (255, 255, 255))
        window.blit(self.text, (self.x, 195))
