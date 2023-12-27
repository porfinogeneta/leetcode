
def car_fleet(target, position, speed):
        pair =  [[p,s] for p,s in zip(position,speed)]
        stack = []
        # iterujemy od tyłu i badamy poszczególne czasy z górą stosu
        for p,s in sorted(pair)[::-1]:
            stack.append((target - p) / s) # dodajemy prędkość do stosu
            # jeżeli czas pod aktualnie najwyższym w stosie jest większy
            # to znaczy że poprzedni był wolniejszy i trzeba zwolnić ze stosu aktualny czas
            if len(stack) >= 2 and stack[-2] >= stack[-1]:
                stack.pop()

        return len(stack)


if __name__ == '__main__':
    target = 10
    position = [6,8]
    speed = [3,2]
    print(car_fleet(target, position, speed))