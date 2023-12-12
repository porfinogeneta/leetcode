import numpy as np
import matplotlib.pyplot as plt

# Funkcja, którą chcemy interpolować
def f(x):
    return 2023 * (x**8) + 1977 * (x**7) - 1939 * (x**4) + 1410 * (x**2) - 966 * x + 1996

# Punkty interpolacyjne
points = [-2023, 1977, -1945, np.sin(1), 1989, -1939, 1791, 1945, np.pi]
values = [f(x) for x in points]

# Stopień wielomianu interpolacyjnego
degree = 8

# Wyznaczanie współczynników wielomianu interpolacyjnego
coefficients = np.polyfit(points, values, degree)

# Tworzenie wielomianu interpolacyjnego
interpolating_polynomial = np.poly1d(coefficients)

# Przykładowe punkty do narysowania wykresu
x_values = np.linspace(min(points), max(points), 1000)
y_values = interpolating_polynomial(x_values)

# Wykres
plt.scatter(points, values, label='Punkty interpolacyjne')
plt.plot(x_values, y_values, label='Wielomian interpolacyjny', color='red')
plt.title('Interpolacja wielomianowa')
plt.xlabel('x')
plt.ylabel('f(x)')
plt.legend()
plt.show()
