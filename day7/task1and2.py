#!/usr/bin/env python3

class File:
    def __init__(self, name, size) -> None:
        self.name = name
        self.size = size
    

class Directory:
    def __init__(self, name, parent) -> None:
        self.name = name
        self.parent = parent
        self.data = [] # files and subdirectories
        self.size = 0
    
    def __repr__(self):
        return f'{self.name}, size = {self.size}'

    # indent = how many tabs to use for indentation (leave at 0)
    def ls(self, recursive=False, indent_lvl=0):
        indentation = '  ' * indent_lvl

        for el in self.data:
            if type(el) == File:
                print(f'{indentation}- {el.name} (file, size={el.size})')
            elif type(el) == Directory:
                print(f'{indentation}- {el.name} (dir, size={el.size})')
                if recursive:
                    el.ls(True, indent_lvl + 1)

    def get_dir(self, dirname):
        for el in self.data:
            if type(el) == Directory:
                if el.name == dirname:
                    return el
        return None
        
    def contains_dir(self, dirname):
        for el in self.data:
            if type(el) == Directory:
                if el.name == dirname:
                    return True
        return False

    def contains_file(self, filename):
        for el in self.data:
            if type(el) == File:
                if el.name == filename:
                    return True
        return False

    # returns the size of the Directory and updates its self.size
    def calculate_size(self):
        sum = 0
        for el in self.data:
            if type(el) == File:
                sum += el.size
            if type(el) == Directory:
                sum += el.calculate_size()
        
        self.size = sum
        return sum


# TASK 1
output_sum = 0
def sum_dir_sizes(directory):
    global output_sum
    for el in directory.data:
        if type(el) == Directory:
            if el.size <= 100000:
                output_sum += el.size
            sum_dir_sizes(el)
                
# TASK 2
sufficient_dirs = []
def find_sufficient_dirs(directory, required_size):
    global sufficient_dirs
    for el in directory.data:
        if type(el) == Directory:
            if el.size >= required_size:
                sufficient_dirs.append(el)
            find_sufficient_dirs(el, required_size)


def main():
    root = Directory('/', None)
    cwd = root
    with open('input.txt', 'r') as input_file:
        input_file.readline() # skip first entrance to root /

        line = input_file.readline()
        while line != '':
            fields = line.strip().split(' ')

            if fields[0] == '$': # command
                # Handle cd <dir>
                if fields[1] == 'cd' and fields[2] != '..':
                    if not cwd.contains_dir(fields[2]):
                        new_dir = Directory(name=fields[2], parent=cwd)
                        cwd.data.append(new_dir)
                    else:
                        cwd = cwd.get_dir(fields[2])

                # Handle cd ..
                elif fields[1] == 'cd' and fields[2] == '..':
                    cwd = cwd.parent

                # Handle ls
                elif fields[1] == 'ls':
                    line = input_file.readline()
                    fields = line.strip().split(' ')
                    while fields[0] != '$' and line != '':
                        type = fields[0]

                        if type.isalpha(): # directory
                            new_dir = Directory(name=fields[1], parent=cwd)
                            if not cwd.contains_dir(new_dir.name):
                                cwd.data.append(new_dir)
                        else: # file
                            new_file = File(name=fields[1], size=int(fields[0]))
                            if not cwd.contains_file(new_file.name):
                                cwd.data.append(new_file)

                        line = input_file.readline()
                        fields = line.strip().split(' ')
                        
                    continue
            line = input_file.readline()
        
    total_size = root.calculate_size() # calulate root size and recursively 
                                       # update all the directories sizes
    # root.ls(recursive=True)

    # Task 1
    # Recurse through the directorytree to find the sum of directories
    # that are less than 100000 in size
    sum_dir_sizes(root)
    print(output_sum)

    # Task 2
    # Recurse through the directory tree to find the directories
    # that are more than or equal to required_to_free in size
    free_space = 70_000_000 - total_size
    required_to_free = 30_000_000 - free_space

    if root.size >= required_to_free:
        sufficient_dirs.append(root)
    find_sufficient_dirs(root, required_to_free)
    print(sorted(sufficient_dirs, key=lambda el : el.size)[0])


if __name__ == '__main__':
    main()
