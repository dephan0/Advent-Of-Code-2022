#!/usr/bin/env python3

def get_priority(item):
    if ord(item) >= ord('a'):
        return ord(item) - ord('a') + 1
    else:
        return ord(item) - ord('A') + 27
    
def get_duplicate(comp1, comp2):
    # use a set for faster lookup ('in' utilizes a hash function for lookups)
    s1 = set(comp1)
    for item in comp2:
        if item in s1:
            return item

def main():
    sum = 0 
    with open('input.txt', 'r') as input_file:
        for line in input_file:
            rucksack = line.strip()
            compartment1 = rucksack[0 : len(rucksack) // 2]
            compartment2 = rucksack[len(rucksack) // 2 :]

            duplicate = get_duplicate(compartment1, compartment2)
            priority = get_priority(duplicate)
            sum += priority
    
    print(sum)

if __name__ == '__main__':
    main()
