import pygame
import pygame.mixer
import random
import sys
from Memory_Path import Memory_Path
from Mario_Memory import Mario_Memory
from Mario_Cards import Mario_Cards
from Bombermario import Bombermario
from Gato import GatoMario
from Guess_who import Guess_who
from Collect_coins import Collect_coins
from Sopita import Sopa
from Catch_Cat import Catch_The_Cat
from Dado import Dado
from Congelar import Congelar
from Quemar import Quemar
from Elegir_personaje import Elegir_personaje
from Hongo_Contador import Hongo_Contador

#====================================================================
#                           GLOBALS
#====================================================================

#crea un tablero nuevo
def createBoard():
    cells = [1,1,2,2,3,3,4,4,5,5,6,6,7,7,8,8,9,9,10,11,12,13,14,15,16,17]
    random.shuffle(cells)
    board = [0] + cells + [0]
    pipes = [findPipe(10, board), findPipe(11, board), findPipe(12, board)]
    pipes = orderPipes(pipes)
    board[pipes[0]] = 10
    board[pipes[1]] = 11
    board[pipes[2]] = 12
    return board

def findPipe(num, board):
    for i in range(0, len(board)):
        if board[i] == num:
            return i

def orderPipes(pipes):
    maximo = max(pipes)
    minimo = min(pipes)
    for elem in pipes:
        if elem != maximo and elem != minimo:
            otro = elem
    pipesOrder = [minimo, otro, maximo]
    return pipesOrder

#pasa el tablero a matriz para dibujarlo
def boardToMatrix(board):
    board = [board[:9],
            [0,0,0,0,0,0,0,0] + [board[9]],
            board[22:] + [0,0] + [board[10]],
            [board[21]] + [0,0,0,0,0,0,0] + [board[11]],
            [board[20]]+[board[19]]+[board[18]]+[board[17]]+[board[16]]+[board[15]]+[board[14]]+[board[13]]+[board[12]]]
    return board

BOARD = createBoard()

