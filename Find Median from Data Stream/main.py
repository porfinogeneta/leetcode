class MedianFinder(object):
    """
        idea: będziemy mieli dwa kopce
        - maksymalny (1 połowa listy)
        - minimalny (2 połowa listy)
        - będziemy też śledzić ile mamy elementów w ogóle
    """

    def __init__(self):
        self.small = []  # kopiec maksymalny
        self.large = []  # kopiec minimalny (standardowy)

    def addNum(self, num):
        """
        :type num: int
        :rtype: None
        idea: pilnujemy żeby w kopcu small były mniejsze elementy niż w kopcu large,
        pilnujemy, żeby kopce różniły się co najwyżej jednym elementem
        O(logn) -> używamy operacji o złożoności logn
        """

        heapq.heappush(self.small, -num)

        # oba kopce istnieją i dodany przez nas element jest większy niż najmniejszy w large,
        # przenosimy zatem minimum ze small do large
        if self.small and self.large and self.large[0] < -self.small[0]:
            val = -heapq.heappop(self.small)
            heapq.heappush(self.large, val)

        # teraz jak różnica długości między kopcami jest większa niż 1
        if len(self.small) > len(self.large) + 1:
            val = -heapq.heappop(self.small)
            heapq.heappush(self.large, val)

        if len(self.large) > len(self.small) + 1:
            val = heapq.heappop(self.large)
            heapq.heappush(self.small, -val)

    def findMedian(self):
        """
        :rtype: float
        idea: jak w obu kopcach jest tyle samo elementów, to mamy parzystą liczbę elementów,
        wówczas bierzemy średnią, jak ta długość jest różna, to bierzemy medianę z dłuższego kopca
        O(1)
        """
        if len(self.small) > len(self.large):
            return -self.small[0]

        if len(self.large) > len(self.small):
            return self.large[0]

        if len(self.small) == len(self.large):
            return (-self.small[0] + self.large[0]) / 2.0

# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()