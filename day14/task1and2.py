#!/usr/bin/env python3
from itertools import pairwise

class Cave:
    def __init__(self, floor=False) -> None:
        pass
        self.data = {}
        self.floor = floor
        self.floor_y = 0

    def use_floor(self):
        self.floor = not self.floor
        self.floor_y = self.find_floor_height()
    
    def find_floor_height(self):
        max = 0
        for pos in self.data.keys():
            max = pos[1] if pos[1] > max else max
        return max + 2

    def generate_rocks(self, coords):
        for current, next in pairwise(coords):
            if current[0] == next[0]:
                if current[1] > next[1]:
                    rock_range = range(current[1], next[1] - 1, -1)
                else:
                    rock_range = range(current[1], next[1] + 1, 1)
                for j in rock_range:
                    self.data[(current[0], j)] = '#' # rock
            elif current[1] == next[1]:
                if current[0] > next[0]:
                    rock_range = range(current[0], next[0] - 1, -1)
                else:
                    rock_range = range(current[0], next[0] + 1, 1)
                for i in rock_range:
                    self.data[(i, current[1])] = '#' # rock
    
    def is_blocked(self, pos):
        if self.floor:
            if pos[1] == self.floor_y:
                return True
        
        item = self.data.get(pos, None)
        if item == '#' or item == 'o':
            return True
        return False
    
    def is_at_top(self, pos):
        return pos == [500, 0]
    
    def is_void_below(self, pos):
        for test_pos in self.data.keys():
            if pos[0] == test_pos[0] and test_pos[1] > pos[1]:
                return False
        return True

    def drop_sand(self):
        sand_pos = [500, 0]
        if self.floor:
            end_condition = self.is_at_top
        else:
            end_condition = self.is_void_below
        
        while True:
            below = (sand_pos[0], sand_pos[1] + 1)
            below_right = (sand_pos[0] + 1, sand_pos[1] + 1)
            below_left = (sand_pos[0] - 1, sand_pos[1] + 1)

            if not self.is_blocked(below):
                sand_pos = list(below)
            elif not self.is_blocked(below_left):
                sand_pos = list(below_left)
            elif not self.is_blocked(below_right):
                sand_pos = list(below_right)
            elif not end_condition(sand_pos):
                self.data[tuple(sand_pos)] = 'o'
                return sand_pos

            if end_condition(sand_pos):
                break
            
        return 'finished'
    
    def clear_all_sand(self):
        for pos in list(self.data.keys()):
            if self.data[pos] == 'o':
                del self.data[pos]
    
    def __repr__(self):
        output = ''
        for y in range(0, 14):
            for x in range(485, 515):
                if y == self.floor_y:
                    output += '#'
                    continue
                item = self.data.get((x, y), None)
                if item == None:
                    output += '.'
                else:
                    output += item
            output += '\n'
        return output


def main():
    cave = Cave()
    with open('day14/input.txt', 'r') as input_file:
        for line in input_file:
            pairs = [token.strip() for token in line.strip().split('->')]
            coords = []
            for pair in pairs:
                pair = pair.split(',')
                coords.append( (int(pair[0]), int(pair[1])) )
            cave.generate_rocks(coords)

    # TASK 1
    units = 1
    while True:
        # print(cave)
        if cave.drop_sand() == 'finished':
            break
        units += 1
    print(units - 1)

    # TASK 2
    units = 1
    cave.clear_all_sand()
    cave.use_floor()
    while True:
        # print(cave)
        if cave.drop_sand() == 'finished':
            break
        units += 1
    print(units)

if __name__ == '__main__':
    main()
