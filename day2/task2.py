#!/usr/bin/env python3
"""
elf:
A for Rock, B for Paper, and C for Scissors
strategy:
X lose, Y draw, and Z win
"""

shape_cost = {
    'A' : 1,
    'B' : 2,
    'C' : 3
}

shape_to_lose = {
    'A' : 'C',
    'B' : 'A',
    'C' : 'B',
}

def main():
    total_score = 0
    with open('input.txt', 'r') as input_file:
        for line in input_file:
            fields = line.strip().split(' ')
            elf_play = fields[0]
            my_strategy = fields[1]

            score = 0
            if my_strategy == 'X': # lose
                my_play = shape_to_lose[elf_play]
            elif my_strategy == 'Y': # draw
                my_play = elf_play
                score += 3
            elif my_strategy == 'Z': # win
                shapes = list(shape_cost.keys())
                shapes.remove(elf_play) 
                shapes.remove(shape_to_lose[elf_play])
                my_play = shapes[0]
                score += 6

            score += shape_cost[my_play]
            total_score += score
    
    print(total_score)

if __name__ == '__main__':
    main()
