import pygame #module
from sys import exit
white = (255, 255, 255) #R G B
black = (0, 0, 0)
red = (255, 0, 0)
pygame.init() #initialize
screen = pygame.display.set_mode((800,400)) #displaysurface (width,height)
pygame.display.set_caption('minor problems') #title of game
clock = pygame.time.Clock() #clock for constant frame rate
test_font = pygame.font.Font('font/Pixeltype.ttf',50) #fontregular (style,size)

#test_surface = pygame.Surface((800,400)) #regularsurface (w,h)
#test_surface.fill('coral') #Plain colour regularsurface

#red = pygame.Surface((100,200)) #(w,h)
#red.fill('Red') #typeofcolor

sky_surface = pygame.image.load('graphics/Sky.png').convert() #imageregularsurface
ground_surface = pygame.image.load('graphics/ground.png').convert()

text_surface = test_font.render('Look at em go!!!',False,'coral') #textregularsurface (prompt,AA,color)

snail_surface = pygame.image.load('graphics/snail/snail1.png').convert_alpha() #snailenemy
#snail_x_pos = 800 #original position
#snail_y_pos = 265 #original position
snail_rectangle = snail_surface.get_rect(midbottom = (800,300))

player_surface = pygame.image.load('graphics/player/player_walk_1.png').convert_alpha() #player
player_rectangle = player_surface.get_rect(midbottom = (80,280)) #player rectangle #midbottom , topleft , etc...
#sprite class makes this better
x1 = 300
y1 = 300
 
x1_change = 0       
y1_change = 0
while True: #all game inside loop

    #event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT: #quit
            pygame.quit() #exit loop when window is closed # opposite of pygame.init()
            exit() #breaks while True loop

        if event.type == pygame.MOUSEMOTION:
            mouse_position = event.pos #alternate way to get mouse position

        if event.type == pygame.KEYDOWN: #key pressed
            if event.key == pygame.K_LEFT:
                x1_change = -10
                y1_change = 0
            elif event.key == pygame.K_RIGHT:
                x1_change = 10
                y1_change = 0
            elif event.key == pygame.K_UP:
                y1_change = -10
                x1_change = 0
            elif event.key == pygame.K_DOWN:
                y1_change = 10
                x1_change = 0
    x1 += x1_change
    y1 += y1_change
    screen.fill(white)
    pygame.draw.rect(screen, black, [x1, y1, 10, 10])
            
        # if event.type == pygame.MOUSEBUTTONUP: #released
        #     print('released mouse button')
        # elif event.type == pygame.MOUSEBUTTONDOWN:#pushed
        #     print("pressed mouse button")
    
    #displaying images
    #screen.blit(test_surface,(0,0))
    #screen.blit(red,(200,100))
    screen.blit(sky_surface,(0,0))
    screen.blit(ground_surface,(0,300))
    screen.blit(text_surface,(300,170))

    #animations
    screen.blit(snail_surface,snail_rectangle)
    snail_rectangle.right -= 5
    if snail_rectangle.right < -50:
        snail_rectangle.right = 900
    #print(snail_rectangle.right)
    #snail_x_pos -= 10 #speed
    #snail_y_pos -= 10
    #if snail_x_pos < -50: #if outside of screen, return
    #    snail_x_pos = 800 #original position

    #rectangles
    screen.blit(player_surface,player_rectangle) #rectangle used for positioning instead of tuple which is always topleft
    #rectangle also used for moving player
    player_rectangle.left += 10 #rectangle moving which also moves the player (surface)
    #print(player_rectangle.left)
    if player_rectangle.left > 850:
        player_rectangle.left = -10

    #collision detection
    #rectanges help in collision detection
    if player_rectangle.colliderect(snail_rectangle):
        print('snail collision!')
    if player_rectangle.collidepoint(mouse_position): #mouse position from event loop
        print('player collision!')
    #another way of collision detection is rec1.collidepoint((x,y))
    # mouse_position = pygame.mouse.get_pos() #tuple returning x,y
    # if player_rectangle.collidepoint(mouse_position): #if mouse touching player surface (rectangle)
        # print('collision!')
        # print(pygame.mouse.get_pressed()) #tuple of mouse button pressed or no?

    #drawing with rectangles (+colors) 1:14:00
    

    pygame.display.update() #updates screen every frame
    clock.tick(60) #60fps