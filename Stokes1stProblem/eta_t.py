import numpy as np
import matplotlib.pyplot as plt

v = 0.02

ts = np.array([0.001, 0.1, 0.2, 0.3, 0.5]) 

def eta(t):
    return 0.25 / np.sqrt(4 * v * t)

plt.plot(ts, eta(ts), marker='o', color='darkblue')
plt.xlabel("Time (t)")
plt.ylabel("eta")
plt.title("eta vs time at fixed y = 0.25")
plt.grid(True, linestyle='--', alpha=0.5)
plt.show()
