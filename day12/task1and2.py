#!/usr/bin/env python3
from PriorityQueue import PriorityQueue

# reverse is used for task 2. (so that we can navigate from from the end in reverse motion)
# if reverse = True:
#   are_connected recognizes two squares as connected if the second one (neighbor)
#   is at most 1 shorter than the second 
# if reverse = False:
#   are_connected recognizes two squares as connected if the second one (neighbor)
#   is at most 1 taller than the second 
def get_edges(vertices, reverse=False):  
    get_neighbor_position = {
        "up" : lambda pos: (pos[0] - 1, pos[1]), # position 1 square above
        "down" : lambda pos: (pos[0] + 1, pos[1]),
        "right" : lambda pos: (pos[0], pos[1] + 1),
        "left" : lambda pos: (pos[0], pos[1] - 1),
    }
    vertices_positions = vertices.keys()
    edges = {pos : [] for pos in vertices_positions}

    if reverse:
        are_connected = lambda cur_pos, neighbor_pos: vertices[neighbor_pos] >= vertices[cur_pos] - 1
    else:
        are_connected = lambda cur_pos, neighbor_pos: vertices[neighbor_pos] <= vertices[cur_pos] + 1

    for current_pos in vertices_positions:
        for direction in get_neighbor_position.keys(): # check all 4 possible neighbors
            neighbor_pos = get_neighbor_position[direction](current_pos)
            if neighbor_pos in vertices_positions and are_connected(current_pos, neighbor_pos):
                edges[current_pos].append(neighbor_pos)

    return edges


class Graph:
    def __init__(self, vertices, edges) -> None:
        self.vertices = vertices
        self.edges = edges
    
    def dijkstra_list(self, start_pos):
        output = []
        pq = PriorityQueue()
        pq.put([0, None, start_pos])
        for position in self.vertices.keys():
            if position != start_pos:
                pq.put([float('inf'), None, position])
        
        while not pq.empty():
            min_v = pq.get()
            min_v_pos = min_v[2]
            output.append(min_v)
            
            for v in pq.data:
                v_pos = v[2]
                # check if the cost of min_v + 1 is smaller than current cost of v
                if  v_pos in self.edges[min_v_pos] and min_v[0] + 1 < v[0]:
                    v[0] = min_v[0] + 1 # update the cost
                    v[1] = min_v[2] # update the parent

        return output
    
    def find_pos_in_list(self, pos, list):
        for element in list:
            if element[2] == pos:
                return element

    def get_path(self, start_pos, end_pos):
        dijkstra_list = self.dijkstra_list(start_pos)
        path = []
        parent = end_pos

        while True:
            iter = self.find_pos_in_list(parent, dijkstra_list)
            path.append(iter[2])
            parent = iter[1]
            if parent == None:
                break
        return list(reversed(path))


def main():
    vertices = {}
    start_pos = None
    end_pos = None
    with open('input.txt', 'r') as input_file:
        lines = input_file.readlines()
        for i, line in enumerate(lines):
            for j, char in enumerate(line.strip()):
                pos = (i, j)
                match char:
                    case 'S':
                        char = 'a'
                        start_pos = pos
                    case 'E':
                        char = 'z'
                        end_pos = pos
                height = ord(char) - ord('a')
                vertices[pos] = height

    # TASK 1
    edges = get_edges(vertices)
    g = Graph(vertices, edges)
    dijkstra_list = g.dijkstra_list(start_pos)

    print(g.find_pos_in_list(end_pos, dijkstra_list)[0]) # display the cheapest cost to end_pos
    # print(g.get_path(start_pos, end_pos)) # display the path (or its length)

    # TASK 2
    edges2 = get_edges(vertices, reverse=True)
    g2 = Graph(vertices, edges2)
    dijkstra_list2 = g2.dijkstra_list(end_pos)

    min = float('inf')
    for element in dijkstra_list2:
        cost = element[0]
        pos = element[2]
        if vertices[pos] == 0:
            min = cost if cost < min else min 
    
    print(min)


if __name__ == '__main__':
    main()
