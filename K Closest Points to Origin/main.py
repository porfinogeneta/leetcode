def kClosest(self, points, k):
    """
    :type points: List[List[int]]
    :type k: int
    :rtype: List[List[int]]
    idea: robimy minheap po odległości i popujemy z niego k razy
    uwaga, nie potrzebujemy liczyć pierwiastka, bo jeśli odległość jest większa to pierwiastek z niej także
    5 < 8 -> sqrt(5) < sqrt(8)
    złożoność O(n + klogn) -> heapify + k razy pop
    """
    points_dist = [[x ** 2 + y ** 2, x, y] for x, y in points]

    heapq.heapify(points_dist)
    res = []

    # popujemy z naszego kopca k razy
    for i in range(k):
        dist, x, y = heapq.heappop(points_dist)
        res.append([x, y])

    return res