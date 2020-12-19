import pygame, random

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
CYAN = (47, 199, 238)
BLUE = (0, 0, 254)
ORANGE = (239, 121, 34)
YELLOW = (247, 212, 8)
GREEN = (0, 255, 0)
PURPLE = (173, 78, 160)
RED = (255, 0, 0)
WIDTH = 20
HEIGHT = 20
MARGIN = 2
grid = []
for row in range(24): ##making the grid
    grid.append([])
    for column in range(10):
        grid[row].append(0)

randomshape = random.randint(1, 7)

pygame.init()
screensize = [255, 255]
screen = pygame.display.set_mode([222, 530])
pygame.display.set_caption("Tetris")

done = False

ycoord = 3
xcoord = 4
delay = 200

while not done:
    
    pygame.time.delay(delay) 
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT: 
            done = True  
            pygame.quit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                xcoord = xcoord - 1
            if event.key == pygame.K_RIGHT:
                xcoord = xcoord + 1
  
    ycoord = ycoord + 1 

    if randomshape == 1 : #Oshape
        grid[ycoord - 1][xcoord] = randomshape
        grid[ycoord][xcoord] = randomshape
        grid[ycoord - 1][xcoord + 1] = randomshape
        grid[ycoord][xcoord + 1] = randomshape
        
        grid[ycoord - 2][xcoord] = 0
        grid[ycoord - 2][xcoord + 1] = 0

    elif randomshape == 2 : #Ishape
        grid[ycoord - 3][xcoord] = randomshape
        grid[ycoord - 2][xcoord] = randomshape
        grid[ycoord - 1][xcoord] = randomshape 
        grid[ycoord][xcoord] = randomshape
    
        grid[ycoord - 4][xcoord] = 0

    elif randomshape == 3 : #Jshape
        grid[ycoord - 2][xcoord] = randomshape
        grid[ycoord - 1][xcoord] = randomshape
        grid[ycoord][xcoord] = randomshape 
        grid[ycoord][xcoord - 1] = randomshape

        grid[ycoord - 3][xcoord] = 0
        grid[ycoord - 2][xcoord - 1] = 0
        grid[ycoord - 1][xcoord - 1] = 0

    elif randomshape == 4 : #Lshape
        grid[ycoord - 2][xcoord] = randomshape
        grid[ycoord - 1][xcoord] = randomshape
        grid[ycoord][xcoord] = randomshape 
        grid[ycoord][xcoord + 1] = randomshape

        grid[ycoord - 3][xcoord] = 0
        grid[ycoord - 2][xcoord + 1] = 0
        grid[ycoord - 1][xcoord + 1] = 0

    elif randomshape == 5 : #Zshape
        grid[ycoord - 1][xcoord] = randomshape
        grid[ycoord - 1][xcoord + 1] = randomshape
        grid[ycoord][xcoord + 1] = randomshape 
        grid[ycoord][xcoord + 2] = randomshape
    
        grid[ycoord - 2][xcoord] = 0
        grid[ycoord - 2][xcoord + 1] = 0
        grid[ycoord - 1][xcoord + 2] = 0

    elif randomshape == 6 : #Tshape
        grid[ycoord - 1][xcoord + 1] = randomshape
        grid[ycoord][xcoord] = randomshape
        grid[ycoord][xcoord + 1] = randomshape 
        grid[ycoord][xcoord + 2] = randomshape

        grid[ycoord - 1][xcoord] = 0
        grid[ycoord - 1][xcoord + 2] = 0
        grid[ycoord - 2][xcoord + 1] = 0

    elif randomshape == 7 : #Sshape
        grid[ycoord][xcoord] = randomshape
        grid[ycoord - 1][xcoord + 1] = randomshape
        grid[ycoord][xcoord + 1] = randomshape 
        grid[ycoord - 1][xcoord + 2] = randomshape
    
        grid[ycoord - 1][xcoord] = 0
        grid[ycoord - 2][xcoord + 1] = 0
        grid[ycoord - 2][xcoord + 2] = 0

    for row in range(24): #draw colours
        for column in range(10):
            color = WHITE
            if grid[row][column] == 1:
                color = YELLOW
            elif grid[row][column] == 2:
                color = CYAN
            elif grid[row][column] == 3:
                color = BLUE
            elif grid[row][column] == 4:
                color = ORANGE
            elif grid[row][column] == 5:
                color = RED
            elif grid[row][column] == 6:
                color = PURPLE
            elif grid[row][column] == 7:
                color = GREEN           
            pygame.draw.rect(screen,
                             color,
                             [(MARGIN + WIDTH) * column + MARGIN,
                              (MARGIN + HEIGHT) * row + MARGIN,
                              WIDTH,
                              HEIGHT])
            pygame.display.flip()