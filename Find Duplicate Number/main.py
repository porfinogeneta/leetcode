def findDuplicate(nums):

    # traktujemy tablicę jako linked listę,
    # zauważamy, że początek cyklu to odpowiedź
    # na pytanie, która liczba się powtarza, bo
    # skoro mamy kilka (co najmniej dwa) nody wskazujące
    # na ten sam, to musi być to cykl, czyli znajdujemy go algorytmem
    # Floyda (chodzi o początek cyklu)

    # startujemy z oboma wskaźnikami,
    # szuakmy miejsca gdzie się złączą
    # można pokazać że odległość tego złączenia
    # od początku całej tablicy jest taka sama
    slow, fast = 0, 0
    while True:
        slow = nums[slow]
        fast = nums[nums[fast]]  # o dwa miejsca się przesuwamy
        if slow == fast:
            break

    # bierzemy drugi slow pointer i idziemy z nim,
    # dopóki nie spotka się z pierwszym, jak się spotkały
    # mamy początek cyklu i rozwiązanie
    slow2 = 0
    while slow2 != slow:
        slow2 = nums[slow2]
        slow = nums[slow]
    return slow  # zwracamy miejsce spotkania