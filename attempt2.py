import random, pygame
from pygame.locals import *

CYAN = (47, 199, 238)
BLUE = (0, 0, 254)
ORANGE = (239, 121, 34)
YELLOW = (247, 212, 8)
GREEN = (0, 255, 0)
PURPLE = (173, 78, 160)
RED = (255, 0, 0)
COLOURS = (CYAN, BLUE, ORANGE, YELLOW, GREEN, PURPLE, RED)

S = [['...',
      '.OO',
      'OO.',
      '...']]
Z = [['...',
      'OO.',
      '.OO',
      '...']]
I = [['.O.',
      '.O.',
      '.O.',
      '.O.',]]
O = [['...',
      'OO.',
      'OO.',
      '...']]
J = [['...',
      'O..',
      'OOO',
      '...',]]
L = [['...',
      '..O',
      'OOO',
      '...',]]
T = [['...',
      '.O.',
      'OOO',
      '...',]]
PIECELIST = {'S': S, 'Z': Z, 'J': J, 'L': L, 'I': I, 'O': O, 'T': T}

pygame.init()
DISPLAY = pygame.display.set_mode((200, 400))
icon = pygame.image.load('tetris.png')
pygame.display.set_caption('Tetris')
pygame.display.set_icon(icon)

def game():
    delay = 250
    board = BlankBoard()
    piece = NewPiece()
    
    while True:
        pygame.time.delay(delay) 
        if piece == None:
            piece = NewPiece()

        for event in pygame.event.get():
            if event.type == KEYDOWN:
                if (event.key == K_LEFT) and ValidPosition(board, piece, adjacentX=-1):
                    piece['x'] -= 1
                elif (event.key == K_RIGHT) and ValidPosition(board, piece, adjacentX=1):
                    piece['x'] += 1
            elif event.type == pygame.QUIT:
                exit()

        if not ValidPosition(board, piece, adjacentY=1):
            addToBoard(board, piece)
            piece = None
        else:
            piece['y'] += 1
        DISPLAY.fill((0, 10, 50))
        drawBoard(board)
        if piece != None:
            drawPiece(piece)
        pygame.display.update()

def ValidPosition(board, piece, adjacentX=0, adjacentY=0):
    for x in range(3):
        for y in range(4):
            aboveboard = y + piece['y'] + adjacentY < 0
            if aboveboard or PIECELIST[piece['shape']][0][y][x] == '.':
                continue
            elif not OnBoard(x + piece['x'] + adjacentX, y + piece['y'] + adjacentY):
                return False
            elif board[x + piece['x'] + adjacentX][y + piece['y'] + adjacentY] != '.':
                return False
    return True

def NewPiece():
    shape = random.choice(list(PIECELIST))
    if shape == 'S':
        tempcolour = 4
    elif shape == 'O':
        tempcolour = 3
    elif shape == 'I':
        tempcolour = 0
    elif shape == 'T':
        tempcolour = 5
    elif shape == 'Z':
        tempcolour = 6
    elif shape == 'J':
        tempcolour = 1
    elif shape == 'L':
        tempcolour = 2
    newPiece = {'shape': shape,
                'x': 4,
                'y': 0, 
                'colour': tempcolour}
    return newPiece

def OnBoard(x, y):
    return x >= 0 and x < 10 and y < 20

def addToBoard(board, piece):
    for x in range(3):
        for y in range(4):
            if PIECELIST[piece['shape']][0][y][x] != '.':
                board[x + piece['x']][y + piece['y']] = piece['colour']

def BlankBoard():
    board = []
    for i in range(10):
        board.append(['.'] * 20)
    return board

def drawBoard(board):
    for x in range(10):
        for y in range(20):
            drawBox(x, y, board[x][y])

def drawBox(box_x, box_y, colour, pixel_x=None, pixel_y=None):
    if colour == '.':
        return
    if pixel_x == None and pixel_y == None:
        pixel_x = box_x * 20
        pixel_y = box_y * 20
    pygame.draw.rect(DISPLAY, COLOURS[colour], (pixel_x, pixel_y, 20, 20))

def drawPiece(piece, pixel_x=None, pixel_y=None):
    if pixel_x == None and pixel_y == None:
        pixel_x = piece['x'] * 20 
        pixel_y = piece['y'] * 20
    for x in range(3):
        for y in range(4):
            if PIECELIST[piece['shape']][0][y][x] != '.':
                drawBox(None, None, piece['colour'], pixel_x + (x * 20), pixel_y + (y * 20))
game()
