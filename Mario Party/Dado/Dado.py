import pygame
import random

def pantalla():

    #lados del dado
    num_1 = pygame.image.load("Dado/1.png")
    num_2 = pygame.image.load("Dado/2.png")
    num_3 = pygame.image.load("Dado/3.png")
    num_4 = pygame.image.load("Dado/4.png")
    num_5 = pygame.image.load("Dado/bowser_icon.png")
    num_5 = pygame.transform.scale(num_5,(100,100))
    dado = pygame.image.load("Dado/dado.png")
    bg = pygame.image.load("Dado/bg.jpg")

    bg = pygame.transform.scale(bg,(500,500))
    num_1 = pygame.transform.scale(num_1, (100, 100))
    num_2 = pygame.transform.scale(num_2, (100, 100))
    num_3 = pygame.transform.scale(num_3, (100, 100))
    num_4 = pygame.transform.scale(num_4, (100, 100))
    num_5 = pygame.transform.scale(num_5, (100, 100))
    dado = pygame.transform.scale(dado, (130, 130))

    pygame.init()
    screen = pygame.display.set_mode((500, 500))
    clock = pygame.time.Clock()
    count = 0

    imagen_mostrar = num_1
    num = 0

    roll = True
    done = False
    #Loop
    while not done:
        screen.blit(bg, (0, 0))
        screen.blit(dado, (185, 185))
        # print(pygame.mouse.get_pos())
        keys = pygame.key.get_pressed()
        if keys[pygame.K_SPACE] and roll == False:
            roll = True
        elif roll == True and keys[pygame.K_SPACE] and num != 0:
            #print(num)
            done = True
            # return num
            # return num
            roll = False
        if roll == True:
            count += 1
            if count == 5:
                count = 0
                num = random.randrange(1, 7)
                if num == 1:
                    imagen_mostrar = num_1
                    # screen.blit(num_1,(200,200))
                elif num == 2:
                    imagen_mostrar = num_2
                    # screen.blit(num_2,(200,200))
                elif num == 3:
                    imagen_mostrar = num_3
                    # screen.blit(num_3,(200,200))
                elif num == 4:
                    imagen_mostrar = num_4
                    # screen.blit(num_4,(200,200))
                elif num == 5:
                    imagen_mostrar = num_5
                    # screen.blit(num_5,(200,200))
                else:
                    imagen_mostrar = num_5
                    # screen.blit(num_5,(200,200))

        # pygame.draw.rect(window, red, (200, 200, 100, 100))
        screen.blit(imagen_mostrar, (200, 200))
        pygame.display.flip()
        clock.tick(100)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
    return num

