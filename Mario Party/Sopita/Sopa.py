import pygame
import pygame.mixer
import random
import string
import copy
import time
import sys

#---------------------------
#   ALGORITMOS CARGADO
#---------------------------

# metodo para leer una archivo
# E: el path del archivo
# S: un string con el contenido del archivo


def guardar(archivo, strLista):
    fo = open(archivo, "w")
    # abre en forma de sobrrescribirlo,
    # si no existe lo crea
    fo.write(strLista)
    fo.close()

# metodo para leer una archivo
# E: el path del archivo
# S: un string con el contenido del archivo


def leer(archivo):
    fo = open(archivo, "r")
    # abre en forma
    # de solo lectura
    resultado = fo.read()
    fo.close()
    # retorna lo que leyo del archivo
    return resultado

# cargar archivo
# lee un archivo y hace las validaciones para colocarlo en la lista
# salida: retorna una lista de lo leido


def cargarArchivo(archivo):
    strResultado = leer(archivo)
    if strResultado != "":
        return eval(strResultado)
    else:
        return []

#========================

# VARIABLES GLOBALES

#========================


LISTA_PALABRAS = []
BOARD_INTERFAZ = []
BOARD_JUEGO = []
CONTADOR = 0

#========================

# ALGORITMOS SOPA

#========================


def create_board(filas, columnas):
    board = []
    for f in range(filas):
        board.append([])
        for c in range(columnas):
            board[f].append(0)
    return board


def print_b(board):
    for i in board:
        print(i)


def get_posMatriz(pos):
    if pos < 30:
        return 0
    else:
        return 1 + get_posMatriz(pos - 30)
#========================

#   GUI DE SOPA

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
        displayText(message, font, color, pos, screen)
        if click[0] == 1 and action != None:
            displayText(message, font, hover, pos, screen)
            action(pos[0],pos[1])
    else:
        displayText(message, font, color, pos, screen)

def displayPalabras(lista_palabras,font,color, posx, posy,screen):
    for elem in lista_palabras:
        posy += 30
        displayText(elem, font, color, (posx,posy), screen)

def dibujar_circulos(imagen,posx,posy,espacios, screen):
    pos_X = posx-15
    pos_Y = posy-15
    for f in range(len(BOARD_JUEGO)):
        pos_Y += espacios
        for c in range(len(BOARD_JUEGO[0])):
            pos_X += espacios
            if BOARD_JUEGO[f][c] == "X":
                screen.blit(imagen,(pos_X,pos_Y))
        pos_X = posx-15
        

#========================

#   MATRIZ DE SOPA

#========================


def dibujar_letras(pos_X, pos_Y,espacios, font,screen, action):
    posx = pos_X
    posy = pos_Y
    for f in range(len(BOARD_INTERFAZ)):
        posy += espacios
        for c in range(len(BOARD_INTERFAZ[0])):
            posx += espacios
            if BOARD_JUEGO[f][c] == 0:
                displayText(BOARD_INTERFAZ[f][c], font, (0,0,0),  (posx, posy), screen)
            else:
                Button(BOARD_INTERFAZ[f][c],font, posx -10, posy -10, 24, 24, (0,0,0), (255,255,255), (posx, posy), screen, action)
                #pygame.draw.rect(screen, (255,255,255), (posx -10, posy -10, 25, 25))
        posx = pos_X

def marcar_letra(posx,posy):
    global BOARD_JUEGO
    BOARD_JUEGO[ get_posMatriz(posy)-1][get_posMatriz(posx)-1] = "X"

def gana():
    global BOARD_JUEGO
    for f in range(len(BOARD_JUEGO)):
        for c in range(len(BOARD_JUEGO[0])):
            if BOARD_JUEGO[f][c] != 0 and BOARD_JUEGO[f][c] != "X":
                return False
    return True
   

def llenar_letras():
    global BOARD_INTERFAZ,BOARD_JUEGO
    for f in range(len(BOARD_INTERFAZ)):
        for c in range(len(BOARD_INTERFAZ[0])):
            if BOARD_JUEGO[f][c] == 0:
                BOARD_INTERFAZ[f][c] = random.choice(string.ascii_lowercase)
            else:
                BOARD_INTERFAZ[f][c] = BOARD_JUEGO[f][c]


#========================

# ALGORITMOS SOPA 2.0

#========================

def palabra_vertical(palabra,board1):
    global BOARD_JUEGO
    board = copy.deepcopy(board1)
    lista_letras = list(palabra)
    inicioY = random.randint(0,(len(board)) - len(palabra))
    inicioX = random.randint(0,(len(board[0])-1))
    for elem in lista_letras:
        if board[inicioY][inicioX] == 0 or board[inicioY][inicioX] == elem:
           board[inicioY][inicioX] = elem
           inicioY += 1
        else:
            return False
    return board

def palabra_horizontal(palabra,board1):
    global BOARD_JUEGO
    board = copy.deepcopy(board1)
    lista_letras = list(palabra)
    inicioX = random.randint(0,(len(board[0])) - len(lista_letras))
    inicioY = random.randint(0,(len(board)-1))
    for elem in lista_letras:
        if board[inicioY][inicioX] == 0 or board[inicioY][inicioX] == elem:
           board[inicioY][inicioX] = elem
           inicioX += 1
        else:
            return False
    return board

