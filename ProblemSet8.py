from numpy import *
import matplotlib.pyplot as plt

L = 2  # arbitrary value


def probability_wave_function_1(x: float, L: float) -> float:
    """Returns a value corresponding to the wavefunction at a particular
    point as given in the question (for the first energy level)"""
    value = sqrt(2 / L) * sin(pi * x / L)
    return value


def probability_wave_function_2(x: float, L: float) -> float:
    """Returns a value corresponding to the wavefunction at a particular
    point as given in the question (for the second energy level)"""
    value = sqrt(2 / L) * sin(2 * pi * x / L)
    return value


dx = 0.01
x_values = arange(0, L, dx)

y1 = []
y2 = []
for x in x_values:
    y1.append(probability_wave_function_1(x, L))
    y2.append(probability_wave_function_2(x, L))

y1_values = [y**2 for y in y1]
y2_values = [y**2 for y in y2]

fig = plt.figure()
# plt.style.use('seaborn')
# subplot1 = fig.add_subplot(331)
# subplot1.plot(x_values, y1_values)
# subplot1.grid()
# subplot1.set(xlabel='x (nm)', ylabel='P1(x)', title='Probability Distribution '
#                                                     'for Psi-1')
#
# subplot2 = fig.add_subplot(333)
# subplot2.plot(x_values, y2_values)
# subplot2.grid()
# subplot2.set(xlabel='x (nm)', ylabel='P2(x)', title='Probability Distribution '
#                                                     'for Psi-2')

y3 = [((a + b)/sqrt(2)) for a, b in zip(y1, y2)]
y3_values = [y**2 for y in y3]
# subplot3 = fig.add_subplot(338)
# subplot3.plot(x_values, y3_values)
# subplot3.grid()
# subplot3.set(xlabel='x (nm)', ylabel='P(x)', title='Probability Distribution '
#                                                    'for Psi')

plt.plot(x_values, y1_values, label='P1(x)')
plt.plot(x_values, y2_values, label='P2(x)')
plt.plot(x_values, y3_values, label='P(x)')
plt.xlim([0, L])
plt.ylim([0, L])
plt.xlabel('x (nm)')
plt.ylabel('P(x)')
plt.title('P(x) vs x')
plt.legend()
plt.grid()
plt.show()
