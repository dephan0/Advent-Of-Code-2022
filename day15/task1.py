#!/usr/bin/env python3
import re

def get_distance(pos1, pos2):
    return abs(pos1[0] - pos2[0]) + abs(pos1[1] - pos2[1])

def impossible_in_row(y : int, pairs):
    impossible_pos = set() # positions where a beacon cant be

    for sensor, beacon in pairs:
        distance = get_distance(sensor, beacon)
        # check if the 'star' overlaps the row (from the top or bottom - the second if)
        if sensor[1] <= y and sensor[1] + distance >= y:
            offset = sensor[1] + distance - y
            start_x = sensor[0] - offset
            end_x = sensor[0] + offset
            for i in range(start_x, end_x + 1):
                impossible_pos.add((i, y))

        elif sensor[1] >= y and sensor[1] - distance <= y:
            offset = abs(sensor[1] - distance - y)
            start_x = sensor[0] - offset
            end_x = sensor[0] + offset
            for i in range(start_x, end_x + 1):
                impossible_pos.add((i, y))

        if beacon in impossible_pos:
            impossible_pos.remove(beacon)

    return impossible_pos

def print_out(pairs):
    sensors = [ pair[0] for pair in pairs ]
    beacons = [ pair[1] for pair in pairs ]

    for row in range(-2, 25):
        impossible_pos = impossible_in_row(row, pairs)
        print(f'{row} ', end='')
        for col in range(-2, 25):
            if (col, row) in sensors:
                print('S', end='')
            elif (col, row) in beacons:
                print('B', end='')
            elif (col, row) in impossible_pos:
                print('#', end='')
            else:
                print('.', end='')
        print()

# checks if position is covered by a pair (sensor and the nearest beacon)
def is_covered(pos, pair):
    sensor, beacon = pair
    return get_distance(pos, sensor) <= get_distance(sensor, beacon)

def within_bounds(pos, bounds):
    return (bounds[0] <= pos[0] <= bounds[1] and
            bounds[0] <= pos[1] <= bounds[1])

# returns positions surrounding the 'start' each pair forms
def get_surrounding_positions(pair):
    sensor, beacon = pair
    # positions = []
    distance = get_distance(sensor, beacon)

    start_pos = (sensor[0], sensor[1] - distance - 1)
    next_pos = start_pos
    yield next_pos

    for _ in range(distance + 1):
        next_pos = (next_pos[0] + 1, next_pos[1] + 1)
        yield next_pos

    for _ in range(distance + 1):
        next_pos = (next_pos[0] - 1, next_pos[1] + 1)
        yield next_pos

    for _ in range(distance + 1):
        next_pos = (next_pos[0] - 1, next_pos[1] - 1)
        yield next_pos

    for _ in range(distance):
        next_pos = (next_pos[0] + 1, next_pos[1] - 1)
        yield next_pos


def find_distress_beacon(pairs, search_range):
    positions = []
    for ind, pair1 in enumerate(pairs):
        print(ind)
        surrounding_pos = get_surrounding_positions(pair1)
        other_pairs = pairs.copy()
        other_pairs.remove(pair1)
        for pos in surrounding_pos:
            pos_covered = False
            for pair2 in other_pairs:
                if is_covered(pos, pair2):
                    pos_covered = True
                    break
            if not pos_covered and within_bounds(pos, search_range):
                print(pos)
                return pos


def main():
    pairs = [] # stores pairs of sensor pos and the nearest beacon pos
    with open('day15/input.txt', 'r') as input_file:
        for line in input_file:
            nums = [ int(match) for match in re.findall(r'-?\d+', line) ]
            sensor = (nums[0], nums[1])
            beacon = (nums[2], nums[3])
            pairs.append((sensor, beacon))
    
    # TASK 1
    positions = impossible_in_row(2_000_000, pairs)
    print(len(positions))
    # print_out(pairs)

    # TASK 2
    db = find_distress_beacon(pairs, (0, 4_000_000))
    print(db[0] * 4_000_000 + db[1])
    # find_distress_beacon(pairs, (0, 20))

if __name__ == '__main__':
    main()