def palabra_diagonal(palabra,board1):
    global BOARD_JUEGO
    board = copy.deepcopy(board1)
    lista_letras = list(palabra)
    inicioX = random.randint(0,(len(board[0])) - len(lista_letras))
    inicioY = random.randint(0,(len(board[0])) - len(lista_letras))
    posInicial = inicioX
    for elem in lista_letras:
        if board[inicioY][inicioX] == 0 or board[inicioY][inicioX] == elem:
           board[inicioY][inicioX] = elem
           inicioX += 1
           inicioY += 1
        else:
            return False
    return [board,posInicial]

def palabra_diagonal_inver(palabra,board1):
    global BOARD_JUEGO
    board = copy.deepcopy(board1)
    lista_letras = list(palabra)
    inicioX = random.randint(0,(len(board[0])) - len(lista_letras))
    inicioY = random.randint(0,(len(board[0])) - len(lista_letras))
    #posInicial = inicioXY
    for elem in lista_letras:
        if board[inicioY][inicioX] == 0 or board[inicioY][inicioX] == elem:
           board[inicioY][inicioX] = elem
           inicioX += 1
           inicioY += 1
        else:
            return False
    return board

def llenar_palabras_aux(lista_palabras, dimensiones):
    global BOARD_JUEGO
    board = create_board(dimensiones, dimensiones)
    puse = 0
    iteraciones = 0
    
    while puse == 0:
        iteraciones += 1
        if iteraciones == 25:
            return False
        palabra_h = palabra_horizontal(lista_palabras[0],board)
        if palabra_h != False:
            board = palabra_h
            puse += 1

    while puse < 2:
        iteraciones += 1
        if iteraciones == 25:
            return False
        palabra_v = palabra_vertical(lista_palabras[1],board)
        if palabra_v != False:
            board = palabra_v
            puse += 1

    while puse < 3:
        iteraciones += 1
        if iteraciones == 25:
            return False
        palabra_d = palabra_diagonal(lista_palabras[2],board)
        if palabra_d != False:
            board = palabra_d[0]
            puse += 1

    while puse < 4:
        iteraciones += 1
        if iteraciones == 25:
            return False
        palabra_dv = palabra_diagonal_inver(lista_palabras[3],board)
        if palabra_dv != False:
            board = palabra_dv
            puse += 1

    return board


def llenar_palabras(lista_palabras ,dimensiones):
    while True == True:
        lista4_palabras = random.choices(lista_palabras, k=4)
        board = llenar_palabras_aux(lista4_palabras,dimensiones)
        if board != False:
            return [board,lista4_palabras]
        


#========================

#   INTERFAZ GRAFICA

#========================


def pantalla():
    global BOARD_INTERFAZ, BOARD_JUEGO, CONTADOR, LISTA_PALABRAS

    dimensiones = random.choice([10,15,20])
    LISTA_PALABRAS = cargarArchivo("Sopita/palabras.txt")
    BOARD_INTERFAZ = create_board(dimensiones, dimensiones)
    res = llenar_palabras(LISTA_PALABRAS, dimensiones)
    BOARD_JUEGO = res[0]
    #print(res[1])


    llenar_letras()
    #print_b(BOARD_JUEGO)
    #print_b(BOARD_INTERFAZ)


    pygame.init()  # comando de correr modulo pygae

    pygame.mixer.music.load("Sopita/Sonidos_Sopa/Sopa.mp3")
    pygame.mixer.music.set_volume(0.3)
    pygame.mixer.music.play(-1)

    game_over = False

    width = dimensiones * 32
    height = dimensiones * 40

    size = (width, height + 100)
    screen = pygame.display.set_mode((width, height + 100))  # tamano de la pantalla

    
    circulo = pygame.image.load("Sopita/Imagenes_sopa/circulo.png")
    circulo = pygame.transform.scale(circulo,(30,30))


    pygame.display.update()  # imprime en pantalla los datos que la ventana contiene

    myfont = pygame.font.SysFont("Arial", 30)  # declaracion de la fuente

    iniTime = time.time()
    timer = 0
    maxTime = random.choice([120])

    print_b(BOARD_JUEGO)
    termino = False
    R = 0
    G = 128
    G1 = 1
    B = 72
    B1 = 1

    while timer < maxTime:
        endTime = time.time()
        timer = endTime - iniTime

        if gana():
            #pygame.display.quit()
            #pygame.quit()
            print("You win word search")
            return gana()

        #mx,my = pygame.mouse.get_pos()

        # cambia color de fondo
        screen.fill((R, G, B))
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
        if B == 255:
            B1 = -1
        elif B == 0:
            B1 = 1
        B += B1

        displayPalabras(res[1],myfont,(255, 255, 255), dimensiones * 15, dimensiones * 31 ,screen)

        dibujar_circulos(circulo,0,0,30,screen)
        label = myfont.render(str(int(maxTime - timer)), True, (0, 0, 0))
        screen.blit(label, (0, height + 50))
        dibujar_letras(0,0, 30 ,myfont, screen, marcar_letra)
        #if gana():
            #print("gana")
            
        
        pygame.display.update()

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
    if not gana():
        print("You lose word search")
    else:
        print("You win word search")
    pygame.mixer.music.stop()
    return gana()
