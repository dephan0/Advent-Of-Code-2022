#!/usr/bin/env python3
import os

def main():
    elf_sum = 0
    max = 0
    with open('input.txt', 'r') as input_file:
        for line in input_file:
            if line == os.linesep:
                if elf_sum > max:
                    max = elf_sum
                elf_sum = 0
            else:
                elf_sum += int(line)
    
    print(max)


if __name__ == '__main__':
    main()
