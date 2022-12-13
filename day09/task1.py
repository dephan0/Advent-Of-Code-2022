#!/usr/bin/env python3

pos_after_motion = {
    'U' : lambda pos: [pos[0], pos[1] + 1],
    'D' : lambda pos: [pos[0], pos[1] - 1],
    'R' : lambda pos: [pos[0] + 1, pos[1]],
    'L' : lambda pos: [pos[0] - 1, pos[1]],
}

def are_touching(pos1, pos2):
    if abs(pos1[0] - pos2[0]) <= 1 and abs(pos1[1] - pos2[1]) <= 1:
        return True 
    return False

def main():
    head_pos = [0, 0]
    tail_pos = [0, 0]
    visited_positions = set()
    with open('input.txt', 'r') as input_file:
        for line in input_file:
            fields = line.strip().split()
            motion, count = fields[0], int(fields[1])

            for i in range(count):
                last_pos = head_pos.copy()
                head_pos = pos_after_motion[motion](head_pos)
                if not are_touching(head_pos, tail_pos):
                    tail_pos = last_pos
                if tuple(tail_pos) not in visited_positions:
                    visited_positions.add(tuple(tail_pos))

    print(len(visited_positions))

if __name__ == '__main__':
    main()

