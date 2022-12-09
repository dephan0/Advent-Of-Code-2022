#!/usr/bin/env python3

def are_touching(pos1, pos2):
    if abs(pos1[0] - pos2[0]) <= 1 and abs(pos1[1] - pos2[1]) <= 1:
        return True 
    return False

def main():
    head_pos = [0, 0]
    tail_pos = [0, 0]
    visited_positions = set()
    with open('day9/input.txt', 'r') as input_file:
        for line in input_file:
            fields = line.strip().split()
            motion, count = fields[0], int(fields[1])

            if motion == 'U':
                for i in range(count):
                    head_pos[1] += 1
                    if not are_touching(head_pos, tail_pos):
                        tail_pos = [head_pos[0], head_pos[1] - 1]
                    if tuple(tail_pos) not in visited_positions:
                        visited_positions.add(tuple(tail_pos))

            elif motion == 'D':
                for i in range(count):
                    head_pos[1] -= 1
                    if not are_touching(head_pos, tail_pos):
                        tail_pos = [head_pos[0], head_pos[1] + 1]
                    if tuple(tail_pos) not in visited_positions:
                        visited_positions.add(tuple(tail_pos))

            elif motion == 'R':
                for i in range(count):
                    head_pos[0] += 1
                    if not are_touching(head_pos, tail_pos):
                        tail_pos = [head_pos[0] - 1, head_pos[1]]
                    if tuple(tail_pos) not in visited_positions:
                        visited_positions.add(tuple(tail_pos))

            elif motion == 'L':
                for i in range(count):
                    head_pos[0] -= 1
                    if not are_touching(head_pos, tail_pos):
                        tail_pos = [head_pos[0] + 1, head_pos[1]]
                    if tuple(tail_pos) not in visited_positions:
                        visited_positions.add(tuple(tail_pos))

    print(len(visited_positions))

if __name__ == '__main__':
    main()
