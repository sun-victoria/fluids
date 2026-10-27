import numpy as np
import matplotlib.pyplot as plt
import math

# Governing equation
# y = u * exp(-kx) * cos(kx-wt) {y>0}

#   exp(-kx) describes the decay of the amplitude as you increase y

##### Defining vars #####

u_inf = 0.5 # freestream velocity
w = 0.3 # frequency
v = 0.002 # fluid viscosity 
k = np.sqrt(w/(2*v)) # wave number? 

y = np.linspace(0, 0.5, 100)
x = np.linspace(-0.5, 0.5, 100)

T = 2 * np.pi / w
time_steps = np.linspace(0, T, 8, endpoint=False)
cmap = plt.get_cmap('viridis')

def u(y, t, k):
    return u_inf * np.exp(-k*y) * np.cos(k*y - w*t)

##### Graphing #####

u_graph = [0.1, 0.5, 0.75, 1]
nu_graph = [0.0001, 0.001, 0.01, 0.09]
w_graph = [0.12, 0.5, 0.7, 10]
k_graph = [10, 20, 30, 50]

fig, axes = plt.subplots(2, 2, figsize = (12, 10), sharey=True)
axes = axes.flatten()

for index, k_i in enumerate(k_graph):
    ax = axes[index]

    for i, t in enumerate(time_steps):
    
        color_fraction = i / (len(time_steps) - 1)
        col = cmap(color_fraction)

        ax.plot(u(y, t, k_i), y, label=f"t = {round(t, 2)} s", color = col)

    ax.set_xlabel('u (m/s)')
    ax.set_ylabel('y (m)')
    ax.set_title(f"Wave number= {k_i} 1/m")
    ax.set_ylim(bottom=0)
    ax.set_xlim(-1.5, 1.5)

    if index == 0:
        ax.legend()

plt.show()
    

