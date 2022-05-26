# Activity 1: Beats

# import statements used in this program
from numpy import *
import matplotlib.pyplot as plt


# Function to return a sine wave given the amplitude a, angular_frequency,
# and time t
def sineWaveZero(a, angular_frequency, t):
    answer = a * sin((-1) * angular_frequency * t)
    return answer


# print(sineWaveZero(1,2,3)) -> for testing

# initializing variables for the first plot
dt = 0.1
t = arange(0, 100, dt)
amplitude = 0.05
frequency = 4

# set up the dependent values for the first plot
y1 = []
for time in t:
    y1.append(sineWaveZero(amplitude, frequency, time))

# initialize the plot, and the subplot for the first plot
fig = plt.figure()
plt.style.use('seaborn')
subplot1 = fig.add_subplot(221)
subplot1.plot(t, y1)

# initialize the dependent values for the second plot
y2 = []
frequency = 4.2
for time in t:
    y2.append(sineWaveZero(amplitude, frequency, time))

# add second subplot to our results
subplot2 = fig.add_subplot(222)
subplot2.plot(t, y2)

# initialize the dependant values for the third plot, by adding each value
# of the first and second lists
y3 = []
for i in range(len(y1)):
    y3.append(y1[i] + y2[i])

# add third subplot to our results
subplot3 = fig.add_subplot(223)
subplot3.plot(t, y3)

# show the plot
plt.show()
