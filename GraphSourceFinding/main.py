
# x to kolejne wiersze, zewnętrzne indeksowanie
# y to kolejne elementy wierszy, wewnętrzne indeksowanie
def isHavingSource(D):
    x,y = 0,0
    while x != len(D) and y != len(D):
        # jesteśmy na przekątnej, 0 to prawidłowy element, przesuwam się w prawo
        if x == y and D[x][y] == 0:
            y += 1
        # 1 na przekątnej to nieprawidłowy element (pętla do siebie nie może być w źródle)
        elif x == y and D[x][y] == 1:
            x += 1
        # 0 na innych pozycjach to nieprawidłowy element
        elif D[x][y] == 0:
            x += 1
        # 1 jest ok nie na przekątnej
        elif D[x][y] == 1:
            y += 1
    # doszliśmny do końca macierzy
    if y == len(D):
        # na wszelki wypadek zmiejszamy x, żeby nie było out of range
        if x == len(D):
            x -= 1
        # badamy kolumnę i wiersz
        for i in range(0,len(D)):
            # kolumna, mają być same 0
            if D[i][x] != 0:
                return False
            # wiersz, pamiętamy że na przekątnej musi być 0, mają być same 1
            if D[x][i] != 1:
                if i != x:
                    return False
    elif x == len(D):
        return False
    return True





if __name__ == '__main__':
    D = [[0,0,0,0,0], [0,0,1,0,0], [1,1,0,0,0], [1,1,1,0,1], [0,0,1,0,0]]
    print(isHavingSource(D))