#Cantidad de jugadores y sus respectivos tableros
PLAYER_COUNT = 0
PLAYER_BOARD_1 = [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
PLAYER_BOARD_2 = [2,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
PLAYER_BOARD_3 = [3,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
PLAYER_BOARD_4 = [4,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
PLAYER1 = ""
PLAYER2 = ""
PLAYER3 = ""
PLAYER4 = ""
TURNLOSS1 = 0
TURNLOSS2 = 0
TURNLOSS3 = 0
TURNLOSS4 = 0
STARPOWER = False

#Tamanos
picsize = 140
square = 150
width = 1370
height = 770

#Colores
white = (255,255,255)
black = (0,0,0)

#Inicio
pygame.init()
window = pygame.display.set_mode((width, height), pygame.RESIZABLE)
window.fill(white)
pygame.display.set_caption('Mario Party')

#Musica
pygame.mixer.music.load("Board/board_musica.mp3")
pygame.mixer.music.set_volume(0.5)
pygame.mixer.music.play(-1)
sonido_star = pygame.mixer.Sound("Board/star.wav")
sonido_star.set_volume(0.5)
sonido_cola = pygame.mixer.Sound("Board/jump.wav")
sonido_cola.set_volume(0.5)
sonido_pipe = pygame.mixer.Sound("Board/pipe.wav")
sonido_pipe.set_volume(0.5)
sonido_win = pygame.mixer.Sound("Board/score.wav")
sonido_win.set_volume(0.5)
sonido_jail = pygame.mixer.Sound("Board/die.wav")
sonido_jail.set_volume(0.5)

#Fonts
bigFont = pygame.font.SysFont('Arial', 45)
smallFont = pygame.font.SysFont('Arial', 15)
regFont = pygame.font.SysFont('Arial', 20)
winFont = pygame.font.SysFont('Arial', 100)

#Imagenes
blank_board = pygame.image.load("Board/board.png")
tictactoe = pygame.image.load("Board/tictactoe.png")
word_search = pygame.image.load("Board/word_search.png")
memory_path = pygame.image.load("Board/memory_path.png")
mario_memory = pygame.image.load("Board/mario_memory.png")
catch_cat = pygame.image.load("Board/catch_cat.png")
bomber_mario = pygame.image.load("Board/bomber_mario.png")
guess_who = pygame.image.load("Board/guess_who.png")
collect_coins = pygame.image.load("Board/collect_coins.png")
mario_cards = pygame.image.load("Board/mario_cards.png")
special_pipe = pygame.image.load("Board/pipe.png")
special_fire = pygame.image.load("Board/fire_flower.png")
special_ice = pygame.image.load("Board/ice_flower.png")
special_star = pygame.image.load("Board/star.png")
special_feather = pygame.image.load("Board/feather.png")
special_jail = pygame.image.load("Board/jail.png")
num_0 = pygame.image.load("Board/dice0.png")
num_1 = pygame.image.load("Board/dice1.png")
num_2 = pygame.image.load("Board/dice2.png")
num_3 = pygame.image.load("Board/dice3.png")
num_4 = pygame.image.load("Board/dice4.png")
num_5 = pygame.image.load("Board/bowser_icon.png")
dado = pygame.image.load("Board/dice.png")
logo = pygame.image.load("Board/logo.png")
background = pygame.image.load("Board/background.jpg")
backgroundWin = pygame.image.load("Board/backgroundWin.png")

tictactoe = pygame.transform.scale(tictactoe,(picsize,picsize))
word_search = pygame.transform.scale(word_search,(picsize,picsize))
memory_path = pygame.transform.scale(memory_path,(picsize,picsize))
mario_memory = pygame.transform.scale(mario_memory,(picsize,picsize))
catch_cat = pygame.transform.scale(catch_cat,(picsize,picsize))
bomber_mario = pygame.transform.scale(bomber_mario,(picsize,picsize))
guess_who = pygame.transform.scale(guess_who,(picsize,picsize))
collect_coins = pygame.transform.scale(collect_coins,(picsize,picsize))
mario_cards = pygame.transform.scale(mario_cards,(picsize,picsize))
special_pipe1 = pygame.transform.scale(special_pipe,(picsize,picsize))
special_pipe2 = pygame.transform.scale(special_pipe,(picsize,picsize))
special_pipe3 = pygame.transform.scale(special_pipe,(picsize,picsize))
special_fire = pygame.transform.scale(special_fire,(picsize,picsize))
special_ice = pygame.transform.scale(special_ice,(picsize,picsize))
special_star = pygame.transform.scale(special_star,(picsize,picsize))
special_feather = pygame.transform.scale(special_feather,(picsize,picsize))
special_jail = pygame.transform.scale(special_jail,(picsize,picsize))
num_0 = pygame.transform.scale(num_0, (100, 100))
num_1 = pygame.transform.scale(num_1, (100, 100))
num_2 = pygame.transform.scale(num_2, (100, 100))
num_3 = pygame.transform.scale(num_3, (100, 100))
num_4 = pygame.transform.scale(num_4, (100, 100))
num_5 = pygame.transform.scale(num_5, (100, 100))
dado = pygame.transform.scale(dado, (130, 130))
background = pygame.transform.scale(background,(width,height))
backgroundWin = pygame.transform.scale(backgroundWin,(width,height))

CELL_IMAGES = [tictactoe, word_search, memory_path, mario_memory, catch_cat, bomber_mario, guess_who, collect_coins, mario_cards,
               special_pipe1, special_pipe2, special_pipe3, special_fire, special_ice, special_star, special_feather, special_jail]

PLAYER1_IMAGE = ""
PLAYER2_IMAGE = ""
PLAYER3_IMAGE = ""
PLAYER4_IMAGE = ""

#====================================================================
#                          FUNCTIONS
#====================================================================

#Empieza la musica del tablero
def playMusic():
    pygame.mixer.music.load("Board/board_musica.mp3")
    pygame.mixer.music.set_volume(0.5)
    pygame.mixer.music.play(-1)

#print el tablero en forma matriz
def print_b(board):
    for i in board:
        print (i)

#retorna la posicion actual de un jugador en su tablero
def currentPosition(board, player):
    for num in range(0, len(board)):
        if board[num] == player:
            currentPos = num
    return currentPos

#mueve un jugador en su tablero
def movePlayer(board, dice_num, player):
    currentPos = currentPosition(board, player)
    board[currentPos] = 0
    board[currentPos + dice_num] = player

def moveWinner(board, player):
    currentPos = currentPosition(board, player)
    board[currentPos] = 0
    board[27] = player

#retorna si el lanzamiento del dado es de gane o no
def checkWin(board, dice_num, player):
    currentPos = currentPosition(board, player)
    if (currentPos + dice_num) >= 27:
        return True
    else:
        return False

#retorna el tablero respectivo de un jugador
def getPlayerBoard(turn):
    global PLAYER_BOARD_1, PLAYER_BOARD_2, PLAYER_BOARD_3, PLAYER_BOARD_4
    if turn == 1:
        return PLAYER_BOARD_1
    elif turn == 2:
        return PLAYER_BOARD_2
    elif turn == 3:
        return PLAYER_BOARD_3
    elif turn == 4:
        return PLAYER_BOARD_4

#encuentra el codigo de juego segun la posicion en el tablero
def findGame(board, currentPos):
    for num in range(0, len(board)):
        if num == currentPos:
            return board[num]

#retorna la imagen de ficha de un jugador
def getPlayerImage(player):
    global PLAYER1_IMAGE, PLAYER2_IMAGE, PLAYER3_IMAGE, PLAYER4_IMAGE
    if player == 1:
        return PLAYER1_IMAGE
    elif player == 2:
        return PLAYER2_IMAGE
    elif player == 3:
        return PLAYER3_IMAGE
    else:
        return PLAYER4_IMAGE

#retorna el nombre del jugador del turno dado
def getMainPlayer(turn):
    global PLAYER1, PLAYER2, PLAYER3, PLAYER4
    if turn == 1:
        return PLAYER1
    elif turn == 2:
        return PLAYER2
    elif turn == 3:
        return PLAYER3
    else:
        return PLAYER4

#ordena los jugadores empezando con el jugador del turno dado y el resto aleatorio luego rellena con jugadores en blanco
def orderPlayers(turn):
    global PLAYER_COUNT, PLAYER1, PLAYER2, PLAYER3, PLAYER4
    mainPlayer = getMainPlayer(turn)
    if PLAYER_COUNT == 2:
        players = [PLAYER1, PLAYER2]
    elif PLAYER_COUNT == 3:
        players = [PLAYER1, PLAYER2, PLAYER3]
    else:
        players = [PLAYER1, PLAYER2, PLAYER3, PLAYER4]
    players.remove(mainPlayer)
    random.shuffle(players)
    if len(players) == 1:
        players += ["", ""]
    elif len(players) == 2:
        players += [""]
    return [mainPlayer] + players

#retorna un juego segun su codigo
def runGame(game, turn):
    global PLAYER_COUNT, PLAYER1, PLAYER2, PLAYER3, PLAYER4
    
    players = orderPlayers(turn)
    mainPlayer = players[0]
    otherPlayer = players[1]
    otherPlayer2 = players[2]
    otherPlayer3 = players[3]
    
    if game == 1:
        return GatoMario.pantalla(mainPlayer, otherPlayer)
    elif game == 2:
        return Sopa.pantalla()
    elif game == 3:
        return Memory_Path.playMemoryPath()
    elif game == 4:
        return Mario_Memory.playMemory(mainPlayer, otherPlayer)
    elif game == 5:
        return Catch_The_Cat.playCatch()
    elif game == 6:
        return Bombermario.pantalla()
    elif game == 7:
        return Guess_who.pantalla()
    elif game == 8:
        return Collect_coins.pantalla()
    elif game == 9:
        return Mario_Cards.playCards(PLAYER_COUNT, mainPlayer, otherPlayer, otherPlayer2, otherPlayer3)
    elif game == 10:
        sonido_pipe.play()
        move = moveToPipe(turn, 2)
        playerBoard = getPlayerBoard(turn)
        movePlayer(playerBoard, move, turn)
        return True
    elif game == 11:
        sonido_pipe.play()
        move = moveToPipe(turn, 3)
        playerBoard = getPlayerBoard(turn)
        movePlayer(playerBoard, move, turn)
        return True
    elif game == 12:
        sonido_pipe.play()
        move = moveToPipe(turn, 1)
        playerBoard = getPlayerBoard(turn)
        movePlayer(playerBoard, move, turn)
        return True
    elif game == 13:
        player = Quemar.pantalla(PLAYER_COUNT, mainPlayer, otherPlayer, otherPlayer2, otherPlayer3)
        moveToStart(player)
        return True
    elif game == 14:
        player = Congelar.pantalla(PLAYER_COUNT, mainPlayer, otherPlayer, otherPlayer2, otherPlayer3)
        addTurnLoss(player)
        return True
    elif game == 15:
        sonido_star.play()
        starPowerOn()
        return True
    elif game == 16:
        sonido_cola.play()
        move = random.choice([1,2,3])
        playerBoard = getPlayerBoard(turn)
        movePlayer(playerBoard, move, turn)
        drawAllPlayers(PLAYER_COUNT)
        print(playerBoard)
        currentPos = currentPosition(playerBoard, turn)
        game = findGame(BOARD, currentPos)
        print("GAME: ", game)
        pygame.time.wait(4000)
        return runGame(game, turn)
    elif game == 17:
        sonido_jail.play()
        addTurnLoss(mainPlayer)
        return True

def addTurnLoss(player):
    global TURNLOSS1, TURNLOSS2, TURNLOSS3, TURNLOSS4, PLAYER1, PLAYER2, PLAYER3, PLAYER4
    if player == PLAYER1:
        TURNLOSS1 += 2
    elif player == PLAYER2:
        TURNLOSS2 += 2
    elif player == PLAYER3:
        TURNLOSS3 += 2
    else:
        TURNLOSS4 += 2

def hasTurnLoss(turn):
    global TURNLOSS1, TURNLOSS2, TURNLOSS3, TURNLOSS4
    if turn == 1:
        return TURNLOSS1
    elif turn == 2:
        return TURNLOSS2
    elif turn == 3:
        return TURNLOSS3
    else:
        return TURNLOSS4

def subTurnLoss(turn):
    global TURNLOSS1, TURNLOSS2, TURNLOSS3, TURNLOSS4
    if turn == 1:
        TURNLOSS1 -= 1
    elif turn == 2:
        TURNLOSS2 -= 1
    elif turn == 3:
        TURNLOSS3 -= 1
    else:
        TURNLOSS4 -= 1

def moveToStart(player):
    global PLAYER1, PLAYER2, PLAYER3, PLAYER4
    if player == PLAYER1:
        playerBoard = getPlayerBoard(1)
        move = currentPosition(playerBoard, 1)
        movePlayer(playerBoard, -move, 1)
    elif player == PLAYER2:
        playerBoard = getPlayerBoard(2)
        move = currentPosition(playerBoard, 2)
        movePlayer(playerBoard, -move, 2)
    elif player == PLAYER3:
        playerBoard = getPlayerBoard(3)
        move = currentPosition(playerBoard, 3)
        movePlayer(playerBoard, -move, 3)
    else:
        playerBoard = getPlayerBoard(4)
        move = currentPosition(playerBoard, 4)
        movePlayer(playerBoard, -move, 4)

def moveToPipe(turn, pipeNum):
    playerBoard = getPlayerBoard(turn)
    currentPos = currentPosition(playerBoard, turn)
    if pipeNum == 2:
        pipePos = pipePosition(11)
    elif pipeNum == 3:
        pipePos = pipePosition(12)
    else:
        pipePos = pipePosition(10)
    return pipePos - currentPos

def pipePosition(pipeNum):
    global BOARD
    for num in range(0, len(BOARD)):
        if BOARD[num] == pipeNum:
            pipePos = num
    return pipePos

def starPower():
    global STARPOWER
    return STARPOWER

def starPowerOff():
    global STARPOWER
    STARPOWER = False

def starPowerOn():
    global STARPOWER
    STARPOWER = True

#====================================================================
#                          GRAPHICS
#====================================================================

#dibuja el tablero en la ventana
def drawBoard(board):
    global square, CELL_IMAGES
    board = boardToMatrix(board)
    window.blit(blank_board, (10, 10))
    for row in range(0, len(board)):
        for column in range(0, len(board[0])):
            if board[row][column] != 0:
                value = board[row][column]
                cell = CELL_IMAGES[value - 1]
                window.blit(cell, (column * square + 15, row * square + 15))
    pygame.display.update()

#necesario para devovler la ventana al tablero
def pygameInit():
    window = pygame.display.set_mode((width, height), pygame.RESIZABLE)
    window.fill(white)
    pygame.display.set_caption('Mario Party')

def drawDice(dice_num):
    window.blit(dado, (990, 315))
    if dice_num == 0:
        imagen_mostrar = num_0
    elif dice_num == 1:
        imagen_mostrar = num_1
    elif dice_num == 2:
        imagen_mostrar = num_2
    elif dice_num == 3:
        imagen_mostrar = num_3
    elif dice_num == 4:
        imagen_mostrar = num_4
    elif dice_num == 5:
        imagen_mostrar = num_5
    else:
        imagen_mostrar = num_5
    window.blit(imagen_mostrar, (1005, 330))
    pygame.display.update()

def drawPlayer(board, player):
    playerBoard = boardToMatrix(board)
    for row in range(0, len(playerBoard)):
        for column in range(0, len(playerBoard[0])):
            if playerBoard[row][column] == player:
                playerImage = getPlayerImage(player)
                if player == 1:
                    window.blit(playerImage, (column * square + 10, row * square + 10))
                elif player == 2:
                    window.blit(playerImage, (column * square + 10, row * square + 10 + 75))
                elif player == 3:
                    window.blit(playerImage, (column * square + 10 + 75, row * square + 10))
                else:
                    window.blit(playerImage, (column * square + 10 + 75, row * square + 10 + 75))
    pygame.display.update()

def drawAllPlayers(playerCount):
    if playerCount == 2:
        drawPlayer(getPlayerBoard(1), 1)
        drawPlayer(getPlayerBoard(2), 2)
    elif playerCount == 3:
        drawPlayer(getPlayerBoard(1), 1)
        drawPlayer(getPlayerBoard(2), 2)
        drawPlayer(getPlayerBoard(3), 3)
    else:
        drawPlayer(getPlayerBoard(1), 1)
        drawPlayer(getPlayerBoard(2), 2)
        drawPlayer(getPlayerBoard(3), 3)
        drawPlayer(getPlayerBoard(4), 4)

def drawWinner(winner):
    sonido_win.play()
    window.blit(backgroundWin, (0, 0))
    displayText(winner, winFont, white, (width/2, height/2 - 40))
    displayText("Wins", winFont, white, (width/2, height/2 + 70))
    pygame.display.update()

def drawTurn(turn):
    global PLAYER1, PLAYER2, PLAYER3, PLAYER4
    if turn == 1:
        displayText("Turn: " + PLAYER1, regFont, black, (1050, 300))
    elif turn == 2:
        displayText("Turn: " + PLAYER2, regFont, black, (1050, 300))
    elif turn == 3:
        displayText("Turn: " + PLAYER3, regFont, black, (1050, 300))
    else:
        displayText("Turn: " + PLAYER4, regFont, black, (1050, 300))
    pygame.display.update()

def displayText(text, font, color, location):
    textSurface = font.render(text, True, color)
    textRect = textSurface.get_rect()
    textRect.center = location
    window.blit(textSurface, textRect)

def makeButton(message, x, y, w, h, color, hover, pos, action=None):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    if (x + w) > mouse[0] > x and (y + h) > mouse[1] > y:
        displayText(message, bigFont, hover, pos)
        if click[0] == 1:
            action()
    else:
        displayText(message, bigFont, color, pos)

def inputText(screen, question):
  current_string = []
  string=''
  displayBox(screen, question + ": " + string.join(current_string))
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
      displayBox(screen, question + ": " + string.join(current_string))
  return string.join(current_string)

def displayBox(screen, message):
  pygame.draw.rect(screen, (0, 0, 0), ((screen.get_width() / 2) - 130, (screen.get_height() / 2) - 10, 255, 20), 0)
  pygame.draw.rect(screen, black, ((screen.get_width() / 2) - 131, (screen.get_height() / 2) - 11, 257, 22), 2)
  if len(message) != 0:
      screen.blit(smallFont.render(message, 1, (255, 255, 255)), ((screen.get_width() / 2) - 125, (screen.get_height() / 2) - 8))
  pygame.display.update()

def getKey():
  while 1:
      event = pygame.event.poll()
      if event.type == pygame.KEYDOWN:
          return event.key

#====================================================================
#                            MENUS
#====================================================================

def start():
    return mainMenu()

def set2Players():
    global PLAYER_COUNT, PLAYER1, PLAYER2
    window.blit(background, (0, 0))
    window.blit(logo, (width / 2 - 190, 40))
    PLAYER_COUNT = 2
    pygame.draw.rect(window, white, (530, 340, 310, 100))
    pygame.draw.rect(window, black, (530, 340, 310, 100), 4)
    PLAYER1 = inputText(window, "Player 1")
    PLAYER2 = inputText(window, "Player 2")
    return setOrden()

def set2Fichas():
    global PLAYER1, PLAYER2, PLAYER1_IMAGE, PLAYER2_IMAGE
    address1 = Elegir_personaje.pantalla(PLAYER1)
    address2 = Elegir_personaje.pantalla(PLAYER2)
    while address1 == address2:
        address2 = Elegir_personaje.pantalla(PLAYER2)
    PLAYER1_IMAGE = pygame.image.load(address1)
    PLAYER1_IMAGE = pygame.transform.scale(PLAYER1_IMAGE, (75, 75))
    PLAYER2_IMAGE = pygame.image.load(address2)
    PLAYER2_IMAGE = pygame.transform.scale(PLAYER2_IMAGE, (75, 75))
    return play()

def set3Players():
    global PLAYER_COUNT, PLAYER1, PLAYER2, PLAYER3
    window.blit(background, (0, 0))
    window.blit(logo, (width / 2 - 190, 40))
    PLAYER_COUNT = 3
    pygame.draw.rect(window, white, (530, 340, 310, 100))
    pygame.draw.rect(window, black, (530, 340, 310, 100), 4)
    PLAYER1 = inputText(window, "Player 1")
    PLAYER2 = inputText(window, "Player 2")
    PLAYER3 = inputText(window, "Player 3")
    return setOrden()

def set3Fichas():
    global PLAYER1, PLAYER2, PLAYER3, PLAYER1_IMAGE, PLAYER2_IMAGE, PLAYER3_IMAGE
    address1 = Elegir_personaje.pantalla(PLAYER1)
    address2 = Elegir_personaje.pantalla(PLAYER2)
    while address1 == address2:
        address2 = Elegir_personaje.pantalla(PLAYER2)
    address3 = Elegir_personaje.pantalla(PLAYER3)
    while address3 == address1 or address3 == address2:
        address3 = Elegir_personaje.pantalla(PLAYER3)
    PLAYER1_IMAGE = pygame.image.load(address1)
    PLAYER1_IMAGE = pygame.transform.scale(PLAYER1_IMAGE, (75, 75))
    PLAYER2_IMAGE = pygame.image.load(address2)
    PLAYER2_IMAGE = pygame.transform.scale(PLAYER2_IMAGE, (75, 75))
    PLAYER3_IMAGE = pygame.image.load(address3)
    PLAYER3_IMAGE = pygame.transform.scale(PLAYER3_IMAGE, (75, 75))
    return play()

def set4Players():
    global PLAYER_COUNT, PLAYER1, PLAYER2, PLAYER3, PLAYER4
    window.blit(background, (0, 0))
    window.blit(logo, (width / 2 - 190, 40))
    PLAYER_COUNT = 4
    pygame.draw.rect(window, white, (530, 340, 310, 100))
    pygame.draw.rect(window, black, (530, 340, 310, 100), 4)
    PLAYER1 = inputText(window, "Player 1")
    PLAYER2 = inputText(window, "Player 2")
    PLAYER3 = inputText(window, "Player 3")
    PLAYER4 = inputText(window, "Player 4")
    return setOrden()

def set4Fichas():
    global PLAYER1, PLAYER2, PLAYER3, PLAYER4, PLAYER1_IMAGE, PLAYER2_IMAGE, PLAYER3_IMAGE, PLAYER4_IMAGE
    address1 = Elegir_personaje.pantalla(PLAYER1)
    address2 = Elegir_personaje.pantalla(PLAYER2)
    while address1 == address2:
        address2 = Elegir_personaje.pantalla(PLAYER2)
    address3 = Elegir_personaje.pantalla(PLAYER3)
    while address3 == address1 or address3 == address2:
        address3 = Elegir_personaje.pantalla(PLAYER3)
    address4 = Elegir_personaje.pantalla(PLAYER4)
    while address4 == address1 or address4 == address2 or address4 == address3:
        address4 = Elegir_personaje.pantalla(PLAYER4)
    PLAYER1_IMAGE = pygame.image.load(address1)
    PLAYER1_IMAGE = pygame.transform.scale(PLAYER1_IMAGE, (75, 75))
    PLAYER2_IMAGE = pygame.image.load(address2)
    PLAYER2_IMAGE = pygame.transform.scale(PLAYER2_IMAGE, (75, 75))
    PLAYER3_IMAGE = pygame.image.load(address3)
    PLAYER3_IMAGE = pygame.transform.scale(PLAYER3_IMAGE, (75, 75))
    PLAYER4_IMAGE = pygame.image.load(address4)
    PLAYER4_IMAGE = pygame.transform.scale(PLAYER4_IMAGE, (75, 75))
    return play()

def setOrden():
    global PLAYER_COUNT, PLAYER1, PLAYER2, PLAYER3, PLAYER4
    playersOrdered = Hongo_Contador.pantalla(PLAYER_COUNT, PLAYER1,  PLAYER2, PLAYER3, PLAYER4)
    while len(playersOrdered) < 4:
        playersOrdered += [""]
    PLAYER1 = playersOrdered[0]
    PLAYER2 = playersOrdered[1]
    PLAYER3 = playersOrdered[2]
    PLAYER4 = playersOrdered[3]
    if PLAYER_COUNT == 2:
        return set2Fichas()
    elif PLAYER_COUNT == 3:
        return set3Fichas()
    else:
        return set4Fichas()

def mainMenu():
    intro = True

    while intro == True:
        window.blit(background, (0, 0))
        window.blit(logo, (width/2 - 190, 40))
        #pygame.draw.rect(window, white, (580, 390, 210, 45))
        makeButton("2 PLAYERS", 580, 390, 210, 45, black, white, (width / 2, 410), set2Players)
        makeButton("3 PLAYERS", 580, 470, 210, 45, black, white, (width / 2, 490), set3Players)
        makeButton("4 PLAYERS", 580, 550, 210, 45, black, white, (width / 2, 570), set4Players)
        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

#====================================================================
#                          GAME LOOP
#====================================================================

def play():
    global BOARD, PLAYER_COUNT
    playMusic()
    dice_num = 0
    turn = 1
    gameOver = False
    print_b(boardToMatrix(BOARD))
    print()
    window.fill(white)
    drawBoard(BOARD)
    drawDice(dice_num)
    drawAllPlayers(PLAYER_COUNT)

    while not gameOver:

        if starPower() == True:                                                  #poner turno en pantalla
            if turn == 1:
                drawTurn(PLAYER_COUNT)
            else:
                drawTurn(turn-1)
        else:
            drawTurn(turn)

        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                sys.exit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    if starPower() == True:
                        if turn == 1:
                            turn = PLAYER_COUNT
                        else:
                            turn -= 1
                        starPowerOff()
                    if hasTurnLoss(turn) != 0:
                        subTurnLoss(turn)
                        turn += 1
                        if turn > PLAYER_COUNT:
                            turn = 1
                    else:
                        dice_num = Dado.pantalla()
                        pygameInit()
                        playerBoard = getPlayerBoard(turn)
                        if dice_num < 5:                                            #si no perdio el turno
                            if checkWin(playerBoard, dice_num, turn) == True:       #si el tiro es mas alto que el tablero
                                winner = turn
                                gameOver = True
                            else:                                                   #si es un tiro normal
                                movePlayer(playerBoard, dice_num, turn)
                                drawBoard(BOARD)
                                drawDice(dice_num)
                                drawAllPlayers(PLAYER_COUNT)
                                print(playerBoard)
                                currentPos = currentPosition(playerBoard, turn)
                                game = findGame(BOARD, currentPos)
                                print("GAME: ", game)
                                pygame.time.wait(4000)
                                pygame.mixer.music.pause()
                                if runGame(game, turn) == True:                     #si gana el minijuego
                                    turn += 1
                                    if turn > PLAYER_COUNT:
                                        turn = 1
                                else:                                               #si pierde el minijuego
                                    movePlayer(playerBoard, -dice_num, turn)
                                    print("Retrocede ", playerBoard)
                                    turn += 1
                                    if turn > PLAYER_COUNT:
                                        turn = 1
                                pygameInit()
                                pygame.mixer.music.unpause()
                                playMusic() 
                        else:                                                       #en este caso perdio el turno
                            print("Pierde el turno ", playerBoard)
                            turn += 1
                            if turn > PLAYER_COUNT:
                                turn = 1

                    drawBoard(BOARD)
                    drawDice(dice_num)
                    drawAllPlayers(PLAYER_COUNT)
                    if gameOver == True:
                        moveWinner(playerBoard, winner)
                        drawBoard(BOARD)
                        drawDice(dice_num)
                        drawAllPlayers(PLAYER_COUNT)
                        print(playerBoard)
                        print("WINNER: ", winner)
                        pygame.display.update()
                        pygame.time.wait(2000)
                        winnerName = getMainPlayer(winner)
                        drawWinner(winnerName)
                        pygame.time.wait(6000)
                        sys.exit()

start()
