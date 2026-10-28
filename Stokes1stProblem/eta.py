import numpy as np
import matplotlib.pyplot as plt

y = np.linspace(0, 0.5, 10)
v = 0.02
t = [0.01, 0.25, 0.5, 0.75]


def eta(y,t):
    return y/np.sqrt(4*v*t)

cmap = plt.get_cmap('viridis')

for i, time in enumerate(t):
    color_fraction = i / (len(t) - 1)
    col = cmap(color_fraction)
    plt.plot(y, eta(y,time), color = col, label = f"t = {time} s")
    print(time)


plt.xlabel("y")
plt.ylabel("eta")
plt.legend()
plt.show()