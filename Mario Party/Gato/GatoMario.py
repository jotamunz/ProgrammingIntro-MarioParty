import pygame
import pygame.mixer
import random
import sys
#import botones

#========================

# VARIABLES GLOBALES

#========================


BOARD = [[0,0,0],
         [0,0,0],
         [0,0,0]]

MARCA_X = 1

MARCA_O = 2

#========================

# PRINTS

#========================

def print_b(board):
    for i in board:
        print (i)

#========================

# ACCIONES DE GATO

#========================

def marcar(fil,col,ficha):
    global BOARD
    if puedo_marcar(fil,col):
        BOARD[fil][col] = ficha

def puedo_marcar(fil,col):
    global BOARD
    if BOARD[fil][col] == 0:
        return True
    else:
        return False


#========================

# POSICIONES GANE

#========================

def tieneMismas(lista):
    if lista == []:
        return True
    elif len(lista) == 1:
        return True
    elif lista[0] == lista[1]:
        return tieneMismas(lista[1:])
    else:
        return False

def horizontal(ficha):
    global BOARD
    fila = []
    for f in range(0,len(BOARD)):
        for c in range(0,len(BOARD[0])):
            fila += [BOARD[f][c]]
        if tieneMismas(fila) and fila[0] == ficha:
            return True
        else:
            fila = []
    return False

def vertical(ficha):
    global BOARD
    columna = []
    for c in range(0,len(BOARD[0])):
        for f in range(0,len(BOARD)):
            columna += [BOARD[f][c]]
        if tieneMismas(columna) and columna[0] == ficha:
            return True
        else:
            columna = []
    return False

def diagonal(ficha):
    global BOARD
    diagonal = []
    for d in range(0,len(BOARD)):
        diagonal += [BOARD[d][d]]
    if tieneMismas(diagonal) and diagonal[0] == ficha:
        return True
    else:
        return False

def diagonal_I(ficha):
    global BOARD
    diagonal_I = []
    for d_I in range(0,len(BOARD)):
        diagonal_I += [BOARD[len(BOARD)-1-d_I][d_I]]
    if tieneMismas(diagonal_I) and diagonal_I[0] == ficha:
        return True
    else:
        return False

def gana(ficha):
    if horizontal(ficha) or vertical(ficha) or diagonal(ficha) or diagonal_I(ficha):
        return True
    else:
        return False
        
#========================

# TURNO JUGADORES

#========================

def Main(Jugador1,Jugador2):
    global BOARD

    turno = random.randint(0,1)
    termino = False
    
    while not(termino):
        
        if turno == 0:
            fila = eval(input("elija la fila en que quiere poner: "))
            columna = eval(input("elija la columna en la que quiere poner: "))
            if puedo_marcar(fila,columna):
                marcar(fila,columna,MARCA_X)
            if gana(MARCA_X):
                termino = True
            print_b(BOARD)
        else: #turno == 1
            fila = eval(input("elija la fila en que quiere poner: "))
            columna = eval(input("elija la columna en la que quiere poner: "))
            if puedo_marcar(fila,columna):
                marcar(fila,columna,MARCA_O)
            if gana(MARCA_O):
                termino = True
            print_b(BOARD)

        turno = (turno + 1)%2

    if gana(MARCA_X):
        return str("Gana :" + Jugador1)
    else: #MARCA_O
        return str("Gana :" + Jugador2)

#========================

#       BOTONES

#========================

def Button(message, x, y, w, h, color, hover, pos, action=None):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    if (x + w) > mouse[0] > x and (y + h) > mouse[1] > y:
        displayText(message, myfont, hover, pos)
        if click[0] == 1 and action != None:
            action()
    else:
        displayText(message, myfont, color, pos)
              
#========================

# INTERFAZ GRAFICA

#========================



