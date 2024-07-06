'''
Lesson 30 - Tetris
'''
#Red Tea Infusion Full Python Course Review
#---positives---
#free python lessons are always a good thing. red tea infusion seems to have been a self-taught coder. 
#quick bite sized lessons. most less than 10 minutes.
#showed various ways to write the same code.
#people learn differently so options are good. 
#I feel much better with reading the code. I'm confident in creating simple strings, variables, lists, among other things.
#like anything, the more reps you take, the better I will get.
# Building complex apps like video games will take more time
#-negatives
#following along with the video was frustrating to say the least
#the audio was very low and needs to be turned all the way up with headphones or loud speakers. not ideal. 
#we'd right a block a code and then have to go back and import or input some other code to make that code valid
#the videos were slightly out of order, in my opinion
#i would have introduced the main block and sets earlier in the course
#all of the lessons worked well except for the tetris and snake game. 
#for the games I had to get the file from the repository for the code. 
#it was clean code. But video was poor. 
#kept back tracking on what needed to be in put
#foreign accent may be difficult for some learners

#Final Score | D+ (65.6/100)
# ---Stat Breakdown---
#syntax - 4.5/5 - clean quality code for 27/30 lessons
#Overall instruction - 3.35/5 - Covered a wide range of topics that are necessary to learn the fundamentals of pyhton. some lessons seemingly were out of order. foreign accent and constant backtracking will make it difficult to follow for some learners.
#audio - 2/5 - have to use headphones, use loud speakers, or be somewhere quiet. poor audio is not ideal for the full course instruction.

from os import system
from time import sleep
from random import choice
from msvcrt import kbhit, getch

BOARD_WIDTH = 10
BOARD_HEIGHT = 20
DROP_RATE = 3
SHAPES = [
    [[1, 1, 1],
     [0, 1, 0]],
    [[0, 2, 2],
     [2, 2, 0]],
    [[3, 3, 0],
     [0, 3, 3]],
    [[4, 0, 0],
     [4, 4, 4]],
    [[0, 0, 5],
     [5, 5, 5]],
    [[6, 6],
     [6, 6]],
    [[7, 7, 7, 7]]
]
COLORS = [
    '\033[38;5;8m',    # Grey
    '\033[38;5;93m',   # Magenta
    '\033[38;5;40m',   # Green
    '\033[38;5;9m',    # Red
    '\033[38;5;33m',   # Blue
    '\033[38;5;208m',  # Orange
    '\033[38;5;11m',   # Yellow
    '\033[38;5;51m'    # Cyan
]
playing = True
board = [[0 for _ in range(BOARD_WIDTH)] for _ in range(BOARD_HEIGHT)]
block = choice(SHAPES)
block_x = BOARD_WIDTH // 2 - 2
block_y = 0
score = 0
lines = 0

def print_board():
    block_color = [c for c in block[0] if c != 0][0]
    system('cls')
    for y in range(BOARD_HEIGHT):
        for x in range(BOARD_WIDTH):
            if x in range(block_x, block_x + len(block[0])) and \
                  y in range(block_y, block_y + len(block)):
                if block[y - block_y][x - block_x] != 0:
                    print(COLORS[block_color] + '■' + COLORS[0], end=' ')
                else:
                    print(COLORS[board[y][x]] + '.' + COLORS[0], end=' ')
            else:
                if board[y][x] != 0:
                    print(COLORS[board[y][x]] + '■' + COLORS[0], end=' ')
                else:
                    print(COLORS[board[y][x]] + '.' + COLORS[0], end=' ')
        print()
    print('-' * (BOARD_WIDTH * 2 - 1))
    print(f'Lines: {lines} Score: {score}')

def move_down():
    global block_y
    if detect_collision(block_x, block_y + 1, block):
        place_block()
    else:
        block_y += 1

def detect_collision(x, y, block):
    for row in range(len(block)):
        for col in range(len(block[0])):
            if block[row][col] != 0:
                if x + col < 0 or \
                    x + col >= BOARD_WIDTH or \
                        y + row >= BOARD_HEIGHT:
                    return True
                if board[y + row][x + col] != 0:
                    return True
    return False

def place_block():
    global block_x, block_y, block
    block_color = [c for c in block[0] if c != 0][0]
    for row in range(len(block)):
        for col in range(len(block[0])):
            if block[row][col] != 0:
                board[block_y + row][block_x + col] = block_color
    block = choice(SHAPES)
    block_x = BOARD_WIDTH // 2 - 2
    block_y = 0
    if detect_collision(block_x, block_y, block):
        game_over()

def game_over():
    global playing
    playing = False

def get_pressed_key():
    key = ''
    while kbhit():
        key = getch().decode()[0]
    return key

def get_input():
    key = get_pressed_key()
    match key:
        case 'q':
            game_over()
        case 'a':
            move_left()
        case 'd':
            move_right()
        case 's':
            move_down()
        case 'w':
            rotate_block()

def move_left():
    global block_x
    if not detect_collision(block_x - 1, block_y, block):
        block_x -= 1

def move_right():
    global block_x
    if not detect_collision(block_x + 1, block_y, block):
        block_x += 1

def rotate_block():
    global block
    rotated_block = [[block[j][i] for j in range(len(block))] \
                      for i in range(len(block[0]) -1, -1, -1)]
    if not detect_collision(block_x, block_y, rotated_block):
        block = rotated_block

def clear_rows():
    global board, score, lines
    new_board = [[0 for _ in range(BOARD_WIDTH)]\
                  for _ in range(BOARD_HEIGHT)]
    row_index = BOARD_HEIGHT - 1
    count = 0
    is_full = lambda row: all(board[row])
    for row in range(BOARD_HEIGHT -1, -1, -1):
        if is_full(row):
            lines += 1
            count += 1
            continue
        new_board[row_index] = board[row]
        row_index -= 1
    
    score += [0, 40, 100, 300, 1200][count]
    board = new_board

def main():
    while playing:
        get_input()
        move_down()
        clear_rows()
        print_board()
        sleep(1 / DROP_RATE)

if __name__ == '__main__':
    main() 