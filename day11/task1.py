#!/usr/bin/env python3

class Monkey:
    def __init__(self, id, items, operation, test_number, if_true, if_false) -> None:
        self.id = id
        self.items = items
        self.operation = operation
        self.test_number = test_number
        self.if_true = if_true
        self.if_false = if_false
        self.times_inspected = 0
    
    def test(self, worry_level):
        return worry_level % self.test_number == 0

    def __repr__(self):
        return f'Monkey id: {self.id}, items: {self.items}, inspected: {self.times_inspected}'
    
def get_operation(tokens):
    last_token = tokens[-1]
    if last_token.isnumeric():
        if tokens[1] == '+':
            return lambda old: old + int(last_token)
        elif tokens[1] == '*':
            return lambda old: old * int(last_token)
    else:
        if tokens[1] == '+':
            return lambda old: old + old
        elif tokens[1] == '*':
            return lambda old: old * old

        
def main():
    monkeys = []
    with open('day11/input.txt', 'r') as input_file:
        for line in input_file:
            line = line.strip()

            if 'Monkey' in line:
                current_id = int(line.strip(':').split()[1])
            elif 'Starting' in line:
                items_string = line.split(': ')[1]
                current_items = [ int(token) for token in items_string.split(', ')]
            elif 'Operation' in line:
                op_string = line.split('= ')[1]
                op_tokens = op_string.split(' ')
                current_op = get_operation(op_tokens)
            elif 'Test' in line:
                current_test_num = int(line.split(' ')[-1])
            elif 'true' in line:    
                current_true = int(line.split()[-1])
            elif 'false' in line:    
                current_false = int(line.split()[-1])
                monkeys.append(Monkey(current_id, current_items, current_op,
                                    current_test_num, current_true, current_false))

    for round in range(20):
        for monkey in monkeys:
            while monkey.items:
                worry_level = monkey.items[0]
                monkey.items.remove(worry_level)
                worry_level = monkey.operation(worry_level)
                worry_level //= 3
                if monkey.test(worry_level):
                    next_monkey_ind = monkey.if_true
                else:
                    next_monkey_ind = monkey.if_false
                monkey.times_inspected += 1

                monkeys[next_monkey_ind].items.append(worry_level)
                
    sorted_monkeys = sorted(monkeys,
                            key=lambda monkey: monkey.times_inspected,
                            reverse=True)
    for monkey in sorted_monkeys: 
        print(monkey)
    print(f'level of monkey buisness : {sorted_monkeys[0].times_inspected * sorted_monkeys[1].times_inspected}')

if __name__ == '__main__':
    main()
