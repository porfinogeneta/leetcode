import heapq
def findKthLargest(nums, k):
    """
        :type nums: List[int]
        :type k: int
        :rtype: int
        idea1: kopiec maksymalny, wyrzucamy elementy k razy
        O(n + klogn) k razy wyrzucamy
        idea2: quick select, sorting z przechodzeniem do odpowiedniej połowy
        theta(n)
    """

    heap = [-n for n in nums]

    heapq.heapify(heap)

    while k > 1:
        heapq.heappop(heap)
        k -= 1

    return -heapq.heappop(heap)

    # przekraczamy czas, bo w najgorszym przypadku gorzej niż O(n^2)
    # k = len(nums) - k
    #
    # def partition(l, r):
    #
    #     pvt_idx = random.randint(l, r)
    #     nums[pvt_idx], nums[r] = nums[r], nums[pvt_idx]
    #
    #     pivot, p = nums[r], l
    #
    #     # robimy partitioning
    #     for i in range(l, r):
    #         if nums[i] <= pivot:
    #             nums[p], nums[i] = nums[i], nums[p]
    #             p += 1
    #
    #     # zamieniamy pivot z granicą podziału
    #     nums[p], nums[r] = nums[r], nums[p]
    #
    #     if p < k:
    #         # szukamy w prawej połowie
    #         return partition(p + 1, r)
    #     elif p > k:
    #         # szukamy w lewej połowie
    #         return partition(l, p - 1)
    #     else:
    #         return nums[p]
    #
    # return partition(0, len(nums) - 1)

if __name__ == '__main__':
   print(findKthLargest([3, 2, 1, 5, 6, 4], 2))