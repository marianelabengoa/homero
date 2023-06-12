import pygame
import sys
import random
from dona import*
from config import *

# ANCHO = 800
# ALTO = 600
# CENTER=(ANCHO//2,ALTO//2)
# NEGRO=(0,0,0)
# BLANCO=(250,250,250)
# RANDOM=(200,150,120)
# CIAN=(0,255,255)
# MAGENTA=(255,0,255)
# AMARILLO=(255,255,0)
# ROJO=(255,0,0)
# COLOR=(171,171,190)
# TITO=(200,171,117)
# POMELO=(182,101,121)
# FPS=60
# fall=True
# right=True
# SPEED=60
# SPEED2=5


pygame.init()

display = pygame.display.set_mode((ANCHO, ALTO))
pygame.display.set_caption(" donuts war")


icono=pygame.image.load("./assets/imagenes/dona.png").convert_alpha()
icono=pygame.transform.scale(icono, SIZE_ICON)
pygame.display.set_icon(icono)


fondo=pygame.image.load("./assets/imagenes/background.jpg").convert()
fondo=pygame.transform.scale(fondo,SIZE)


homero_l=pygame.image.load("./assets/imagenes/homer_left.png").convert_alpha()
homero_l=pygame.transform.scale(homero_l, HOMERO_SIZE)
rect_homero=homero_l.get_rect()
rect_homero.midbottom=(CENTER_X, DISPLAY_BOTTOM)
homero=homero_l


homero_r=pygame.image.load("./assets/imagenes/homer_right.png").convert_alpha()
homero_r=pygame.transform.scale(homero_r, HOMERO_SIZE)
# rect_homero=homero_r.get_rect()
# rect_homero.midbottom=(CENTER_X, DISPLAY_BOTTOM)


rect_boca=pygame.rect.Rect(0,0,50,10)
rect_boca.x=rect_homero.x+30
rect_boca.y=rect_homero.y+128


donas=[]

for i in range(10):
    dona=Dona(DONUT_SIZE,(random.randrange(30, ANCHO-30), random.randrange(-1000,0)),"./assets/imagenes/dona.png")
    donas.append(dona)


sonido=pygame.mixer.music.load("./assets/sonido/ouch.mp3")

fuente=pygame.font.Font("./assets/font/simpsons.ttf", 48)


while True:

    clock.tick(FPS)
    display.blit(fondo, ORIGIN)

    for evento in pygame.event.get():
        if evento.type ==pygame.QUIT:
            pygame.quit()
            sys.exit()
        
        key=pygame.key.get_pressed()

        display.blit(fondo, (0,0))
        # homero=homero_r
        # rect_homero=rect_homero_r
        

        if key[pygame.K_LEFT]:
            if rect_homero.left>DISPLAY_LEFT:
                rect_homero.x-=HOMERO_SPEED
                homero=homero_l
                rect_boca.x=rect_homero.x+30
                rect_boca.y=rect_homero.y+128

            
        if key[pygame.K_RIGHT]:
            if rect_homero.right<=DISPLAY_RIGHT:
                rect_homero.x+=HOMERO_SPEED
                homero=homero_r
                rect_boca.x=rect_homero.x+80
                rect_boca.y=rect_homero.y+128


    pygame.draw.rect(display, ROJO, rect_boca)
    display.blit(fondo, (0,0))
    display.blit(homero, rect_homero)
    
    display.blit(fuente.render("Score: " + str(score), True, NEGRO), (50,50))


    for dona in donas:
        if dona.rect.bottom<=DISPLAY_BOTTOM:
            if dona.active:
                dona.update() 
            else:
                dona.rect.y=0

        if rect_boca.colliderect(dona.rect):
            dona.active=False
            if flag_sound:
                score+=1
                pygame.mixer.music.play()
                pygame.mixer.music.set_pos(0.2)
                flag_sound=False
            else:
                flag_sound=True

        if dona.active:
            display.blit(dona.imagen, dona.rect)

    pygame.display.flip() # muestra la pantalla # set-executionpolicy unrestricted