# two solutions, union find and dfs

# # dfs
# class Solution:
#     def countComponents(self, n: int, edges: List[List[int]]) -> int:
#         graph = {i : [] for i in range(n)}

#         for a,b in edges:
#             graph[a].append(b)
#             graph[b].append(a)
#         visited = set()
        
#         def dfs(v):
#             if v in visited:
#                 return
#             visited.add(v)
#             for n in graph[v]:
#                 dfs(n)
#             return

#         components = 0
#         for i in range(n):
#             if i not in visited:
#                 dfs(i)
#                 components += 1

#         return components


# union find