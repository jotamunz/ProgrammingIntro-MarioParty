import pygame
import pygame.mixer
import random
import sys
import time

#========================

# VARIABLES GLOBALES

#========================

BOARD_INTERFAZ = []
BOARD_JUEGO = []
CONTADOR = 0

#========================

# ALGORITMOS COLLECT COINS

#========================

def create_board(filas,columnas): 
    board = []
    for f in range(filas):
        board.append([])
        for c in range(columnas):
            board[f].append(0)
    return board

def print_b(board):
    for i in board:
        print (i)

def contar_1():
    global BOARD_INTERFAZ
    res = 0
    for f in range(len(BOARD_INTERFAZ)):
        for c in range(len(BOARD_INTERFAZ[0])):
            if BOARD_INTERFAZ[f][c] == 1:
                res += 1
    return res

def get_posMatriz(pos):
    if pos< 25:
        return 0
    else:
        return 1 + get_posMatriz(pos-25)

#========================

#   MATRIZ DE COLLECT COINS

#========================

def dibujar_cuadros(imagen,screen):
    posx = -25
    posy = -25
    for f in range(len(BOARD_INTERFAZ)):
        posy += 25
        for c in range(len(BOARD_INTERFAZ[0])):
            posx += 25
            if BOARD_INTERFAZ[f][c] == 0:
                screen.blit(imagen,(posx,posy))
        posx = -25
    #pygame.display.update()

def dibujar_monedas(monedas_buenas,monedas_malas ,screen):
    posx = -25
    posy = -25
    for f in range(len(BOARD_JUEGO)):
        posy += 25
        for c in range(len(BOARD_JUEGO[0])):
            posx += 25
            if BOARD_JUEGO[f][c] > 0:
                screen.blit(monedas_buenas,(posx,posy))
            elif BOARD_JUEGO[f][c] < 0:
                screen.blit(monedas_malas,(posx,posy))
                
        posx = -25
    #pygame.display.update()

def llenar_cuadros():
    global BOARD_JUEGO
    for f in range(len(BOARD_JUEGO)):
        for c in range(len(BOARD_JUEGO[0])):
            BOARD_JUEGO[f][c] = random.randint(-10,10)

def quitar_cuadro():
    global BOARD_INTERFAZ
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    if click[0]:
        BOARD_INTERFAZ[get_posMatriz(mouse[1])][get_posMatriz(mouse[0])] = 1
        #print_b(BOARD_INTERFAZ)

def recoger_moneda():
    global BOARD_JUEGO,CONTADOR,BOARD_INTERFAZ
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    if click[0]:
        if BOARD_INTERFAZ[get_posMatriz(mouse[1])][get_posMatriz(mouse[0])] == 0:
            CONTADOR += BOARD_JUEGO[get_posMatriz(mouse[1])][get_posMatriz(mouse[0])]
          
#========================

#   INTERFAZ GRAFICA

#========================

def pantalla():
    global BOARD_INTERFAZ,BOARD_JUEGO,CONTADOR

    BOARD_INTERFAZ = []
    BOARD_JUEGO = []
    CONTADOR = 0

    BOARD_INTERFAZ = create_board(25,25)
    BOARD_JUEGO = create_board(25,25)

    llenar_cuadros()
    #print_b(BOARD_JUEGO)

    pygame.init()  # comando de correr modulo pygae

    pygame.mixer.music.load("Collect_coins/Sonidos_Coin/Price.mp3")
    pygame.mixer.music.set_volume(0.5)
    pygame.mixer.music.play(-1)

    game_over = False

    width = 25**2
    height = 25**2

    size = (width, height+100)
    screen = pygame.display.set_mode((width, height+100))#tamano de la pantalla

    bloque = pygame.image.load("Collect_coins/Imagenes_Collect/bloque.png")
    bloque = pygame.transform.scale(bloque,(25,25))

    monedas_buenas = pygame.image.load("Collect_coins/Imagenes_Collect/GoodCoin.png")
    monedas_buenas = pygame.transform.scale(monedas_buenas,(25,25))

    monedas_malas = pygame.image.load("Collect_coins/Imagenes_Collect/BadCoin.png")
    monedas_malas = pygame.transform.scale(monedas_malas,(25,25))

    sonido_moneda = pygame.mixer.Sound("Collect_coins/Sonidos_Coin/coin.wav")
    sonido_moneda.set_volume(0.1)
    

    pygame.display.update() # imprime en pantalla los datos que la ventana contiene

    myfont = pygame.font.SysFont("Arial", 25) # declaracion de la fuente

    iniTime = time.time()
    timer = 0
    maxTime = random.choice([30,45,60])  

    print_b(BOARD_JUEGO)
    termino = False
    R = 0
    G = 128
    G1 = 1
                
    while timer < maxTime:
        #print(timer)
        
        endTime = time.time()
        timer = endTime - iniTime
            
            
        #mx,my = pygame.mouse.get_pos()
            
        #cambia color de fondo
        screen.fill((R,G,0))
        if R == 255:
            R1 = -1
        elif R == 0:
            R1 = 1
        R += R1
        if G == 255:
            G1 = -1
        elif G == 0:
            G1 = 1
        G += G1
        
        
        label = myfont.render("Monedas: " + str(CONTADOR),True,(0,0,0))
        screen.blit(label, (20, 633))
        
        label = myfont.render(str(int(maxTime-timer)),True,(0,0,0))
        screen.blit(label, (550, 633))

        dibujar_monedas(monedas_buenas,monedas_malas ,screen)
        dibujar_cuadros(bloque,screen)     
        pygame.display.update()
    
        if pygame.mouse.get_pressed()[0] == 1 and pygame.mouse.get_pos()[1] < 624:
            sonido_moneda.play()
            recoger_moneda()
            quitar_cuadro()

        #gana()
    
        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                pygame.display.quit()
                pygame.quit()
                sys.exit()
                
    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            pygame.display.quit()
            pygame.quit()
            sys.exit()
    #pygame.display.quit()
    #pygame.quit()
    if CONTADOR >= 0:
        pygame.mixer.music.stop()
        print("You win collect the coins")
        return True
    else:
        pygame.mixer.music.stop()
        print("You lose collect the coins")
        return False
