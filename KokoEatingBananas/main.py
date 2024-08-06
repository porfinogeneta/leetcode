import math


def minEatingSpeed(piles, h):
    # robimy zakres 1 do max, w którym szukamy godzin
    l, r = 1, max(piles)
    res = r
    while l <= r:
        # szukamy dobrego k
        k = (l + r) // 2
        hours = 0
        # sumujemy godziny z danym k
        for pile in piles:
            hours += math.ceil(pile / k)
        # jak uda się zjeść wszystko z danym k, update res i zbadanie jeszcze mniejszego k
        if hours <= h:
            res = min(res, k)
            r = k - 1
        else:
            # nie udało się zjeść z danym k, przechodzimy do większych przedziałów
            l = k + 1
    return res

def minEatingSpeedV2(piles, h):
    """
        idea: wyszukiwać liczby między maksymalną możliwą i najmnieszą możliwą
        i sprawdzać, dla jakiej możemy dostać najbardziej korzystny wynik
    """
    left = min(piles)
    right = max(piles)
    res = float("inf")
    while left < right:
        mid = (left + right) // 2
        time = 0
        for b in piles:
            time += math.ceil(b / mid)
        if time <= h:
            res = min(res, mid)
        # możemy spróbować mniejszej liczby
        if time <= h:
            right = mid - 1
        else:
            left = mid + 1

    return res

if __name__ == '__main__':
    piles = [3, 6, 7, 11]
    h = 8
    # print(minEatingSpeed(piles, h))
    print(minEatingSpeedV2(piles, h))
