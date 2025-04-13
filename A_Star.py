# Mohammad Zafari
# mhdzafari80@gmial.com

from math import inf
from pickle import FALSE
from heapdict import heapdict

ans_path = []
def greedy_bfs(start, goal, v, graph, hn):

    gn = [inf for x in range(v)]
    explored = set()
    frontier = heapdict()
    gn[start] = 0
    frontier[start] = hn[start] + gn[start]
    # print(frontier[start])
    parent  = {}
    path = []
    while frontier.__len__ != 0:
        # print(frontier.queue)
        (node, fn_node) = frontier.popitem()
        # print(node)
        # print(fn_node)
        if node == goal:
            print('\nanswer found with A* search')
            path.append(node)
            # print(parent[node])
            while parent[node]:
                path.append(parent[node])
                node = parent[node]
            path.append(start)
            return path[::-1]

        explored.add(node)
        for (child, edge_w) in graph[node]:
            child_temp_gn= gn[node] + edge_w

            if child not in frontier or child not in explored:
                gn[child] = gn[node] + edge_w    
                frontier[child] = hn[child] + gn[child]
                parent[child] = node
            elif child in frontier and child not in explored:
                if child_temp_gn < gn[child]:
                    frontier[child] = child_temp_gn + hn[child]

def printAnswer(dict, path):
    # print('The path is:')
    for number in path[:-1]:
        print(dict[number], end = " ---> ",)
    print(dict[path[-1]])
    print("\n")

def addedge(x, y, x_to_y_cost):
    graph[x].append((y, x_to_y_cost))


#example
if __name__ == "__main__":
    v = 5
    graph = [[] for i in range(v)] 
    hn = [8, 6, 3, 2, 0]

    dict_v = {
        0 : 'A',
        1 : 'B',
        2 : 'C',
        3 : 'D',
        4 : 'E'
        }
    addedge(0, 1, 3)
    addedge(0, 3, 2)
    addedge(1, 0, 1)
    addedge(1, 2, 2)
    addedge(1, 3, 3)
    addedge(2, 2, 4)
    addedge(3, 0, 1)
    addedge(3, 2, 1)
    addedge(3, 4, 4)

    s = 0
    g = 4
    answer_in_number = greedy_bfs(s, g, v, graph, hn)
    printAnswer(dict_v, answer_in_number)
    # ATTENTION
    # Depending on the turn of popping from frontier, we arrive at two answers, both of which are correct.
    # 1: A ---> D ---> E
    # 2: A ---> D ---> C ---> E
