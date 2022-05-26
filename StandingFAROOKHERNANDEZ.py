# Activity 2: Standing Waves

# The import statements used in this program
from numpy import *
import matplotlib.pyplot as plt
from matplotlib import animation


# Define the function to return the sin function with variables
# wavenumber k, displacement x, angular_frequency and time t
def sineWaveZeroPhi(k, x, angular_frequency, t):
    answer = sin(k * x - angular_frequency * t)
    return answer


# print(sineWaveZeroPhi(1,2,3,4)) -> for testing

# set up the plot and subplots, for the graph/animation
fig = plt.figure()
subplot = plt.axes(xlim=(0, 10), xlabel=("x"), ylim=(-2, 2), ylabel=("y"))
line1, = subplot.plot([], [], lw=2)
line2, = subplot.plot([], [], lw=2)
line3, = subplot.plot([], [], lw=2)

# Create a list of plot lines
lines = [line1, line2, line3]


# initializer function so that the graph is cleared when the animation begins
def init():
    for item in lines:
        item.set_data([], [])
    return lines


# create the independent value list
x = linspace(0, 10, 1000)


# the function to pass into matplotlib animation
def animate(i):
    # setting up the first dependent value list
    y1 = []
    for item in x:
        y1.append(sineWaveZeroPhi(pi / 2, item, 2 * pi, 0.01 * i))

    # setting up the second dependent variable list
    y2 = []
    for item in x:
        y2.append(sineWaveZeroPhi(pi / 2, item, -1 * 2 * pi, 0.01 * i))

    # setting up the third dependent value list by adding the other two
    y3 = []
    for i in range(len(y1)):
        y3.append(y1[i] + y2[i])

    WaveFunctions = [[x, y1], [x, y2], [x, y3]]

    # using set data on each value in lines, using the x and y values above
    for item in lines:
        # item = line2
        for lists in WaveFunctions:
            # lists = [x, y1]
            item.set_data(lists[0], lists[1])

    return lines


# animating the graph
anim = animation.FuncAnimation(fig, animate, init_func=init, frames=200,
                               interval=20, blit=True)

# showing the animation
plt.show()
