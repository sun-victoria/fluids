import numpy as np
import matplotlib.pyplot as plt


mu = 1.5e-5 # kinematic viscosity
u_inf = 100
rho = 1.225 # density of air at sea level
nu = mu/rho

def shear(x):
    return 0.332*mu*u_inf*np.sqrt(u_inf/(nu*x))

length = np.linspace(0.01, 1, 100)

plt.plot(length, shear(length), label='Shear Stress', color ='purple')
plt.xlabel('Length')
plt.ylabel('Shear Stress')
plt.legend()
plt.show()
