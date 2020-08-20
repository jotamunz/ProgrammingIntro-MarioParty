import pygame
import random
import sys
import math

#====================================================================
#                           GLOBALS
#====================================================================

white = (255,255,255)
black = (0,0,0)

cat_circle = pygame.image.load("Catch_Cat/Figures/circle.png")
cat_mario = pygame.image.load("Catch_Cat/Figures/mario_run.png")
cat_goomba = pygame.image.load("Catch_Cat/Figures/goomba.png")

#====================================================================
#                          FUNCTIONS
#====================================================================

def print_b(board):
    for i in board:
        print (i)

def available(board, row, col):
    if board[row][col] == 0:
        return True
    else:
        return False

def select(board, row, col):
    board[row][col] = 1

def catPosition(board):
    for i in range (0, len(board)):
        for j in range (0, len(board[0])):
            if board[i][j] == 2:
                pos = [i, j]
    return pos

def bestMove(board):
    catPos = catPosition(board)
    i = catPos[0]
    j = catPos[1]
    #Horizontal Right
    if 1 in board[i][j:]:
        for col in range(j, 11):
            if board[i][col] == 1:
                distanceRight = [11 - (col - j), 0, 1]
                break
    else:
        distanceRight = [11 - (j + 1), 0, 1]
    #Horizontal Left
    if 1 in board[i][:j]:
        for col in range(0, j):
            if board[i][col] == 1:
                distanceLeft = [11 - (j - col), 0, -1]
    else:
        distanceLeft = [j, 0, -1]
    if i%2 == 0:
        #Upper Right
        row = i - 1
        col = j
        distanceTopRight = [i, -1, 0]
        while row >= 0 and col < len(board[0]):
            if board[row][col] == 1:
                distanceTopRight = [11 - (i - row), -1, 0]
                break
            else:
                if row % 2 != 0:
                    col += 1
                row -= 1
        #Upper Left
        row = i - 1
        col = j - 1
        distanceTopLeft = [i, -1, -1]
        while row >= 0 and col >= 0:
            if board[row][col] == 1:
                distanceTopLeft = [11 - (i - row), -1, -1]
                break
            else:
                if row % 2 == 0:
                    col -= 1
                row -= 1
        #Lower Right
        row = i + 1
        col = j
        distanceBotRight = [11 - (i + 1), 1, 0]
        while row < len(board) and col < len(board[0]):
            if board[row][col] == 1:
                distanceBotRight = [11 - (row - i), 1, 0]
                break
            else:
                if row % 2 != 0:
                    col += 1
                row += 1
        #Lower Left
        row = i + 1
        col = j - 1
        distanceBotLeft = [11 - (i + 1), 1, -1]
        while row < len(board) and col >= 0:
            if board[row][col] == 1:
                distanceBotLeft = [11 - (row - i), 1, -1]
                break
            else:
                if row % 2 == 0:
                    col -= 1
                row += 1
    else:
        # Upper Right
        row = i - 1
        col = j + 1
        distanceTopRight = [i, -1, 1]
        while row >= 0 and col < len(board[0]):
            if board[row][col] == 1:
                distanceTopRight = [11 - (i - row), -1, 1]
                break
            else:
                if row % 2 != 0:
                    col += 1
                row -= 1
        # Upper Left
        row = i - 1
        col = j
        distanceTopLeft = [i, -1, 0]
        while row >= 0 and col >= 0:
            if board[row][col] == 1:
                distanceTopLeft = [11 - (i - row), -1, 0]
                break
            else:
                if row % 2 == 0:
                    col -= 1
                row -= 1
        # Lower Right
        row = i + 1
        col = j + 1
        distanceBotRight = [11 - (i + 1), 1, 1]
        while row < len(board) and col < len(board[0]):
            if board[row][col] == 1:
                distanceBotRight = [11 - (row - i), 1, 1]
                break
            else:
                if row % 2 != 0:
                    col += 1
                row += 1
        # Lower Left
        row = i + 1
        col = j
        distanceBotLeft = [11 - (i + 1), 1, 0]
        while row < len(board) and col >= 0:
            if board[row][col] == 1:
                distanceBotLeft = [11 - (row - i), 1, 0]
                break
            else:
                if row % 2 == 0:
                    col -= 1
                row += 1
    posibleMoves = [distanceRight, distanceLeft, distanceTopRight, distanceTopLeft, distanceBotRight, distanceBotLeft]
    moveValue = [distanceRight[0], distanceLeft[0], distanceTopRight[0], distanceTopLeft[0], distanceBotRight[0], distanceBotLeft[0]]
    for move in posibleMoves:
        if move[0] == min(moveValue):
            return move

