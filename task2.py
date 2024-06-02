import numpy as np
import scipy.integrate as spi

def monte_carlo_integral(f, a, b, n=10000):
    x = np.random.uniform(a, b, n)
    y = np.random.uniform(0, f(b), n)
    below_curve = np.where(y < f(x), 1, 0)
    integral = (b - a) * (f(b) - 0) * np.mean(below_curve)
    return integral

def f(x):
    return x ** 3

# Визначте межі інтегрування, наприклад, від 0 до 1
a = 0  # нижня межа
b = 2  # верхня межа

# Обчислення інтеграла
result, error = spi.quad(f, a, b)

print("Інтеграл використовуючи quad: ", result)

integral = monte_carlo_integral(f, a, b)
print(f"Інтеграл використовуючи метод Монте-Карло: {integral}")
