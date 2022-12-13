#!/usr/bin/env python3
import os

def main():
    top3sums = []
    elf_sum = 0
    with open('input.txt', 'r') as input_file:
        for line in input_file:
            if line == os.linesep:
                top3sums.append(elf_sum)
                top3sums = sorted(top3sums, reverse=True)

                if len(top3sums) > 3:
                    top3sums.pop()

                elf_sum = 0
            else:
                elf_sum += int(line)
    
    print(sum(top3sums))


if __name__ == '__main__':
    main()
