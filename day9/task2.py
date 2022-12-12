#!/usr/bin/env python3

pos_after_motion = {
    'U' : lambda pos: [pos[0], pos[1] + 1],
    'D' : lambda pos: [pos[0], pos[1] - 1],
    'R' : lambda pos: [pos[0] + 1, pos[1]],
    'L' : lambda pos: [pos[0] - 1, pos[1]],
}

# used for the extended example
def print_knots(knots_pos):
    for i in range(15, -6, -1):
        for j in range(-11, 15):
            to_print = '.'
            for ind, knot in enumerate(reversed(knots_pos)):
                if knot[0] == j and knot[1] == i:
                    to_print = len(knots_pos) - ind - 1
                    to_print = 'H' if to_print == 0 else to_print
            print(to_print, end='')
        print()
    print()


def are_touching(pos1, pos2):
    if abs(pos1[0] - pos2[0]) <= 1 and abs(pos1[1] - pos2[1]) <= 1:
        return True 
    return False


def next_move(knot, knot_after):
    # same x 
    if knot[0] == knot_after[0]:
        dist = knot_after[1] - knot[1]
        new_y = knot[1] + dist - 1 if dist > 0 else knot[1] + dist + 1
        return [ knot[0], new_y ]

    # same y 
    elif knot[1] == knot_after[1]:
        dist = knot_after[0] - knot[0]
        new_x = knot[0] + dist - 1 if dist > 0 else knot[0] + dist + 1
        return [ new_x, knot[1] ] 
    
    else: # diagonal
        for x in (-1, 1):
            for y in (-1, 1):
                new_pos = [knot[0] + x, knot[1] + y]
                if are_touching(new_pos, knot_after):
                    return new_pos
    

def main():
    knots_pos = [ [0, 0] for _ in range(10) ] 
    visited_positions = set()

    with open('input.txt', 'r') as input_file:
        for line in input_file:
            fields = line.strip().split()
            motion, count = fields[0], int(fields[1])
            # print_knots(knots_pos)

            for i in range(count):
                knots_pos[0] = pos_after_motion[motion](knots_pos[0]) # update head
                for ind in range(1, len(knots_pos)):
                    knot = knots_pos[ind]
                    knot_after = knots_pos[ind - 1]
                    if not are_touching(knot, knot_after):
                        knots_pos[ind] = next_move(knot, knot_after)

                # check if tail position is in set 
                if tuple(knots_pos[-1]) not in visited_positions:
                        visited_positions.add(tuple(knots_pos[-1]))

    print(len(visited_positions))


if __name__ == '__main__':
    main()
