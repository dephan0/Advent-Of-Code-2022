#!/usr/bin/env python3
import re

def print_crates(crates):
    max_len = max([ len(stack) for stack in crates ])
    for i in range(max_len):
        for j in range(len(crates)):
            if len(crates[j]) >= max_len - i:
                print(f'[{crates[j][max_len - i - 1]}] ', end='')
            else:
                print('    ', end='')
        print()
    print()


def main():
    with open('input.txt', 'r') as input_file:
        crates = [ [] for _ in range(9) ]

        for line_index in range(9):
            line = input_file.readline()
            stack_index = 0
            for i, chr in enumerate(line):
                if i % 4 == 1: # Letters are on indices 1,5,9,13...
                    if chr.isalpha():
                        crates[stack_index].append(chr)
                    stack_index += 1
        
        # reverse the order of stacks
        crates = [ list(reversed(stack)) for stack in crates ]
        print_crates(crates)
        
        # skip one line
        input_file.readline()

        # read the procedures
        steps = []
        while True:
            line = input_file.readline()
            if line == '':
                break

            step = [ int(num) for num in re.findall(r'\d+', line) ]
            steps.append(step)

        # execute the procedures
        for step in steps:
            num_crates = step[0]
            from_index = step[1] - 1
            to_index = step[2] - 1
            for _ in range(num_crates):
                popped = crates[from_index].pop()
                crates[to_index].append(popped)

            # if you want to see each step
            # print(f'move {num_crates} from {from_index} to {to_index}')
            # print_crates(crates)

        print_crates(crates)
        answer = ''.join([ stack[-1] for stack in crates ])
        print(f'answer : {answer}')


if __name__ == '__main__':
    main()
