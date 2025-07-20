class KthLargest(object):

    def __init__(self, k, nums):
        """
        :type k: int
        :type nums: List[int]
        idea: robimy kopiec minimalny o wielkości k, przetrzymujemy w nim k największych elementów,
        jak kopiec będzie za duży pozbywamy się najmniejszych elementów, trzymając kopiec minimalny
        o wielkości k minimum zawsze będzie k-tym największym elementem
        O(n) tworzenie kopca + usunięcie za małych elementów
        O(nlogn) -> potencjalnie musimy zrobić pop n razy, każdy pop logn
        """
        self.minHeap = nums
        self.k = k

        heapq.heapify(self.minHeap)
        while len(self.minHeap) > k:
            heapq.heappop(self.minHeap)

    def add(self, val):
        """
        :type val: int
        :rtype: int
        idea: dodajemy elemennt do kopca, jak mamy za dużo wartości w kopcu,
        usuwamy minimalne dopóki wielkość kopca nie będzie k
        O(logn) dodanie do kopca
        """
        heapq.heappush(self.minHeap, val)
        if len(self.minHeap) > self.k:
            heapq.heappop(self.minHeap)
        return self.minHeap[0]


