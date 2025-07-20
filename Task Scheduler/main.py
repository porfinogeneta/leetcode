def leastInterval(self, tasks, n):
    """
    :type tasks: List[str]
    :type n: int
    :rtype: int
    idea: skorzystamy z kopca maksymalnego i kolejki. skoro interesuje nas tylko minimalna liczba
    interwałów to policzymy sobie taski i wrzucimy je na kopiec maksymalny. poczynając od najbardziej popularnego taska
    będziemy go ściągać i umieszczać w kolejce w postaci pary [ile zostało takiego taska, na jakim timerze można go użyć],
    no i potem przechodzimy po kopcu i w razie czego dobieramy z kolejki element na kopiec, robimy to jednak,
    gdy będziemy mogli wykorzystać element (druga liczba pary z kolejki mówi nam o timerze, kiedy mozna wykorzystać)
    O(len(tasks) + len(taska) * n) -> może być tak że mamy same taki AAAAAAA i np n=10 (przejście po while)
    len(tasks), bo Counter
    """

    counted_dict = Counter(tasks)
    # kopiec maksymalny w python robimy przez ujemne wartości
    maxHeap = [-cnt for cnt in counted_dict.values()]
    heapq.heapify(maxHeap)

    q = deque()  # pary [-#elementów, kiedy można użyć]

    timer = 0

    while maxHeap or q:
        timer += 1
        if maxHeap:
            max_elem = 1 + heapq.heappop(maxHeap)  # na kopcu były ujemne wartości
            # chcemy dodawać na kolejkę tylko jak będzie co procesować
            if max_elem != 0:
                q.append([max_elem, timer + n])

        if q and q[0][1] == timer:
            heapq.heappush(maxHeap, q.popleft()[0])

    return timer


