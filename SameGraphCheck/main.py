
A = {0:[], 1: [3], 2:[4], 3:[0,1,4],4:[2,3]}
# B = {0: [2], 1: [2], 2:[0,1,3], 3:[2,4],4:[3]}
B = {0:[], 1: [3], 2:[4], 3:[4,1,0],4:[2,3]}

def checking_if_same(A, B):
    queue = []
    visited = [False] * len(A)
    # visited[0] = True
    # queue.append(0)

    for s in A.keys():
        # s = queue.pop(0)
        deg = 0 # zmienna której używam do przechowywania stopnia wierzchołka

        # standardowe sprawdzenie kolejnych wierzchołków
        for edge in A[s]:
            if not visited[edge]:
                visited[edge] = True
                queue.append(edge)
            deg += 1

        for edge in B[s]:
            # jeśli się okaże że próbujemy sprawdzać coś czego nie sprawdziliśmy w poprzednim
            # to musi to dany wierzchołek musi mieć inne połączenie
            if not visited[edge]:
                return False
            deg -= 1

        # jeżeli stopień wierzchołka jest różny w obu przypadkach
        if deg != 0:
            return False

    return True




if __name__ == '__main__':
    print(checking_if_same(A,B))