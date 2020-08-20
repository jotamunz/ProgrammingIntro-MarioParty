import pygame
import pygame.mixer
import random
import sys
import copy

white = (255, 255, 255)
black = (0, 0, 0)

def numero_masCercano(num,lista_num):
    lista_diferencia = []
    lista_diferencia_aux = []
    orden_jugadores = []

    for i in range(0,len(lista_num)):
        lista_diferencia += [abs(num - lista_num[i])]

    lista_diferencia_aux =  copy.deepcopy(lista_diferencia)

    while lista_diferencia_aux != []:
        menor = min(lista_diferencia_aux)
        lista_diferencia_aux.remove(menor)
        for i in range(0,len(lista_diferencia)):
            #print(menor)
            if lista_diferencia[i] == menor:
                orden_jugadores += [i]
                #print(orden_jugadores)
                break

    return orden_jugadores

def inputText(screen, question, font):
  current_string = []
  string=''
  displayBox(screen, question + ": " + string.join(current_string), font)
  while 1:
      inkey = getKey()
      if inkey == pygame.K_BACKSPACE:
          current_string = current_string[0:-1]
      elif inkey == pygame.K_RETURN:
          break
      elif inkey == pygame.K_MINUS:
          current_string.append("_")
      elif inkey <= 127:
          current_string.append(chr(inkey))
      displayBox(screen, question + ": " + string.join(current_string), font)
  return string.join(current_string)

def displayBox(screen, message, font):
  pygame.draw.rect(screen, (0, 0, 0), ((screen.get_width() / 2) - 130, (screen.get_height() / 2) + 250, 250, 20), 0)
  pygame.draw.rect(screen, black, ((screen.get_width() / 2) - 131, (screen.get_height() / 2) + 249, 252, 22), 2)
  if len(message) != 0:
      screen.blit(font.render(message, 1, (255, 255, 255)), ((screen.get_width() / 2) - 125, (screen.get_height() / 2) + 252))
  pygame.display.update()

def getKey():
  while 1:
      event = pygame.event.poll()
      if event.type == pygame.KEYDOWN:
          return event.key

def displayText(text, font, color, location, screen):
    textSurface = font.render(text, True, color)
    textRect = textSurface.get_rect()
    textRect.center = location
    screen.blit(textSurface, textRect)


def pantalla(PLAYER_COUNT, PLAYER1_NOMBRE,  PLAYER2_NOMBRE, PLAYER3_NOMBRE, PLAYER4_NOMBRE):
    global BOARD_INTERFAZ, BOARD_JUEGO, CONTADOR, LISTA_PALABRAS


    pygame.init()  # comando de correr modulo pygae

    pygame.mixer.music.load("Hongo_Contador/Sonidos_Hongo/Hongo.mp3")
    pygame.mixer.music.set_volume(0.5)
    pygame.mixer.music.play(-1)

    game_over = False

    width = 1370 
    height = 770

    size = (width, height)
    screen = pygame.display.set_mode((width, height))  # tamano de la pantalla

    smallFont = pygame.font.SysFont('Arial', 15) # declaracion de font
    bigFont = pygame.font.SysFont('Arial', 25) # declaracion de font
    fondo = pygame.image.load("Hongo_Contador/Imagenes/fondo.png")
    fondo = pygame.transform.scale(fondo,(width,height))

    if PLAYER_COUNT == 2:
        screen.blit(fondo, (0, 0))
        displayText("TYPE A NUMBER BETWEEN 1 AND 1000", bigFont, black,((screen.get_width() / 2), (screen.get_height() / 2) + 200), screen)
        PLAYER1_NUMERO = int(inputText(screen, "Player 1", smallFont))
        PLAYER2_NUMERO = int(inputText(screen, "Player 2", smallFont))
        lista_num = [PLAYER1_NUMERO,PLAYER2_NUMERO]

    elif PLAYER_COUNT == 3:
        screen.blit(fondo, (0, 0))
        displayText("TYPE A NUMBER BETWEEN 1 AND 1000", bigFont, black, ((screen.get_width() / 2), (screen.get_height() / 2) + 200), screen)
        PLAYER1_NUMERO = int(inputText(screen, "Player 1", smallFont))
        PLAYER2_NUMERO = int(inputText(screen, "Player 2", smallFont))
        PLAYER3_NUMERO = int(inputText(screen, "Player 3", smallFont))
        lista_num = [PLAYER1_NUMERO,PLAYER2_NUMERO,PLAYER3_NUMERO]

    elif PLAYER_COUNT == 4:
        screen.blit(fondo, (0, 0))
        displayText("TYPE A NUMBER BETWEEN 1 AND 1000", bigFont, black, ((screen.get_width() / 2), (screen.get_height() / 2) + 200), screen)
        PLAYER1_NUMERO = int(inputText(screen, "Player 1", smallFont))
        PLAYER2_NUMERO = int(inputText(screen, "Player 2", smallFont))
        PLAYER3_NUMERO = int(inputText(screen, "Player 3", smallFont))
        PLAYER4_NUMERO = int(inputText(screen, "Player 4", smallFont))
        lista_num = [PLAYER1_NUMERO,PLAYER2_NUMERO,PLAYER3_NUMERO,PLAYER4_NUMERO]

    numero = random.randint(0,1000)

    res_orden = numero_masCercano(numero,lista_num)
    #print(res_orden)
    res_nombres_ordenados = []

    for i in range(len(lista_num)):
        if res_orden[i] == 0:
            res_nombres_ordenados += [PLAYER1_NOMBRE]
        elif res_orden[i] == 1:    
            res_nombres_ordenados += [PLAYER2_NOMBRE]
        elif res_orden[i] == 2:
            res_nombres_ordenados += [PLAYER3_NOMBRE]
        elif res_orden[i] == 3:
            res_nombres_ordenados += [PLAYER4_NOMBRE]
            
    mostrar = False


    pygame.display.update()  # imprime en pantalla los datos que la ventana contiene

    myfont = pygame.font.SysFont("Arial", 100)  # declaracion de la fuente

    termino = False

    while not(termino):

        screen.blit(fondo,(0,0))
        screen.blit(fondo,(0,0))
        if mostrar == False:
            displayText(str(random.randint(0,1000)), myfont, (0,0,0), (665, 200), screen)
        if mostrar == True:
            displayText(str(numero), myfont, (0,0,0), (665, 200), screen)
            termino = True
        pygame.display.update()
        #print(pygame.mouse.get_pos())

        keys = pygame.key.get_pressed()
        if keys[pygame.K_SPACE]:
            mostrar = True
         
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.display.quit()
                pygame.quit()
                sys.exit()

        if termino == True:
            delay = 0
            while delay < 300000:
                delay += 0.01
            pygame.mixer.music.stop()
            # pygame.display.quit()
            # pygame.quit()
            #sys.exit()
            #print(res_nombres_ordenados)
            return res_nombres_ordenados
            #return numero_masCercano(numero,lista_num)
