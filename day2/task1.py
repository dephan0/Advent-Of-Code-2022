#!/usr/bin/env python3
"""
elf:
A for Rock, B for Paper, and C for Scissors
me:
X for Rock, Y for Paper, and Z for Scissors
"""

# convert A,B,C to X,Y,Z
elf_to_me = {
    'A' : 'X',
    'B' : 'Y',
    'C' : 'Z' 
}

shape_cost = {
    'X' : 1,
    'Y' : 2,
    'Z' : 3
}

# A win against A (Rock) is Y (paper)
winning_response = {
    'A' : 'Y',
    'B' : 'Z',
    'C' : 'X',
}

def main():
    total_score = 0
    with open('input.txt', 'r') as input_file:
        for line in input_file:
            fields = line.strip().split(' ')
            score = 0
            elf_play = fields[0]
            my_response = fields[1]

            # add the shape cost to each score
            score += shape_cost[my_response]
            
            if elf_to_me[elf_play] == my_response: # draw
                score += 3
            elif winning_response[elf_play] == my_response: # win
                score += 6
            # else, if the round was lost, dont add any point

            total_score += score

    print(total_score)


if __name__ == '__main__':
    main()
