

T = {7: [8,1], 3: [1],5:[4], 8:[2],1:[0],  4:[0], 2:[], 0:[]}
# T = {2: [3,4], 1:[3], 0:[4], 3:[5,6,7], 4:[6], 5:[],6:[],7:[]}

def dfs(graph,visited,start):
    # dno rekursji, odwiedzony element
    print(start)
    for node in graph[start]:
        if node not in visited:
            dfs(graph,visited,node)


def topological_recu(graph,visited,start,stack):
    visited.add(start)

    for node in graph[start]:
        if node not in visited:
            topological_recu(graph,visited,node,stack)

    stack.append(start)

def topological_sort(graph):
    stack = []
    visited = set()

    for node in graph:
        if node not in visited:
            topological_recu(graph,visited, node,stack)

    return stack[::-1]

if __name__ == '__main__':
    topological_sort(T)
    # print(dfs(T, {} , 7))
    # print(dfs(T, {} , 3))
    # print(dfs(T, {} , 4))


