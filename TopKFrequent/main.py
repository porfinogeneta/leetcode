def topKFrequent(self, nums, k):
    # trik to zrobienie bucketów, w których indeksy to
    # liczba wystąpień, a wartości, to listy z liczbami o danym wystąpieniu
    hashMap = {}
    for n in nums:
        hashMap[n] = 1 + hashMap.get(n, 0)

    counts = [[] for _ in range(len(nums))]
    for kk, v in hashMap.items():
        counts[v - 1].append(kk)

    res = []
    for i in range(len(counts) - 1, -1, -1):
        for elem in counts[i]:
            if k == 0: break
            k -= 1
            res.append(elem)

    return res