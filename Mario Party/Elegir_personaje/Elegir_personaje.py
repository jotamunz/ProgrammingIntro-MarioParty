import pygame
import pygame.mixer
import random
import sys

#========================

# VARIABLES GLOBALES

#========================

LISTA_IMAGENES =  ["Elegir_personaje/Personajes/Mario.png","Elegir_personaje/Personajes/Luigi.png",
                  "Elegir_personaje/Personajes/Boo.png","Elegir_personaje/Personajes/Daisy.png",
                  "Elegir_personaje/Personajes/Bowser.png","Elegir_personaje/Personajes/Koopa.png",
                  "Elegir_personaje/Personajes/Dry_Bones.png","Elegir_personaje/Personajes/Peach.png",
                  "Elegir_personaje/Personajes/Toad.png","Elegir_personaje/Personajes/Yoshi.png"]
RESULTADO = 0

ELEGIDO = 0

IMAGEN = "Elegir_personaje/Personajes/Mario.png"

PERSONAJE = "Elegir_personaje/Personajes/Mario.png"

#========================

# ALGORITMOS ELEGIR_PERSONAJE

#========================

def contar_1():
    global BOARD
    res = 0
    for f in range(len(BOARD)):
        for c in range(len(BOARD[0])):
            if BOARD[f][c] == 1:
                res += 1
    return res
#========================

#   GUI DE ELEGIR_PERSONAJE

#========================

def displayText(text, font, color, location, screen):
    textSurface = font.render(text, True, color)
    textRect = textSurface.get_rect()
    textRect.center = location
    screen.blit(textSurface, textRect)


def Button(message,font, x, y, w, h, color, hover, pos, screen,personaje):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    if (x + w) > mouse[0] > x and (y + h) > mouse[1] > y:
        displayText(message, font, hover, pos, screen)
        if click[0] == 1:
            elegir_personaje(personaje)
    else:
        displayText(message, font, color, pos, screen)

def Button2(message,font, x, y, w, h, color, hover, pos, screen, action=None):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    pygame.draw.rect(screen, (29, 195, 96),pygame.Rect(x, y, w, h))
    if (x + w) > mouse[0] > x and (y + h) > mouse[1] > y:
        displayText(message, font, hover, pos, screen)
        if click[0] == 1 and action != None:
            action()
    else:
        displayText(message, font, color, pos, screen)

def Confirmar():
    global RESULTADO
    RESULTADO = True


    

def dibujar_textos(font, screen):
    lista_imagenes_temp = LISTA_IMAGENES.copy()
    for i in range(len(LISTA_IMAGENES)):
        personaje = LISTA_IMAGENES[i]
        lista_imagene_temp = lista_imagenes_temp.remove(personaje)
        pygame.draw.rect(screen, (255, 150, 100),pygame.Rect(1040, (i*50) + 25, 310, 42))
        personajeEdit = personaje.replace('Elegir_personaje/Personajes/', ".png")
        Button(personajeEdit.strip('.png'),font, 1040, (i*50) + 25, 600, 50, (255,255,255), (0,0,0), (1200,(i*50)+45), screen, personaje)
            

#========================

# ACCIONES DE ELEGIR_PERSONAJE

#========================

def elegir_personaje(personaje):
    global LISTA_IMAGENES, IMAGEN, PERSONAJE
    #num 0 - 14
    PERSONAJE = personaje
    imagen_escondida = personaje
    Imagen = pygame.image.load(imagen_escondida)
    Imagen = pygame.transform.scale(Imagen,(400,400))
    IMAGEN = Imagen

def elegir(num):
    global ELEGIDO
    print(pygame.mouse.get_pos())
    print(num)



#========================

#   INTERFAZ GRAFICA

#========================

def pantalla(PLAYER):
    global LISTA_IMAGENES, RESULTADO, ELEGIDO, IMAGEN

    RESULTADO = 5
    ELEGIDO = 0

    pygame.init()  # comando de correr modulo pygae

    pygame.mixer.music.load("Elegir_personaje/Elegir_musica/elegir_cancion.mp3")
    pygame.mixer.music.set_volume(0.5)
    pygame.mixer.music.play(-1)

    game_over = False

    width = 1370
    height = 770

    size = (width, height)
    screen = pygame.display.set_mode((width, height))#tamano de la pantalla

    bg = pygame.image.load("Elegir_personaje/Personajes/background.jpg")
    bg = pygame.transform.scale(bg,size)

    IMAGEN = pygame.image.load("Elegir_personaje/Personajes/Mario.png")
    IMAGEN = pygame.transform.scale(IMAGEN,(400,400))

    myfont = pygame.font.SysFont("Arial", 30) # declaracion de la fuente
    myfont2 = pygame.font.SysFont("Arial", 45) # declaracion de la fuente

    screen.blit(bg,(0,0))
    pygame.display.update() # imprime en pantalla los datos que la ventana contiene

    
    posx_iamgen = 350
    posy_iamgen = 200

    limite_clicks = random.randint(4,8)

    

    termino = False

    while not(termino): #loop del juego


        #1040, (i*50) + 25, 600, 50, (255,255,255), (0,0,0), (1200,(i*50)+50), screen, personaje
        
        
        screen.blit(bg,(0,0))
        displayText(PLAYER + " pick a character!", myfont2, (0, 0, 0), (550, 70), screen)
        Button2("Confirmar",myfont, 400, 640, 300, 50, (255,255,255), (0,0,0), (550,665), screen, Confirmar)
        dibujar_textos(myfont, screen)
        screen.blit(IMAGEN,(posx_iamgen,posy_iamgen))
        pygame.display.update()

        if RESULTADO == True:
            pygame.mixer.music.stop()
            return PERSONAJE
        
        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                pygame.display.quit()
                pygame.quit()
                sys.exit()
