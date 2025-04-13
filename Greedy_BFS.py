# Mohammad Zafari
# mhdzafari80@gmial.com

from math import inf
from queue import PriorityQueue

def greedy_bfs(start, goal, v, graph, hn):

    explored = set()
    frontier = PriorityQueue()
    frontier.put((hn[start], start))
    parent  = {}
    path = []
    while frontier.empty() == False:
        node = frontier.get()[1]
        if node == goal:
            print('\nanswer found with Greedy search')
            path.append(node)
            while parent[node]:
                path.append(parent[node])
                node = parent[node]
            path.append(start)
            return path[::-1]
      
        explored.add(node)
        for child in graph[node]:
            if child not in frontier.queue and child not in explored:
                frontier.put((hn[child], child))
                parent[child] = node

def printAnswer(dict, path):
    print('The path is:')
    for number in path[:-1]:
        print(dict[number], end = " --> ")
    print(dict[path[-1]])
    print("\n")



def addedge(x, y, x_to_y_cost):
    #x_to_y_cost is not used by Greedy bfs
    graph[x].append(y)


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
