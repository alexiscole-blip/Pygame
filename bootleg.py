from curses import KEY_DOWN
from tkinter import Canvas
import pygame
from sys import exit

#The basics
pygame.init()
screen = pygame.display.set_mode((800,400))
pygame.display.set_caption('Runner')
clock = pygame.time.Clock()
test_font = pygame.font.Font('font/Pixeltype.ttf', 50)

#Background aka play surface
Sky_Surface = pygame.image.load('graphics/Sky.png').convert()
Ground_Surface = pygame.image.load('graphics/Ground.png').convert()

text_Surface = test_font.render('Fuck ya!', False, 'Black').convert()
score_rect = text_Surface.get_rect(midtop = (400, 50))

#snail
snail_Surface = pygame.image.load('graphics/snail/snail1.png').convert_alpha()
snail_rect = snail_Surface.get_rect(midbottom = (100,300))

#player
player_surf = pygame.image.load('graphics/player/player_walk_1.png').convert_alpha()
player_rect = player_surf.get_rect(midbottom = (80,300))
player_gravity = 0

player_colliding = False

max_health = 100
current_health = max_health
 

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        # if event.type == pygame.MOUSEBUTTONDOWN:
        #    if  player_rect.collidepoint(event.pos):print('oops')
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                if player_rect.bottom == 300:
                    player_gravity = -25
                



    screen.blit(Sky_Surface,(0,0))
    screen.blit(Ground_Surface,(0,300))

    pygame.draw.rect(screen, "pink", score_rect, 5, 3)
    screen.blit(text_Surface, score_rect)

   # pygame.draw.line(screen, 'purple', (0,0), pygame.mouse.get_pos()) 

   #health bar
    health_status = pygame.draw.rect(screen, 'green', (150, 100, 400*current_health/max_health, 30))

    pygame.draw.ellipse(screen, (255,255,0), pygame.Rect(0, 0, 100, 100))
   
   #snail movement
    snail_rect.right += - 4
    if snail_rect.right < -10:
        snail_rect.right = 850
    screen.blit(snail_Surface, snail_rect)

    #player movement
    player_gravity += 1
    player_rect.top += player_gravity
    if player_rect.bottom > 300: player_rect.bottom = 300
    
    screen.blit(player_surf,player_rect)
    
    #player and snail collision
    if player_rect.colliderect(snail_rect):
        current_health -= 3
        print(current_health)
        pygame.draw.rect(screen, 'red', player_rect)


        # if player_colliding == False:
        #     player_colliding = True
        #     print("he ded x(")
        #     player_health -= 3
        #     pygame.draw.rect(screen, "red", player_rect)
        #     print(player_life)
        # if player_colliding == False:
        #     player_colliding = False
        #     print('he is alive')
        #     player_health += 1
        

    else: 
        player_colliding = False



    
#Do not edit, this is the pixels
    pygame.display.update()
    clock.tick(60)
    
