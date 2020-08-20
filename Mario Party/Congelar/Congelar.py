import pygame
import pygame.mixer
import random
import sys

# Entrada : (PLAYER_COUNT, mainPlayer, otherPlayer, otherPlayer2, otherPlayer3)


#========================

# VARIABLES GLOBALES

#========================

NUMERO_DE_JUGADORES = 2

LISTA_JUGADORES = []

RESULTADO = 0

JUGADOR = 0

#========================

# GUI DE ELEGIR_PERSONAJE

#========================

def displayText(text, font, color, location, screen):
    textSurface = font.render(text, True, color)
    textRect = textSurface.get_rect()
    textRect.center = location
    screen.blit(textSurface, textRect)

def Button(message,font, x, y, w, h, color, hover, pos, screen):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    pygame.draw.rect(screen, (114, 218, 253),pygame.Rect(x, y, w, h))
    if (x + w) > mouse[0] > x and (y + h) > mouse[1] > y:
        displayText(message, font, hover, pos, screen)
        if click[0] == 1:
            elegir_jugador(message)
    else:
        displayText(message, font, color, pos, screen)

def dibujar_textos(font, screen):
    lista_imagenes_temp = LISTA_JUGADORES.copy()
    for i in range(NUMERO_DE_JUGADORES-1):
        #print(NUMERO_DE_JUGADORES)
        jugador = LISTA_JUGADORES[i]
        Button(jugador,font, 400, (i*150) + 25, 550, 50, (255,255,255), (0,0,0), (1370/2,(i*150)+50), screen)

def elegir_jugador(jugador):
    global ELEGIDO, RESULTADO
    RESULTADO = True
    ELEGIDO = jugador
#========================

#   INTERFAZ GRAFICA

#========================

def pantalla(PLAYER_COUNT, mainPlayer, otherPlayer, otherPlayer2, otherPlayer3):

    global LISTA_JUGADORES, RESULTADO, ELEGIDO,NUMERO_DE_JUGADORES

    LISTA_JUGADORES = [otherPlayer, otherPlayer2, otherPlayer3]
    NUMERO_DE_JUGADORES = PLAYER_COUNT

    pygame.init()  # comando de correr modulo pygae

    pygame.mixer.music.load("Congelar/Sonidos_Congelar/congelar_musica.mp3")
    pygame.mixer.music.set_volume(0.5)
    pygame.mixer.music.play(-1)

    RESULTADO = False

    width = 1370
    height = 770
    size = (width, height)
    screen = pygame.display.set_mode((width, height))#tamano de la pantalla

    bg = pygame.image.load("Congelar/bg.jpg")
    bg = pygame.transform.scale(bg,size)

    screen.blit(bg,(0,0))
    pygame.display.update() # imprime en pantalla los datos que la ventana contiene

    myfont = pygame.font.SysFont("Arial", 50) # declaracion de la fuente

    termino = False

    while not(termino): #loop del juego

        screen.blit(bg,(0,0))
        dibujar_textos(myfont, screen)

        pygame.display.update()

        if RESULTADO == True:
            pygame.mixer.music.stop()
            return ELEGIDO

        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                pygame.display.quit()
                pygame.quit()
                sys.exit()
