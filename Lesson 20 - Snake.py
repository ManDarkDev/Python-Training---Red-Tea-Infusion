import os
import time
import random
import msvcrt

BOARD_WIDTH = 20
BOARD_HEIGHT = 5
DIFFICULTY = 8

def create_fruit(tail_positions):
    fruit_position = [random.randint(1, BOARD_WIDTH), random.randint(1, BOARD_HEIGHT)]
    while fruit_position in tail_positions:
    
        def create_board(fruit_position, head_position, tail_positions):
            board = ''
    for i in range (BOARD_HEIGHT + 2):
        for j in range(BOARD_WIDTH + 2):
            if i == 0 or j == 0 or i == BOARD_HEIGHT + 1 or j == BOARD_WIDTH +1:
                board+= '#'
            elif fruit_position == [j, i]:
                board += 'F'
            elif head_position == [j, i]:
                board += 'O'
            elif[j, i] in tail_positions:
                board += 'o'
            else:
                board += ' '
        board += '\n'
    return board

def draw(fruit_position, head_position, tail_positions):
    tail_positions
    board = create_board(fruit_position, head_position, tail_positions)
    os.system('cls')
    print(board)
    
    def get_pressed_key():
        if msvcrt.kbhit():
            return msvcrt.getch().decode()
        else:
            return ''
            
def move(head_position, directions):
    key = get_pressed_key()
    if key == 'd':
        head_position[0] += 1
        directions['RIGHT'] = True
    elif key == 'a':
        head_position[0] -= 1
        directions ['LEFT'] = True
    elif key == 's':
        head_position[1] += 1
        directions['DOWN'] = True    
    elif key == 's':
        head_position[1] -= 1
        directions['UP'] = True           
    else:
        if directions['RIGHT'] == True:
            head_position[0] += 1
        elif directions['LEFT'] == True:
            head_position

def main():
    head_position = [BOARD_WIDTH // 2, BOARD_HEIGHT // 2]
    tail_positions = [head_position.copy()]
    fruit_position = create_fruit(tail_positions)
    
    
    while True:
        draw(fruit_position, head_position, tail_positions)
        
        time.sleep(1 / DIFFICULTY)
        
main()