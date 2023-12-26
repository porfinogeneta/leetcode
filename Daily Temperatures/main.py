

def dailyTemperatures(temperatures):
    # stos wartości malejących
    res = [0] * len(temperatures)
    # stos na pary wartoci index,temeperatura
    stack = [(0, temperatures[0])]
    for i in range(1, len(temperatures)):
        # wyrzucamy ze stosu dopóki jest stos i element na górze jest mniejszy
        while stack and temperatures[i] > stack[-1][1]:
            popped_i = stack.pop()[0]
            # obliczamy różnicę między indeksami i dodajemy ją do wyniku
            res[popped_i] = i - popped_i
        # na końcu jeśli sprawdzana wartość była mniejsza od góry stosu, dodaję ją
        stack.append((i, temperatures[i]))
    return res


if __name__ == '__main__':
    temperatures = [73, 74, 75, 71, 69, 72, 76, 73]
    print(dailyTemperatures(temperatures))