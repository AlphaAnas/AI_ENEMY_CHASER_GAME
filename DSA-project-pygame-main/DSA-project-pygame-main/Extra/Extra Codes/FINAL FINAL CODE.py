import pygame
from sys import exit
import random
from random import randint
from pygame import mixer

# game loop
# one while loop which runs when the player moves
# collision of cheese and player score add
# collision of enemy and player game end
# one place where the enemy position resets, so that 
# game is more fun!
# lastly, keeping all positions updated!\

#updated=> need to add wall rectangle so player cannot pass'em
# all the boxes in grids should have some weight according to background image so more/less weight in steep slopes.
# player should move according to the box. 

width , height = 600 , 670
pygame.init() #initialize
screen = pygame.display.set_mode((width,height)) #displaysurface (width,height)
pygame.display.set_caption('Chase Up!')
clock = pygame.time.Clock() #clock for constant frame rate
game_active = False # intro and gameover are same!
start_time = 0
score = 0
x_speed = 0 ; y_speed = 0
enemyx = 0 ; enemyy = 0
test_font = pygame.font.SysFont('Comic Sans MS', 30)

# wall=pygame.image.load('wall.jpg').convert_alpha()
# wall=pygame.transform.scale(wall, (65,65))
# wall_rec = wall.get_rect(topright=(300,300)) 
# is there need for wall?
# maybe not wall lekan there is ig need for some obstacles!

player_surface = pygame.image.load('Final Game/Assets/player.png').convert_alpha()
player_surface = pygame.transform.scale(player_surface, (100,100))
player_rectangle = player_surface.get_rect(center=(width//2, height//2))

name_surface = test_font.render('Press Space To Start!',False,(111,196,169))
name_rectangle = name_surface.get_rect(center = (300,200))

enemy_surface = pygame.image.load('Final Game/Assets/enemy.png').convert_alpha()
enemy_surface = pygame.transform.scale(enemy_surface, (80,80))
# enemy_rectangle = enemy_surface.get_rect(topleft = (random.randint(0,536),random.randint(0,350)))

food_surface = pygame.image.load('Final Game/Assets/coin.png').convert_alpha()
food_surface = pygame.transform.scale(food_surface,(35,65))
food_rectangle = food_surface.get_rect(center = (500,500))

background_surface = pygame.image.load('Final Game/Assets/background.jpg').convert()
background_surface = pygame.transform.scale(background_surface,(610,610))

background_colour = pygame.Surface((600,670)) #(w,h)
background_colour.fill('coral') #typeofcolor

# add game sound
mixer.music.load("Final Game/Assets/backgroundm.mp3") 
mixer.music.play(-1)
caught =mixer.Sound("Final Game/Assets/caught.wav") 
coin = mixer.Sound("Final Game/Assets/coinm.wav")

rows = 25
col = 25
box_width =  width // col
box_height = height // rows

running = True
#make grid
# no need to make grid, we need to have an already existing grid with all the 1's and 0's.
matrix=[]
for i in range(col):
    arr = [None]*rows
    
    matrix.append(arr)

def ending(): #ending messagge
  # NOT ENDING THE GAME! JUST RESETTING IT YA
  end_msg = test_font.render(f'You got caught !',True,(64,0,0))
  score_surface = test_font.render(f'Score : {score}',False,(64,64,64))
  score_rectangle = score_surface.get_rect(center = (400,310))
  screen.blit(score_surface,score_rectangle)
  screen.blit(end_msg, (350, 350))

def draw_rec(x,y, display, color): # rec= #(x coordinate, y-coordinate(where to start), widht, height)
     pygame.draw.rect(display, color, (x, y,box_width-2, box_height-2), 0)

while running:

    for event in pygame.event.get():

        if event.type == pygame.QUIT: #quit
            pygame.quit() #exit loop when window is closed # opposite of pygame.init()
            exit() #breaks while True loop

        if game_active:
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT:

                    #player_rectangle.x -= 8
                    x_speed= -8 ; y_speed = 0
                if event.key == pygame.K_RIGHT :

                    #player_rectangle.x += 8
                    x_speed = 8 ; y_speed = 0
                if event.key == pygame.K_UP:
            
                    #player_rectangle.y -= 8
                    y_speed = -8 ; x_speed = 0 
                if event.key == pygame.K_DOWN:
                    #player_rectangle.y += 8
                    y_speed = 8 ; x_speed = 0 

        else:
            if event.type == pygame.KEYUP and event.key == pygame.K_SPACE:
                score = 0
                food_rectangle.center = (randint(0,600),randint(0,600))
                enemy_rectangle = enemy_surface.get_rect(topleft = (random.randint(0,536),random.randint(0,350)))
                if player_rectangle.colliderect(enemy_rectangle) or food_rectangle.colliderect(enemy_rectangle):
                    enemy_rectangle = enemy_surface.get_rect(topleft = (random.randint(0,536),random.randint(0,350)))
                game_active = True
    # Need to have a grid where, the player only moves on 0s and when 1 comes then he stops!
    if game_active:

        screen.blit(background_colour,(0,0))
        screen.blit(background_surface,(-4,0))
        screen.blit(player_surface,player_rectangle)
        screen.blit(enemy_surface,enemy_rectangle)
        screen.blit(food_surface,food_rectangle)
        
        # score
        score_surface = test_font.render(f'Score : {score}',False,(64,64,64))
        score_rectangle = score_surface.get_rect(center = (300,640))
        screen.blit(score_surface,score_rectangle)

        pygame.draw.line(screen,'black',(0,611),(600,611),7)
        # screen.blit(wall, wall_rec)
        player_rectangle.x += x_speed ; player_rectangle.y += y_speed

        # adding the grid on the image

        # for i in range(col):
        #     for j in range(rows):
        #     #calculating the box size
        #         x=i*box_width
        #         y=j*box_height
        #         draw_rec(x,y, screen, (64,0,0))
        
        # if enemy hits boundary then its movement starts in opposite direction
        if player_rectangle.x<0:
            player_rectangle.x=550
        elif player_rectangle.x>=550:
            player_rectangle.x = 0
        if player_rectangle.y <0:
            player_rectangle.y =550
        elif player_rectangle.y >550:
            player_rectangle.y = 0

        # collision
        if player_rectangle.colliderect(enemy_rectangle):
            player_rectangle.x = width//2 ; x_speed=0 ; y_speed = 0
            caught.play()
            #ending()
            game_active = False
            #pygame.display.update()
            #pygame.time.delay(500)
            #break
            
        if player_rectangle.colliderect(food_rectangle):
            food_rectangle.center = (randint(0,600),randint(0,600))
            score += 1
            coin.play()
        # if score != 0:
        #     score_surface = test_font.render(f'Score : {score}',False,(64,64,64))
        #     score_rectangle = score_surface.get_rect(center = (300,620))
        #     screen.blit(score_surface,score_rectangle)

    else: # before starting of game # and after ending as well
        screen.fill((94,129,162))
        screen.blit(name_surface,name_rectangle)
        if score != 0:
            end_msg = test_font.render(f'You Got Caught!!!',True,(64,0,0))
            end_msg_rectangle = end_msg.get_rect(center=(300, 350))
            screen.blit(end_msg, end_msg_rectangle)

    pygame.display.update()
    clock.tick(60)

game_active = False