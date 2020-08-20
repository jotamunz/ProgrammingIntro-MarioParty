import pygame
import random
import sys
import math

#====================================================================
#                           GLOBALS
#====================================================================

white = (255, 255, 255)
black = (0, 0, 0)

path_mario = pygame.image.load("Memory_Path/Figures/mario.png")
path_block = pygame.image.load("Memory_Path/Figures/block.png")
path_goomba = pygame.image.load("Memory_Path/Figures/goomba.png")
path_shroom = pygame.image.load("Memory_Path/Figures/shroom.png")
path_star = pygame.image.load("Memory_Path/Figures/star.png")
path_denied = pygame.image.load("Memory_Path/Figures/denied.png")
path_mario_star = pygame.image.load("Memory_Path/Figures/mario_star.png")

#====================================================================
#                          FUNCTIONS
#====================================================================

def createBoard():
    board = [[0,0,1],
             [0,0,1],
             [0,0,1],
             [0,0,1],
             [0,0,1],
             [0,0,1],
             [0,0,1],
             [0,0,1]]
    for sublist in board:
        random.shuffle(sublist)
    return board

def print_b(board):
    for i in board:
        print (i)

def currentRow(board):
    for i in range(0, len(board)):
        if 1 in board[i]:
            return i-1
    return len(board)-1

def turnCard(board, row, col):
    board[row][col] = 1

def checkMatch(CardBoard, row, col):
    if CardBoard[row][col] == 1:
        return True
    else:
        return False

def checkWin(row):
    if row == 0:
        return True
    else:
        return False

def tryAgain(board):
    board = [[0, 0, 0],
             [0, 0, 0],
             [0, 0, 0],
             [0, 0, 0],
             [0, 0, 0],
             [0, 0, 0],
             [0, 0, 0],
             [0, 0, 0]]
    return board

def validClick(col):
    if col >= 0 and col <= 2:
        return True
    else:
        return False

#====================================================================
#                          GRAPHICS
#====================================================================

def drawBoard(window, board, CARD_BOARD, square):
    for row in range(0, len(board)):
        for column in range(0, len(board[0])):
            pygame.draw.rect(window, white, (column * square + square, row * square + square, square, square))
            if board[row][column] == 0:
                window.blit(path_block, (column * square + square, row * square + square))
            else:
                if CARD_BOARD[row][column] == 0:
                    window.blit(path_goomba, (column * square + square, row * square + square))
                if CARD_BOARD[row][column] == 1:
                    window.blit(path_shroom, (column * square + square, row * square + square))
    pygame.display.update()

def drawFigures(window, width):
    window.blit(path_mario, (-25, 750))
    window.blit(path_star, (width/2 - 50, 0))
    pygame.display.update()

def displayText(window, text, font, color, location):
    textSurface = font.render(text, True, color)
    textRect = textSurface.get_rect()
    textRect.center = location
    window.blit(textSurface, textRect)

def drawWin(window, winner, width):
    if winner == True:
        pygame.draw.rect(window, white, (0, 0, width, 100))
        pygame.draw.rect(window, white, (0, 750, 100, 150))
        window.blit(path_mario_star, (width/2 - 50, 0))
    else:
        window.blit(path_denied, (width / 2 - 50, 0))
    pygame.display.update()

#====================================================================
#                          GAME LOOP
#====================================================================

def playMemoryPath():
    global path_mario, path_block, path_goomba, path_shroom, path_star, path_denied, path_mario_star

    CARD_BOARD = createBoard()

    BOARD = [[0, 0, 0],
             [0, 0, 0],
             [0, 0, 0],
             [0, 0, 0],
             [0, 0, 0],
             [0, 0, 0],
             [0, 0, 0],
             [0, 0, 0]]

    square = 100
    width = 3 * square + square + square
    height = 8 * square + square

    pygame.init()

    window = pygame.display.set_mode((width, height))
    window.fill(white)
    pygame.display.set_caption('Memory Path')
    myFont = pygame.font.SysFont('Arial', 40)

    pygame.mixer.music.load("Memory_Path/Music/Castle.mp3")
    pygame.mixer.music.set_volume(0.5)
    pygame.mixer.music.play(-1)

    path_mario = pygame.transform.scale(path_mario, (150, 150)).convert_alpha()
    path_block = pygame.transform.scale(path_block, (100, 100)).convert_alpha()
    path_goomba = pygame.transform.scale(path_goomba, (100, 100)).convert_alpha()
    path_shroom = pygame.transform.scale(path_shroom, (100, 100)).convert_alpha()
    path_star = pygame.transform.scale(path_star, (100, 100)).convert_alpha()
    path_denied = pygame.transform.scale(path_denied, (100, 100)).convert_alpha()
    path_mario_star = pygame.transform.scale(path_mario_star, (100, 100)).convert_alpha()

    attempt = 0
    gameOver = False
    drawFigures(window, width)
    print_b(CARD_BOARD)
    print()
    #print_b(BOARD)

    while not gameOver:
        drawBoard(window, BOARD, CARD_BOARD, square)
        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                clickX = event.pos[0]
                col = math.floor(clickX / square) - 1
                row = currentRow(BOARD)
                if validClick(col) == True:
                    turnCard(BOARD, row, col)
                    drawBoard(window, BOARD, CARD_BOARD, square)
                    #print_b(BOARD)
                    if checkMatch(CARD_BOARD, row, col) == True:
                        if checkWin(row) == True:
                            gameOver = True
                            winner = True
                    else:
                        attempt += 1
                        if attempt >= 5:
                            gameOver = True
                            winner = False
                        else:
                            BOARD = tryAgain(BOARD)
                            pygame.time.wait(1000)

                drawBoard(window, BOARD, CARD_BOARD, square)
                #print_b(BOARD)
                if gameOver == True:
                    if winner == True:
                        print("You win memory path")
                    else:
                        print("You lose memory path")
                    drawWin(window, winner, width)
                    pygame.display.update()
                    pygame.time.wait(3000)
    return winner


