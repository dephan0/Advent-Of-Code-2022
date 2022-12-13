#!/usr/bin/env python3

# checks if two ranges overlap each other
def do_overlap(r1_start, r1_end, r2_start, r2_end) -> bool:
    if r1_end >= r2_start and r1_end <= r2_end: # if r1 overlaps r2
        return True
    if r2_end >= r1_start and r2_end <= r1_end: # if r2 overlaps r1
        return True
    return False

def main():
    count = 0
    with open('input.txt', 'r') as input_file:
        for line in input_file:
            ranges = line.split(',')

            elf1_start, elf1_end = [ int(num) for num in ranges[0].split('-') ]
            elf2_start, elf2_end = [ int(num) for num in ranges[1].split('-') ]

            if do_overlap(elf1_start, elf1_end, elf2_start, elf2_end):
                count += 1
    
    print(count)

if __name__ == '__main__':
    main()
