
graph = {0: [1], 1: [0, 2], 2: [1], 3: [4], 4: [3, 5], 5: [4], 6: [7], 7: [6]}
# graph = {0: [1,4], 1: [0, 2, 4], 2: [1,3], 3: [2,4], 4: [0,1,3], 5: [6,7], 6: [5], 7: [5]} # graf niespójny
# graph = {0: [1,4], 1: [0, 2, 4], 2: [1,3,5], 3: [2,4], 4: [0,1,3], 5: [2, 6,7], 6: [5], 7: [5]}

def bipartiness_dfs(graph):
    visited = set()
    # 1 - czerowny 0 - neutralny -1 niebieski
    colors = [0]*len(graph)
    stack = []
    for node in graph.keys():
        if node not in visited:
            stack.append(node)
            colors[node] = 1
            while stack != []:
                current_node = stack.pop()
                if current_node not in visited:
                    print(current_node)
                    visited.add(current_node)
                    stack.extend(graph[current_node])
                    for neighbor in graph[current_node]:
                        if neighbor not in visited:
                            colors[neighbor] = -1 * colors[current_node]
                        else:
                            if colors[neighbor] == colors[current_node]:
                                return False
    return True

if __name__ == '__main__':
    print(bipartiness_dfs(graph))