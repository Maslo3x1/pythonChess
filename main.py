'''
2 player chess game in Python 3
'''
import pygame as p
p.init()

#game setup

WIDTH = 1000
HEIGHT = 900
screen = p.display.set_mode([WIDTH, HEIGHT])
p.display.set_caption('2 player chess!')
font = p.font.Font('freesansbold.ttf', 20)
big_font = p.font.Font('freesansbold.ttf', 50)
timer = p.time.Clock()
fps = 60

#game variables and images

black_pieces = ['rook', 'knight', 'bishop', 'king', 'queen', 'bishop', 'knight', 'rook',
                'pawn', 'pawn', 'pawn', 'pawn', 'pawn', 'pawn', 'pawn', 'pawn']
black_locations = [(0, 0), (1, 0), (2, 0), (3, 0), (4, 0), (5, 0), (6, 0), (7, 0),
                   (0, 1), (1, 1), (2, 1), (3, 1), (4, 1), (5, 1), (6, 1), (7, 1)]
white_pieces = ['rook', 'knight', 'bishop', 'king', 'queen', 'bishop', 'knight', 'rook',
                'pawn', 'pawn', 'pawn', 'pawn', 'pawn', 'pawn', 'pawn', 'pawn']
white_locations = [(0, 7), (1, 7), (2, 7), (3, 7), (4, 7), (5, 7), (6, 7), (7, 7),
                   (0, 6), (1, 6), (2, 6), (3, 6), (4, 6), (5, 6), (6, 6), (7, 6)]
captured_pieces_white = []
captured_pieces_black = []

# 0 - whites turn no selection: 1-whites turn piece selected: 2- black turn no selection, 3 - black turn piece selected

turn_step = 0
selection = 100
valid_moves = []

# load in game piece images (queen, king, rook, bishop, knight, pawn) x 2

black_queen = p.image.load('assets/images/black queen.png')
black_queen = p.transform.scale(black_queen, (80, 80))
black_queen_small = p.transform.scale(black_queen, (45, 45))
black_king = p.image.load('assets/images/black king.png')
black_king = p.transform.scale(black_king, (80, 80))
black_king_small = p.transform.scale(black_king, (45, 45))
black_rook = p.image.load('assets/images/black rook.png')
black_rook = p.transform.scale(black_rook, (80, 80))
black_rook_small = p.transform.scale(black_rook, (45, 45))
black_bishop = p.image.load('assets/images/black bishop.png')
black_bishop = p.transform.scale(black_bishop, (80, 80))
black_bishop_small = p.transform.scale(black_bishop, (45, 45))
black_knight = p.image.load('assets/images/black knight.png')
black_knight = p.transform.scale(black_knight, (80, 80))
black_knight_small = p.transform.scale(black_knight, (45, 45))
black_pawn = p.image.load('assets/images/black pawn.png')
black_pawn = p.transform.scale(black_pawn, (65, 65))
black_pawn_small = p.transform.scale(black_pawn, (45, 45))
white_queen = p.image.load('assets/images/white queen.png')
white_queen = p.transform.scale(white_queen, (80, 80))
white_queen_small = p.transform.scale(white_queen, (45, 45))
white_king = p.image.load('assets/images/white king.png')
white_king = p.transform.scale(white_king, (80, 80))
white_king_small = p.transform.scale(white_king, (45, 45))
white_rook = p.image.load('assets/images/white rook.png')
white_rook = p.transform.scale(white_rook, (80, 80))
white_rook_small = p.transform.scale(white_rook, (45, 45))
white_bishop = p.image.load('assets/images/white bishop.png')
white_bishop = p.transform.scale(white_bishop, (80, 80))
white_bishop_small = p.transform.scale(white_bishop, (45, 45))
white_knight = p.image.load('assets/images/white knight.png')
white_knight = p.transform.scale(white_knight, (80, 80))
white_knight_small = p.transform.scale(white_knight, (45, 45))
white_pawn = p.image.load('assets/images/white pawn.png')
white_pawn = p.transform.scale(white_pawn, (65, 65))
white_pawn_small = p.transform.scale(white_pawn, (45, 45))

white_images = [white_pawn, white_queen, white_king, white_knight, white_rook, white_bishop]

small_white_images = [white_pawn_small, white_queen_small, white_king_small, white_knight_small,
                      white_rook_small, white_bishop_small]
black_images = [black_pawn, black_queen, black_king, black_knight, black_rook, black_bishop]

