
# def car_fleet(target, position, speed):
#         pair =  [[p,s] for p,s in zip(position,speed)]
#         stack = []
#         # iterujemy od tyłu i badamy poszczególne czasy z górą stosu
#         for p,s in sorted(pair)[::-1]:
#             stack.append((target - p) / s) # dodajemy prędkość do stosu
#             # jeżeli czas pod aktualnie najwyższym w stosie jest większy
#             # to znaczy że poprzedni był wolniejszy i trzeba zwolnić ze stosu aktualny czas
#             if len(stack) >= 2 and stack[-2] >= stack[-1]:
#                 stack.pop()
#
#         return len(stack)


if __name__ == '__main__':
    target = 10
    position = [6,8]
    speed = [3,2]
    # print(car_fleet(target, position, speed))
    data = {"A": [246, 231, 236,217,246], "B": [243,246,243,235,235], "C": [265, 260,265,253,291]}
    values = [item for sublist in data.values() for item in sublist]
    mean = sum(values)/len(values)
    SST = sum([(yi - mean)**2 for yi in values])
    print("SST: ", SST)
    means = [sum(vals)/len(vals) for vals in data.values()]
    print("Means: ", means)
    SSA = 5 * sum([(m - mean)**2 for m in means])
    print("SSA: ", SSA)
    SSE = 0
    for j in range(3):
        hsum = 0
        for i in range(5):
            hsum += (list(data.values())[j][i] - means[j])**2
        SSE += hsum
    print("SSE: ", SSE)