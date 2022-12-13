#!/usr/bin/env python3
from task1 import get_priority as t1_get_priority

def get_duplicate(elf1, elf2, elf3):
    # use a set for faster lookup ('in' utilizes a hash function for lookups)
    s1 = set(elf1)
    s2 = set(elf2)
    for item in elf3:
        if item in s1 and item in s2:
            return item

def main():
    sum = 0 
    with open('input.txt', 'r') as input_file:
        while True:
            lines3 = [ input_file.readline().strip() for _ in range(3) ]
            if lines3[2] == '':
                break

            duplicate = get_duplicate(*lines3)
            priority = t1_get_priority(duplicate) # Function from task1.py
            sum += priority

    print(sum)
if __name__ == '__main__':
    main()
