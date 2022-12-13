#!/usr/bin/env python3
import functools

# e.g. generate [1,2,3,[4]] from '[1,2,3,[4]]'
def list_from_string(string):
    stack = []
    current_num = ''

    for char in string:
        if char == '[':
            stack.append(char)
        elif char == ']':
            new_list = []
            if current_num != '':
                stack.append(int(current_num))
                current_num = ''
            popped = stack.pop() 
            while popped != '[':
                new_list.append(popped)
                popped = stack.pop()
            new_list = list(reversed(new_list))
            stack.append(new_list)
        elif char == ',':
            if current_num != '':
                stack.append(int(current_num))
                current_num = ''
        else:
            current_num += char

    return stack.pop()

# returns positive value if left > right, negative if left < right and 0 if left = right
def compare_elements(left, right):
    if type(left) == int and type(right) == int:
        return left - right

    if type(left) == list and type(right) == list:
        left_len = len(left)
        right_len = len(right)
        longer = right_len if  right_len >= left_len else left_len

        for i in range(longer):
            if i >= left_len:
                return -1
            elif i >= right_len:
                return 1
            comparison = compare_elements(left[i], right[i])
            if comparison != 0:
                return comparison
        return 0

    if type(left) != type(right):
        if type(left) == int:
            return compare_elements([left], right)
        else:
            return compare_elements(left, [right])


def main():
    packets = []
    with open('input.txt', 'r') as input_file:
        packets = [ list_from_string(line.strip()) 
                    for line in input_file.readlines()
                    if line.strip() != '']
    # TASK 1
    sum = 0
    ind = 1
    for packet, next_packet in  zip(packets[::2], packets[1::2]):
        if compare_elements(packet, next_packet) < 0:
            sum += ind
        ind += 1
    print(sum)

    # TASK 2
    packets.append([[2]])
    packets.append([[6]])

    # sort using the custom comparator 'compare_elements'
    packets.sort(key=functools.cmp_to_key(compare_elements))
    
    ind1 = packets.index([[2]]) + 1
    ind2 = packets.index([[6]]) + 1
    print(ind1 * ind2)


if __name__ == '__main__':
    main()
