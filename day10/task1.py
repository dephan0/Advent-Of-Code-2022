#!/usr/bin/env python3

def main():
    cycle = 0
    X_reg = 1
    sum = 0

    with open('day10/input.txt', 'r') as input_file:
        for line in input_file:
            fields = line.strip().split()
            fields_count = len(fields)
            
            for _ in range(fields_count): # if noop, loop once, if addx, loop twice
                cycle += 1
                if (cycle - 20) % 40 == 0:
                    strength = cycle * X_reg
                    sum += strength
                    print(f'Cycle : {cycle}, register: {X_reg}, strength = {strength}')
            
            if fields_count == 2: # addx
                X_reg += int(fields[1])

    print(sum)
                

if __name__ == '__main__':
    main()