def moveCat(board, row, col, prevRow, prevCol):
    board[prevRow][prevCol] = 0
    board[row][col] = 2

def checkWin(board):
    catPos = catPosition(board)
    i = catPos[0]
    j = catPos[1]
    if board[i][j+1] == 0:
        return False
    if board[i][j-1] == 0:
        return False
    if board[i-1][j] == 0:
        return False
    if board[i+1][j] == 0:
        return False
    if i % 2 == 0:
        if board[i-1][j-1] == 0:
            return False
        if board[i+1][j-1] == 0:
            return False
    if i % 2 != 0:
        if board[i-1][j+1] == 0:
            return False
        if board[i+1][j+1] == 0:
            return False
    return True

def checkWinCat(board):
    catPos = catPosition(board)
    i = catPos[0]
    j = catPos[1]
    if i == 0 or i == 10:
        return True
    if j == 0 or j == 10:
        return True
    else:
        return False

def validClick(col):
    if col >= 0 and col < 11:
        return True
    else:
        return False

#====================================================================
#                          GRAPHICS
#====================================================================

def drawBoard(window, board, square):
    for row in range(0, len(board)):
        for column in range(0, len(board[0])):
            #pygame.draw.rect(window, white, (column * square, row * square, square, square))
            if row%2 == 0:
                window.blit(cat_circle, (column * square, row * square))
                if board[row][column] == 1:
                    window.blit(cat_goomba, (column * square, row * square))
                if board[row][column] == 2:
                    window.blit(cat_mario, (column * square, row * square))
            else:
                window.blit(cat_circle, (column * square + 25, row * square))
                if board[row][column] == 1:
                    window.blit(cat_goomba, (column * square + 25, row * square))
                if board[row][column] == 2:
                    window.blit(cat_mario, (column * square + 25, row * square))
    pygame.display.update()

#====================================================================
#                          GAME LOOP
#====================================================================

def playCatch():
    global cat_circle, cat_mario, cat_goomba

    BOARD = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
             [0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 2, 0, 0, 0, 1, 0],
             [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]

    square = 50
    width = 11 * square + 25
    height = 11 * square

    pygame.init()

    window = pygame.display.set_mode((width, height))
    window.fill(white)
    pygame.display.set_caption('Catch The Cat')
    myFont = pygame.font.SysFont('Arial', 50)

    pygame.mixer.music.load("Catch_Cat/Music/Slide.mp3")
    pygame.mixer.music.set_volume(0.5)
    pygame.mixer.music.play(-1)

    cat_circle = pygame.transform.scale(cat_circle, (square, square)).convert_alpha()
    cat_mario = pygame.transform.scale(cat_mario, (square, square)).convert_alpha()
    cat_goomba = pygame.transform.scale(cat_goomba, (square, square)).convert_alpha()

    gameOver = False
    turn = False
    #print_b(BOARD)

    while not gameOver:
        drawBoard(window, BOARD, square)
        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                if turn == False:
                    clickY = event.pos[1]
                    row = math.floor(clickY / square)
                    clickX = event.pos[0]
                    col = math.floor(clickX / square)
                    if row%2 != 0:
                        col = math.floor((clickX - 25) / square)
                    if validClick(col) == True:
                        if available(BOARD, row, col) == True:
                            select(BOARD, row, col)
                            #print_b(BOARD)
                            drawBoard(window, BOARD, square)
                            turn = not turn
                            if checkWin(BOARD) == True:
                                gameOver = True
                                winner = True

            if turn == True:
                move = bestMove(BOARD)
                catPos = catPosition(BOARD)
                row = move[1] + catPos[0]
                col = move[2] + catPos[1]
                if available(BOARD, row, col) == True:
                    moveCat(BOARD, row, col, catPos[0], catPos[1])
                    #print_b(BOARD)
                    drawBoard(window, BOARD, square)
                    turn = not turn
                    if checkWinCat(BOARD) == True:
                        gameOver = True
                        winner = False

            if gameOver == True:
                if winner == True:
                    print("You win catch the cat")
                else:
                    print("You lose catch the cat")
                pygame.display.update()
                pygame.time.wait(3000)
    return winner