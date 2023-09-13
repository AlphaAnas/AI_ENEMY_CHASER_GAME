#https://www.youtube.com/watch?v=FfWpgLFMI7w
import pygame
import sys
import random

width , height = 800 , 600

screen = pygame.display.set_mode((width, height))
pygame.display.set_caption('ENEMY CHASER AI')
icon=pygame.image.load('teddy-bear.png')
pygame.display.set_icon(icon)
player_img=pygame.image.load('angry-birds.png')
enemy_img=pygame.image.load('kindpng_1122861.png')
enemy_img = pygame.transform.scale(enemy_img, (64, 64)) #reducing the size to 64 pixels.
clock = pygame.time.Clock()


class Player:
    def __init__(self, x, y):
        self.x = int(x)
        self.y = int(y)
        self.enemyx=random.randint(0,800) # enemy can pop up from any randon direction
        self.enemyy=random.randint(50,150)
        self.rect= screen.blit(player_img,(self.x, self.y)) #still don't know its use. was just testing
       # self.rect = pygame.Rect(self.x, self.y, 32, 32)
       # self.color = (250, 120, 60)
        self.x_speed = 0
        self.y_speed = 0
        self.enemyXspeed = 0 
        self.enemyYspeed = 0
        self.left_pressed = False
        self.right_pressed = False
        self.up_pressed = False
        self.down_pressed = False
        self.player_speed = 1
        self.enemy_speed=0.7

    def player_draw(self, img): #removed the paramter window.
        #pygame.draw.rect(win, self.color, self.rect)
        screen.blit(img,(self.x, self.y))
    def enemy_draw(self, img): 
       
        screen.blit(img,(self.enemyx,self.enemyy))

    def update(self): # seting position for our player
        self.x_speed = 0 
        self.y_speed = 0
        if self.left_pressed and not self.right_pressed and self.x>0:
            self.x_speed =- self.player_speed
        if self.right_pressed and not self.left_pressed and self.x<width-64: # subtracted 64 cuz pixel size of player is 64 so it will stop 64 pixels before the edge.
            self.x_speed = self.player_speed
        if self.up_pressed and not self.down_pressed and self.y>0:
            self.y_speed =- self.player_speed
        if self.down_pressed and not self.up_pressed and self.y<height-64:#subtracted 64 cuz pixel size of player is 64 so it will stop 64 pixels before the edge
            self.y_speed = self.player_speed

        self.x += self.x_speed
        self.y += self.y_speed

        # setting position of the enemy
    def update_enemy(self):
        self.enemyXspeed = -0.8
        self.enemyYspeed = 0
        self.enemyx += self.enemyXspeed
        self.enemyy += self.enemyYspeed
        # if enemy hits boundary then its movement starts in opposite direction
        if self.enemyx<=0:
            self.enemyx=736
        elif self.enemyx>=736:
            self.enemyx = 0
            # self.enemyXspeed=-self.enemy_speed

        
   
       # self.rect = pygame.Rect(int(self.x), int(self.y), 32, 32)

player = Player(width//2,height//2)
#enemy=Player(width//2,height//2)


    

running = True


while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT :
                player.left_pressed = True
            if event.key == pygame.K_RIGHT :
                player.right_pressed = True
            if event.key == pygame.K_UP:
                player.up_pressed = True
            if event.key == pygame.K_DOWN:
                player.down_pressed = True

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                player.left_pressed = False
            if event.key == pygame.K_RIGHT:
                player.right_pressed = False
            if event.key == pygame.K_UP:
                player.up_pressed = False
            if event.key == pygame.K_DOWN:
                player.down_pressed = False

    screen.fill((12, 24, 36))
    
    player.player_draw(player_img)
    player.enemy_draw(enemy_img)

    player.update()
    player.update_enemy()
    pygame.display.flip()

    clock.tick(500)
