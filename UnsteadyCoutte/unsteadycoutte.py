import numpy as np
import matplotlib.pyplot as plt

# Computational Fluid Dynamics Vol. 1 Hoffman & Chiang
# Ch.3 Parabolic Partial Differential Equations
# 3.3.1 Forward Time/Central Space Method (explicit scheme)

# Fluid at rest is bounded by two inifinite parallel plates (no edge effects)
# @ t = 0, the lower plate is suddenly accelerated in the x-direction

# (du / dt) = v * (d^2u / dy^2) where the kinematic viscosity is denoted by nu, v

v = 0.000217 # m^2 / s
h = 40/1000 # m
u0 = 40 # m /s 

dy = 0.001 # m
ny = int(h/dy + 1)

dt = 0.002 # s
nm = 541 # number of steps in time

## Define domain
U = np.zeros((ny, nm))
y = np.linspace(0, h, ny)

## Define initial conditions
U[:, 0] = 0

## Define boundary conditions
U[0, :] = 40
U[ny - 1, :] = 0

## Diffusion number, d (must be less than or equal to 1/2 for convergence?)
d = v * (dt) / (dy * dy)

## Solution
for n in range(nm - 1):
  U[1 : ny - 1, n + 1] = U[1 : ny - 1, n] + d * (
      U[2:ny, n] - 2 * U[1 : ny - 1, n] + U[0 : ny - 2, n]
  )

plt.figure(figsize=(5, 5))
time_steps_to_plot = [0, 50, 100, 150, 200, nm - 1]
for n in time_steps_to_plot:
  plt.plot(U[:, n], y * 1000, label=f't = {n*dt:.3f} s')

plt.xlabel('u (m/s)')
plt.ylabel('y (mm)')
plt.title('Unsteady Couette Flow')
plt.legend()
plt.grid(True)
plt.show()