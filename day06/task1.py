#!/usr/bin/env python3

# finds start-of-packet marker
def find_marker(buffer):
    for i in range(0, len(buffer) - 4):
        frame = buffer[i : i + 4]
        if len(set(frame)) == len(frame):
            return i + len(frame) 
    return -1

def main():
    with open('input.txt', 'r') as input_file:
        buffer = input_file.readline().strip()
        print(find_marker(buffer))

if __name__ == '__main__':
    main()
