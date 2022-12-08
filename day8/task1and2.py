#!/usr/bin/env python3

# returns an n x n list of dictionaries of every tree eg. {top: True, bottom: False etc...}
def get_visibility(trees):
    rows = len(trees)
    columns = len(trees[0])
    visibility_dict = {'top' : False, 'bottom': False, 'left' : False, 'right' : False}
    visibility = [ [ visibility_dict.copy() for _ in range(columns) ] for _ in range(rows) ]

    # check on the left
    for i in range(rows):
        max = trees[i][0]
        visibility[i][0]['left'] = True
        for j in range(1, columns):
            if trees[i][j] > max:
                max = trees[i][j]
                visibility[i][j]['left'] = True
            else:
                visibility[i][j]['left'] = False

    # check on the right
    for i in range(rows):
        last_ind = columns - 1
        max = trees[i][last_ind]
        visibility[i][last_ind]['right'] = True
        for j in range(last_ind - 1, -1, -1):
            if trees[i][j] > max:
                max = trees[i][j]
                visibility[i][j]['right'] = True
            else:
                visibility[i][j]['right'] = False

    # check on the top
    for j in range(columns):
        max = trees[0][j]
        visibility[0][j]['top'] = True
        for i in range(1, rows):
            if trees[i][j] > max:
                max = trees[i][j]
                visibility[i][j]['top'] = True
            else:
                visibility[i][j]['top'] = False

    # check on the bottom
    for j in range(columns):
        last_ind = rows - 1
        max = trees[last_ind][j]
        visibility[last_ind][j]['bottom'] = True
        for i in range(last_ind - 1, -1, -1):
            if trees[i][j] > max:
                max = trees[i][j]
                visibility[i][j]['bottom'] = True
            else:
                visibility[i][j]['bottom'] = False
    
    return visibility


def count_visible(visibility_table):
    count = 0
    for row in visibility_table:
        for dict in row:
            if True in dict.values():
                count += 1
    return count


def calculate_scenic_score(trees, row_ind, col_ind):
    tree_height = trees[row_ind][col_ind]
    rows = len(trees)
    columns = len(trees[0])

    # up
    up_score = 0
    for i in range(row_ind - 1, -1, -1):
        up_score += 1
        if trees[i][col_ind] >= tree_height:
            break

    # down
    down_score = 0
    for i in range(row_ind + 1, rows):
        down_score += 1
        if trees[i][col_ind] >= tree_height:
            break

    # left
    left_score = 0
    for j in range(col_ind - 1, -1, -1):
        left_score += 1
        if trees[row_ind][j] >= tree_height:
            break

    # right
    right_score = 0
    for j in range(col_ind + 1, columns):
        right_score += 1
        if trees[row_ind][j] >= tree_height:
            break

    return up_score * down_score * left_score * right_score


def get_highest_score(trees):
    rows = len(trees)
    columns = len(trees[0])
    max = 0
    coords = (0,0)
    for i in range(rows):
        for j in range(columns):
            score = calculate_scenic_score(trees, i, j)
            if score > max:
                max = score
                coords = (i, j)
    return max, coords


def main():
    trees = []
    with open('testinput.txt', 'r') as input_file:
        for line in input_file:
            row = [ int(val) for val in line.strip() ]
            trees.append(row)

    # Task 1 
    visibility = get_visibility(trees)
    count = count_visible(visibility)
    print(count)
    
    # Task 2 (first element in tuple is the score, the second are the coordinates)
    highest_score = get_highest_score(trees)
    print(highest_score)
    

if __name__ == '__main__':
    main()