small_black_images = [black_pawn_small, black_queen_small, black_king_small, black_knight_small,
                      black_rook_small, black_bishop_small]

piece_list = ['pawn', 'queen', 'king', 'knight', 'rook', 'bishop']

#check variables / flashing counter

#draw main game board

def draw_board():
    for i in range(32):
        column = i % 4
        row = i // 4
        if row % 2 == 0:
            p.draw.rect(screen, 'light grey', [600 - (column * 200), row * 100, 100, 100])
        else:
            p.draw.rect(screen, 'light grey', [700 - (column * 200), row * 100, 100, 100])
        p.draw.rect(screen, 'gray', [0, 800, WIDTH, 100])
        p.draw.rect(screen, 'gold', [0, 800, WIDTH, 100], 5)
        p.draw.rect(screen, 'gold', [800, 0, 200, HEIGHT], 5)
        status_text = ["White: select a piece to move.", "White: select a destination.", "Black: select a piece to move.", "Black: select a destination."]
        screen.blit(big_font.render(status_text[turn_step], True, 'black'), (20, 820))
        for i in range(9):
            p.draw.line(screen, 'black', (0, 100 * i), (800, 100 * i), 2)
            p.draw.line(screen, 'black', (100 * i, 0), (100 * i, 800), 2)

#draw pieces onto a board

def draw_pieces():
    for i in range(len(white_pieces)):
        index = piece_list.index(white_pieces[i])
        if white_pieces[i] == 'pawn':
            screen.blit(white_pawn, (white_locations[i][0] * 100 + 22, white_locations[i][1] * 100 + 30))
        else:
            screen.blit(white_images[index], (white_locations[i][0] * 100 + 10, white_locations[i][1] * 100 + 10))
        if turn_step < 2:
            if selection == i:
                p.draw.rect(screen, 'red', [white_locations[i][0] * 100 + 1], [white_locations[i][0] * 100 + 1, 100, 100], 2)

    for i in range(len(black_pieces)):
        index = piece_list.index(black_pieces[i])
        if black_pieces[i] == 'pawn':
            screen.blit(black_pawn, (black_locations[i][0] * 100 + 22, black_locations[i][1] * 100 + 30))
        else:
            screen.blit(black_images[index], (black_locations[i][0] * 100 + 10, black_locations[i][1] * 100 + 10))
        if turn_step >= 2:
            if selection == i:
                p.draw.rect(screen, 'blue', [black_locations[i][0] * 100 + 1], [black_locations[i][0] * 100 + 1, 100, 100], 2)

# function to check all pieces valid options on board

def check_options():
    pass

#game loop

run = True
while run:
    timer.tick(fps)
    screen.fill('dark grey')
    draw_board()
    draw_pieces()

    #event handling

    for event in p.event.get():
        if event.type == p.QUIT:
            run = False
        if event.type == p.MOUSEBUTTONDOWN and event.button == 1:
            x_coord = event.pos[0] // 100
            y_coord = event.pos[1] // 100
            click_coord = (x_coord, y_coord)
            if turn_step < 2:
                if click_coord == white_locations:
                    selection = white_locations.index(click_coord)
                    if turn_step == 0:
                        turn_step  = 1
                if click_coord in valid_moves and selection != 100:
                    white_locations[selection] = click_coord
                    if click_coord in black_locations:
                        black_piece = black_locations.index(click_coord)
                        captured_pieces_white.append(black_pieces[black_piece])
                        black_pieces.pop(black_piece)
                        black_locations.pop(black_piece)
                    black_options = check_options(black_pieces, black_locations, 'black')
                    white_options = check_options(white_pieces, white_locations, 'white')
                    turn_step = 2
                    selection = 100
                    valid_moves = []
            if turn_step > 1:
                if click_coord == black_locations:
                    selection = black_locations.index(click_coord)
                    if turn_step == 2:
                        turn_step  = 3
                if click_coord in valid_moves and selection != 100:
                    black_locations[selection] = click_coord
                    if click_coord in white_locations:
                        white_piece = white_locations.index(click_coord)
                        captured_pieces_black.append(white_pieces[white_piece])
                        white_pieces.pop(white_piece)
                        white_locations.pop(white_piece)
                    black_options = check_options(black_pieces, black_locations, 'black')
                    white_options = check_options(white_pieces, white_locations, 'white')
                    turn_step = 0
                    selection = 100
                    valid_moves = []

    p.display.flip()

p.quit()

