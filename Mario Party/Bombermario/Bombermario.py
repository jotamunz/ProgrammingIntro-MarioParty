import pygame
import pygame.mixer
import random
import sys

#========================

# VARIABLES GLOBALES

#========================

BOARD = []

#========================

# ALGORITMOS BOMBERMARIO

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
    global BOARD
    res = 0
    for f in range(len(BOARD)):
        for c in range(len(BOARD[0])):
            if BOARD[f][c] == 1:
                res += 1
    return res

def get_posMatriz(pos):
    if pos< 50:
        return 0
    else:
        return 1 + get_posMatriz(pos-50)

def es_limite(fil,col):
    #print(fil)
    #print((len(BOARD)-1))
    if fil == (len(BOARD)-1) or col ==  (len(BOARD[0])-1):
        return True
    return False

def colocar_estrella():
    global BOARD
    posx = random.randint(0,len(BOARD[0])-2)
    posy = random.randint(0,(len(BOARD)-2))
    BOARD[posx][posy] = "E"
    BOARD[posx+1][posy] = "E"
    BOARD[posx][posy+1] = "E"
    BOARD[posx+1][posy+1] = "E"


def localizar_estrella():
    for f in range(len(BOARD)):
        for c in range(len(BOARD[0])):
            if BOARD[f][c] == "E":
                return [c*50,f*50]

def gana():
    for f in range(len(BOARD)):
        for c in range(len(BOARD[0])):
            if BOARD[f][c] == "E":
                print("You lose bombermario")
                return False
    print("You win bombermario")
    return True
            
#========================

#   GUI DE BOMBERMARIO

#========================

def dibujar_cuadros(imagen,screen):
    posx = -50
    posy = -50
    for f in range(len(BOARD)):
        posy += 50
        for c in range(len(BOARD[0])):
            posx += 50
            if BOARD[f][c] == 0 or BOARD[f][c] == "E":
                screen.blit(imagen,(posx,posy))
        posx = -50
    pygame.display.update()
          
#========================

# ACCIONES DE BOMBERMARIO

#========================


def quitar_cuadro():
    global BOARD
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    if click[0] == 1 and not(es_limite(get_posMatriz(mouse[1]),get_posMatriz(mouse[0]))):
        BOARD[get_posMatriz(mouse[1])][get_posMatriz(mouse[0])] = 1
        BOARD[get_posMatriz(mouse[1])+1][get_posMatriz(mouse[0])] = 1
        BOARD[get_posMatriz(mouse[1])][get_posMatriz(mouse[0])+1] = 1
        BOARD[get_posMatriz(mouse[1])+1][get_posMatriz(mouse[0])+1] = 1
        #print_b(BOARD)

#========================

#   INTERFAZ GRAFICA

#========================

def pantalla():
    global BOARD

    dimensiones = random.choice([10,15,20])
    BOARD = create_board(dimensiones,dimensiones)
    colocar_estrella()

    pygame.mixer.pre_init(44100,16,2,4096)

    pygame.init()  # comando de correr modulo pygae

    pygame.mixer.music.load("Bombermario/Sonidos_Bomber/Mozart.mp3")
    pygame.mixer.music.set_volume(0.4)
    pygame.mixer.music.play(-1)

    game_over = False

    width = dimensiones*50
    height = dimensiones*50

    size = (width, height)
    screen = pygame.display.set_mode((width, height))#tamano de la pantalla

    bg = pygame.image.load("Bombermario/Imagenes_Bomber/bg.jpg")
    bg = pygame.transform.scale(bg,size)
    bloque = pygame.image.load("Bombermario/Imagenes_Bomber/bloque.png")
    bloque = pygame.transform.scale(bloque,(50,50))
    estrella = pygame.image.load("Bombermario/Imagenes_Bomber/estrella.png")
    estrella = pygame.transform.scale(estrella,(100,100))
    bomba = pygame.image.load("Bombermario/Imagenes_Bomber/bomba.png")
    bomba = pygame.transform.scale(bomba,(50,50))
    sonido_bomba = pygame.mixer.Sound("Bombermario/Sonidos_Bomber/Bomba.wav")
    sonido_bomba.set_volume(0.1)

    screen.blit(bg,(0,0))
    pygame.display.update() # imprime en pantalla los datos que la ventana contiene

    myfont = pygame.font.SysFont("Arial", 25) # declaracion de la fuente
    

    limite_clicks = 10
    cantidad_clicks = 0
    
    print_b(BOARD)
    termino = False
    done = False

    ubicacion = localizar_estrella()

    while not(done): #loop del juego

        mx,my = pygame.mouse.get_pos()

        screen.blit(bg,(0,0))
        screen.blit(estrella,(ubicacion[0],ubicacion[1]))
        dibujar_cuadros(bloque,screen)
        screen.blit(bomba,(mx-25,my-25))
        pygame.display.update()

        if pygame.mouse.get_pressed()[0] == 1:
            sonido_bomba.play()
            cantidad_clicks += 1
            if cantidad_clicks <= limite_clicks:
                quitar_cuadro()

            
        
        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                pygame.mixer.music.stop()
                #pygame.display.quit()
                #pygame.quit()
                return gana()

