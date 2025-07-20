def lastStoneWeight(self, stones):
    """
    :type stones: List[int]
    :rtype: int
    O(n) -> heapify
    O(nlogn) -> mamy 2x pop (logn) który potencjalnien będziemy robić n razy
    idea: symulujemy, to co nam kazali, dopóki mamy więcej niż 1 kamień
    """
    # liczby ujemne, bo chcemy zasymulować kopiec max
    stoneHeap = [-elem for elem in stones]
    heapq.heapify(stoneHeap)

    while len(stoneHeap) > 1:
        # bierzemy dwa największe elementy i je 'zderzamy'
        m1 = -heapq.heappop(stoneHeap)
        m2 = -heapq.heappop(stoneHeap)

        if m1 != m2:
            m1 = abs(m1 - m2)
            heapq.heappush(stoneHeap, -m1)

    if stoneHeap != []:
        return -stoneHeap[0]

    return 0
