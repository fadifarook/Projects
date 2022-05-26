from numpy import *
import matplotlib.pyplot as plt

L = 1  # given
a = 1.1  # given
n = 0.1028


def sin_function(A: int, a: float, L: int, x: float):
    """Returns the sin function for x values less than L"""
    value = A * sin((pi * x) / (a * L))
    return value


def exp_function(A: int, a: float, L: int, x: float, n: float):
    """Returns the exponential function for x values less than L"""
    exponent = -(x - L) / n
    value = A * sin(pi / a) * power(e, exponent)
    return value


dx = 0.01
x_values = arange(0, L + L/2, dx)  # till 1.5 nm
y_values = []
for x in x_values:
    if x <= L:
        y_values.append(sin_function(1, a, L, x))
    else:
        y_values.append(exp_function(1, a, L, x, n))

plt.plot(x_values, y_values)
plt.axvline(x=L, color='black')
plt.xlim([0, L+L/2])
plt.ylim([0, L+L/2])
plt.xlabel('x (nm)')
plt.ylabel('Psi(x)')
plt.title('Psi(x) vs x')

# plt.style.use('seaborn')
plt.grid()
plt.show()


print(sin_function(1, a, L, L))
print(exp_function(1, a, L, L, n))
