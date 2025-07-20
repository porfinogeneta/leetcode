
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
def car_fleet(target, position, speed):

    pair = [(p, s) for p,s in zip(position, speed)]
    stack = []
    fleets_cnt = 0
    # będziemy przechodzić po samochodach posortowanych po pozycjach,
    # w sposób malejący, bo to samochody najbliżej mety potencjalnie wyznaczą
    # nam predkość floty
    for car in sorted(pair, key = lambda x: x[0], reverse=True):
        # obliczamy kiedy samochód dojedzie do końca
        arrival = (target - car[0]) / float(car[1])
        # jak czas dotarcia jest mniejszy od ostatniego najszybszego,
        # to nasze obecne auto musi zwolnić
        if stack and stack[-1][1] >= arrival:
            stack.append([car, stack[-1][1]])
        else:
            # jak to auto przyjedzie później to jest to początek
            # jakiejś floty
            fleets_cnt += 1
            stack.append([car, arrival])
    return fleets_cnt


if __name__ == '__main__':
    target = 10
    position = [6,8]
    speed = [3,2]
    print(car_fleet(target, position, speed))