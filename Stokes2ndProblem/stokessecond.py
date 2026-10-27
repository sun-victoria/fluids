import numpy as np
import matplotlib.pyplot as plt
import math

# Governing equation
# y = u * exp(-kx) * cos(kx-wt) {y>0}

#   exp(-kx) describes the decay of the amplitude as you increase y

u_inf = 0.5 # freestream velocity
w = 0.3 # frequency
v = 0.002 # fluid viscosity 
k = np.sqrt(w/(2*v)) # wave number? 

y = np.linspace(0, 0.8, 100)
x = np.linspace(-0.5, 0.5, 100)

T = 2 * np.pi / w
time_steps = np.linspace(0, T, 6, endpoint=False)
cmap = plt.get_cmap('Blues')


def u(y, t):
    return u_inf * np.exp(-k*y) * np.cos(k*y - w*t)

for i, t in enumerate(time_steps):
    color_fraction = i / (len(time_steps) - 1)
    col = cmap(color_fraction)

    plt.plot(u(y,t), y, label=f"t = {round(t, 2)} s", color = col)
    
plt.xlabel('x (m)')
plt.ylabel('y (m)')
plt.title('u(y)')
plt.ylim(bottom=0)
plt.legend()
plt.show()

