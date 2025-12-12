class Solution(object):
    def canFinish(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """
        graph = {i: [] for i in range(numCourses)}
        for t,s in prerequisites:
            # build an edge going from s to t
            graph[s].append(t)

        # find a cycle in a graph,
        visited = set()
        
        # false when schedulling is impossible
        def dfs(v):
            if v in visited:
                return False
            if graph[v] == []:
                return True
            visited.add(v)
            for n in graph[v]:
                if not dfs(n): return False
            # we visited all neighbours
            # so vertex was visited and doesn't contain any more neighbours to visit
            # we remove it from visited as it can be used by some other path
            visited.remove(v)
            graph[v] = []
            return True

        for k in graph:
            if not dfs(k):
                return False

        
        return True
