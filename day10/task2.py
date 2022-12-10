#!/usr/bin/env python3

def main():
    cycle = 0
    X_reg = 1 # sprite position
    crt_rows = [ '' for _ in range(6) ]

    with open('day10/input.txt', 'r') as input_file:
        for line in input_file:
            fields = line.strip().split()
            fields_count = len(fields)
            
            for _ in range(fields_count): # if noop, loop once, if addx, loop twice
                cycle += 1
                row = (cycle - 1) // 40
                pos_in_row = (cycle - 1) % 40

                if abs(X_reg - pos_in_row) <= 1: # crt position is inside of sprite 
                    crt_rows[row] += '#'
                else:
                    crt_rows[row] += '.'
            
            if fields_count == 2: # addx
                X_reg += int(fields[1])

    for row in crt_rows:
        print(row)
                

if __name__ == '__main__':
    main()
