import collections

# jak działa algorytm
# utrzymujemy kolejkę z dwoma zakończeniami, z lewej strony utrzymujemy największy
# dotychczas element, a z prawej kolejne potencjalnie największe elementy, które kolejno dodajemy
# jak element dodany z prawej jest większy od elementów dotychzas dodanych, usuwamy je, bo mamy
# nowy maksymalny w oknie
# element z lewej strony kolejki (element maksymalny) jest usuwany jak przekroczymy zakres okna
# dodajemy elementy do outputu jak mamy pewność że utworzyliśmy całe okno
def maxSlidingWindow(nums, k):
    output = []
    # kolejka w której przetrzymujemy maksymalne wartości w każdej iteracji,
    # dla każdego okna, uwaga w kolejce przetrzymujemy indeksy elementów maksymalnych
    dequeue = collections.deque()

    l,r = 0, 0

    while r < len(nums):
        # wyrzucamy z kolejki wszystkie elementy mniejsze od tego, który chcemy dodać
        while dequeue and nums[dequeue[-1]] < nums[r]:
            dequeue.pop()
        # dodajemy jak usunęliśmy wszystkie za małe wartości
        dequeue.append(r)

        # jak lewy jest poza zasięgiem indeksu, na którym jesteśmy, to wyrzucamy go z zakresu
        if dequeue[0] < l:
            dequeue.popleft()

        # zaczynamy od pointerów l,r = 0,0, więc dodajemy do outputu tylko jak
        # okno będzie co najmniej rozmiaru k
        if (r + 1) >= k:
            # dodajemy tylko jak element był największy w oknie (najbardziej lewy element jest maksymalny)
            output.append(nums[dequeue[0]])
            l += 1
        r += 1

    return output




if __name__ == '__main__':
    print(maxSlidingWindow([1,3,-1,-3,5,6,7], 3))