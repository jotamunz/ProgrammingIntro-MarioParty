import pygame
import pygame.mixer
import random
import sys

#========================

# VARIABLES GLOBALES

#========================

# BOARD = [[0,0,0,0,0,0,0,0,0,0],
#          [0,0,0,0,0,0,0,0,0,0],
#          [0,0,0,0,0,0,0,0,0,0],
#          [0,0,0,0,0,0,0,0,0,0],
#          [0,0,0,0,0,0,0,0,0,0],
#          [0,0,0,0,0,0,0,0,0,0],
#          [0,0,0,0,0,0,0,0,0,0],
#          [0,0,0,0,0,0,0,0,0,0],
#          [0,0,0,0,0,0,0,0,0,0],
#          [0,0,0,0,0,0,0,0,0,0]]

LISTA_IMAGENES = ["Guess_who/Imagenes_Guess_Who/Paper_Mario.png","Guess_who/Imagenes_Guess_Who/Luigi.png",
                  "Guess_who/Imagenes_Guess_Who/Baby_Mario.png","Guess_who/Imagenes_Guess_Who/Dry_Bones.png",
                  "Guess_who/Imagenes_Guess_Who/Bowser_Jr.png","Guess_who/Imagenes_Guess_Who/Boo.png",
                  "Guess_who/Imagenes_Guess_Who/Bowser.png","Guess_who/Imagenes_Guess_Who/Koopa.png",
                  "Guess_who/Imagenes_Guess_Who/Daisy.png","Guess_who/Imagenes_Guess_Who/Donkey_Kong.png",
                  "Guess_who/Imagenes_Guess_Who/Mario.png","Guess_who/Imagenes_Guess_Who/Peach.png",
                  "Guess_who/Imagenes_Guess_Who/Toad.png","Guess_who/Imagenes_Guess_Who/Yoshi.png",
                  "Guess_who/Imagenes_Guess_Who/Goomba.png"]

RESULTADO = 0

#========================

# ALGORITMOS GUESS WHO

#========================

def get_posMatriz(pos):
    if pos< 50:
        return 0
    else:
        return 1 + get_posMatriz(pos-50)

def print_b(board):
    for i in board:
        print (i)

def contar_1(BOARD):
    res = 0
    for f in range(len(BOARD)):
        for c in range(len(BOARD[0])):
            if BOARD[f][c] == 1:
                res += 1
    return res
#========================

#   GUI DE GUESS WHO

#========================

def displayText(text, font, color, location, screen):
    textSurface = font.render(text, True, color)
    textRect = textSurface.get_rect()
    textRect.center = location
    screen.blit(textSurface, textRect)


def Button(message,font, x, y, w, h, color, hover, pos, screen, action=None):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    if (x + w) > mouse[0] > x and (y + h) > mouse[1] > y:
        displayText(message, font, hover, pos, screen)
        if click[0] == 1 and action != None:
            action()
    else:
        displayText(message, font, color, pos, screen)

def gane():
    global RESULTADO
    RESULTADO = True

def pierde():
    global RESULTADO
    RESULTADO = False

def dibujar_cuadros(imagen,screen,BOARD):
    posx = -50
    posy = -50
    for f in range(len(BOARD)):
        posy += 50
        for c in range(len(BOARD[0])):
            posx += 50
            if BOARD[f][c] == 0:
                screen.blit(imagen,(posx,posy))
        posx = -50
    pygame.display.update()

def dibujar_textos(font, screen, imagen_ganadora):
    lista_imagenes_temp = LISTA_IMAGENES.copy()
    for i in range(len(LISTA_IMAGENES)):
        personaje = LISTA_IMAGENES[i]
        lista_imagene_temp = lista_imagenes_temp.remove(personaje)
        pygame.draw.rect(screen, (255, 150, 100),pygame.Rect(600, i*33, 300, 32))
        if personaje == imagen_ganadora:
            personaje = personaje.replace('Guess_who/Imagenes_Guess_Who/',".png")
            Button(personaje.strip('.png'),font, 600, i*33, 600, 33, (255,255,255), (0,0,0), (750,(i*33)+15), screen, gane)
        else:
            personaje = personaje.replace('Guess_who/Imagenes_Guess_Who/',".png")
            Button(personaje.strip('.png'),font, 600, i*33, 600, 33, (255,255,255), (0,0,0), (750,(i*33)+15), screen, pierde)
            

#========================

# ACCIONES DE GUESS WHO

#========================


def quitar_cuadro(BOARD):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    if click[0] == 1 and mouse[1]  < 500 and mouse[0]  < 500:
        BOARD[get_posMatriz(mouse[1])][get_posMatriz(mouse[0])] = 1
        #print_b(BOARD)


#========================

#   INTERFAZ GRAFICA

#========================

def pantalla():
    global LISTA_IMAGENES, RESULTADO

    BOARD = [[0,0,0,0,0,0,0,0,0,0],
         [0,0,0,0,0,0,0,0,0,0],
         [0,0,0,0,0,0,0,0,0,0],
         [0,0,0,0,0,0,0,0,0,0],
         [0,0,0,0,0,0,0,0,0,0],
         [0,0,0,0,0,0,0,0,0,0],
         [0,0,0,0,0,0,0,0,0,0],
         [0,0,0,0,0,0,0,0,0,0],
         [0,0,0,0,0,0,0,0,0,0],
         [0,0,0,0,0,0,0,0,0,0]]

    RESULTADO = 5

    pygame.init()  # comando de correr modulo pygae

    pygame.mixer.music.load("Guess_who/Sonidos_Who/Winter.mp3")
    pygame.mixer.music.set_volume(0.5)
    pygame.mixer.music.play(-1)

    game_over = False

    width = 1000
    height = 500

    size = (width, height)
    screen = pygame.display.set_mode((width, height))#tamano de la pantalla

    bg = pygame.image.load("Guess_who/Imagenes_Guess_Who/bg.jpg")
    bg = pygame.transform.scale(bg,size)
    bloque = pygame.image.load("Guess_who/Imagenes_Guess_Who/bloque.png")
    bloque = pygame.transform.scale(bloque,(50,50))
    sonido_bloque = pygame.mixer.Sound("Guess_who/Sonidos_Who/bloque.wav")

    screen.blit(bg,(0,0))
    pygame.display.update() # imprime en pantalla los datos que la ventana contiene

    myfont = pygame.font.SysFont("Arial", 25) # declaracion de la fuente

    imagen_escondida = random.choice(LISTA_IMAGENES)
    Imagen = pygame.image.load(imagen_escondida)
    Imagen = pygame.transform.scale(Imagen,(200,200))
    
    posx_iamgen = random.randint(0,300)
    posy_iamgen = random.randint(0,300)

    limite_clicks = random.randint(4,8)

    

    termino = False

    while not(termino): #loop del juego

        screen.blit(bg,(0,0))
        dibujar_textos(myfont, screen, imagen_escondida)
        #boton1 = Button("hola", myfont, 575, 300, 50, 50, (255,255,255), (0,0,0), (600,300), screen)
        screen.blit(Imagen,(posx_iamgen,posy_iamgen))
        dibujar_cuadros(bloque,screen,BOARD)
        pygame.display.update()

        if RESULTADO == True:
            pygame.mixer.music.stop()
            print("You win guess who")
            return True

        if RESULTADO == False:
            pygame.mixer.music.stop()
            print("You lose guess who")
            return False
        
        if contar_1(BOARD) < limite_clicks:
            #sonido_bloque.play()
            quitar_cuadro(BOARD)
        
        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                pygame.display.quit()
                pygame.quit()
                sys.exit()