def pantalla(mainPlayer, otherPlayer):
    global BOARD,MARCA_X,MARCA_O

    BOARD = [[0,0,0],
         [0,0,0],
         [0,0,0]]

    MARCA_X = 1

    MARCA_O = 2

    pygame.init()  # comando de correr modulo pygae

    pygame.mixer.music.load("Gato/Sonidos_Gato/Gato_musica.mp3")
    pygame.mixer.music.set_volume(0.3)
    pygame.mixer.music.play(-1)

    game_over = False

    width = 500
    height = 500

    size = (width, height)

    screen = pygame.display.set_mode((width, height + 100))#tamano de la pantalla
    bg = pygame.image.load("Gato/Imagenes_Gato/bg.png")
    bg = pygame.transform.scale(bg,size)
    ficha_x = pygame.image.load("Gato/Imagenes_Gato/Goomba.png")
    ficha_x = pygame.transform.scale(ficha_x,(150,150))
    ficha_o = pygame.image.load("Gato/Imagenes_Gato/Mario.png")
    ficha_o = pygame.transform.scale(ficha_o,(150,150))

    tablero = pygame.image.load("Gato/Imagenes_Gato/tablero.png")
    tablero = pygame.transform.scale(tablero,size)

    sonido_mario = pygame.mixer.Sound("Gato/Sonidos_Gato/mario.wav")
    sonido_goomba = pygame.mixer.Sound("Gato/Sonidos_Gato/goomba.wav")
    sonido_mario.set_volume(0.2)
    sonido_goomba.set_volume(0.4)

    pygame.display.update() # imprime en pantalla los datos que la ventana contiene

    myfont = pygame.font.SysFont("Arial", 35) # declaracion de la fuente
    font2 = pygame.font.SysFont("Arial", 35)# declaracion de la fuente



    turno = random.randint(1,2)
    if turno == 1:
        marcador = MARCA_X
    else:
        marcador = MARCA_O
        
    termino = False

    R = 0
    delay = 0
    
    while not(termino): #loop del juego

        #print(turno)
        screen.fill((R,0,0))
        screen.blit(bg,(0,0))
        screen.blit(tablero,(0,0))

        if marcador == MARCA_X and not(gana(MARCA_X)) and not(gana(MARCA_O)):
            label = font2.render("Turno: " + str(otherPlayer),True,(255,255,255))
            screen.blit(label, (20, 510))
            pygame.display.update()
        if marcador == MARCA_O and not(gana(MARCA_X)) and not(gana(MARCA_O)):
            label = font2.render("Turno: " + str(mainPlayer),True,(255,255,255))
            screen.blit(label, (20, 510))
            pygame.display.update()
            
        for f in range(0,len(BOARD)):
            for c in range(0,len(BOARD[0])):
                if BOARD[f][c] == 1:
                    screen.blit(ficha_x,(c*165,f*165))
                if BOARD[f][c] == 2:
                    screen.blit(ficha_o,(c*165,f*165))
        if gana(MARCA_X):
            label = myfont.render("Gana " + otherPlayer,True,(255,255,255))
            screen.blit(label, (20, 510))
            pygame.display.update()

        if gana(MARCA_O):
            label = myfont.render("Gana " + mainPlayer,True,(255,255,255))
            screen.blit(label, (0, 510))
            pygame.display.update()
        pygame.display.update()

        
        #cambia color de fondo
        if R == 255:
            R1 = -1
        elif R == 0:
            R1 = 1
        R += R1



        if turno == 1:
            marcador = MARCA_X
        else:
            marcador = MARCA_O


        #print(marcador)

        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                pygame.mixer.music.stop()
                #pygame.display.quit()
                #pygame.quit()
                #sys.exit()
                if gana(MARCA_X):
                    print(otherPlayer + " wins tic-tac-toe")
                    return False
                else:
                    print(mainPlayer + " wins tic-tac-toe")
                    return True
                

            if event.type == pygame.MOUSEBUTTONDOWN:

                if turno == 1:
                    sonido_goomba.play()
                else:
                    sonido_mario.play()
                    
                posClick = [event.pos[0],event.pos[1]]
                #print(str(posClick))
                

                if event.pos[0] >= 0 and event.pos[0] <= 164:
                        if event.pos[1] >= 0 and event.pos[1] <= 164:
                            if puedo_marcar(0,0):
                                marcar(0,0,marcador)

                if event.pos[0] >= 165 and event.pos[0] <= 330:
                        if event.pos[1] >= 0 and event.pos[1] <= 161:
                            if puedo_marcar(0,1):
                                marcar(0,1,marcador)

                if event.pos[0] >= 331 and event.pos[0] <= 493:
                        if event.pos[1] >= 0 and event.pos[1] <= 161:
                            if puedo_marcar(0,2):
                                marcar(0,2,marcador)

                if event.pos[0] >= 0 and event.pos[0] <= 164:
                        if event.pos[1] >= 161 and event.pos[1] <= 328:
                            if puedo_marcar(1,0):
                                marcar(1,0,marcador)

                if event.pos[0] >= 165 and event.pos[0] <= 330:
                        if event.pos[1] >= 161 and event.pos[1] <= 328:
                            if puedo_marcar(1,1):
                                marcar(1,1,marcador)

                if event.pos[0] >= 331 and event.pos[0] <= 493:
                        if event.pos[1] >= 161 and event.pos[1] <= 328:
                            if puedo_marcar(1,2):
                                marcar(1,2,marcador)

                if event.pos[0] >= 0 and event.pos[0] <= 164:
                        if event.pos[1] >= 328 and event.pos[1] <= 483:
                            if puedo_marcar(2,0):
                                marcar(2,0,marcador)

                if event.pos[0] >= 165 and event.pos[0] <= 330:
                        if event.pos[1] >= 328 and event.pos[1] <= 483:
                            if puedo_marcar(2,1):
                                marcar(2,1,marcador)

                if event.pos[0] >= 331 and event.pos[0] <= 493:
                        if event.pos[1] >= 328 and event.pos[1] <= 483:
                            if puedo_marcar(2,2):
                                marcar(2,2,marcador)

                
                if gana(MARCA_X):
                    #print("gana")
                    label = myfont.render("Gana " + otherPlayer,True,(0,0,0))
                    screen.blit(label, (20, 500))
                    pygame.display.update()

                if gana(MARCA_O):
                    #print("gana")
                    label = myfont.render("Gana " + mainPlayer,True,(0,0,0))
                    screen.blit(label, (20, 500))
                    pygame.display.update()

                if turno == 1:
                    turno = 2
                else:
                    turno = 1
