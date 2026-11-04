import numpy as np
import matplotlib.pyplot as plt

R = 150000 # representative Reynolds number
u_inf = 100
nu = 1.5e-5 # kinematic viscosity


def d1(x):
    r2 = u_inf*x/nu
    return 1.72*x/np.sqrt(R)

def d1_local(x):
    r2 = u_inf*x/nu
    return 1.72*x/np.sqrt(r2)


def d2(x):
    r2 = u_inf*x/nu
    return 0.664*x/np.sqrt(R)

def d2_local(x):
    r2 = u_inf*x/nu
    return 0.664*x/np.sqrt(r2)

def d99(x):
    r2 = u_inf*x/nu
    return 5.0*x/np.sqrt(R)

def d99_local(x):
    r2 = u_inf*x/nu
    return 5.0*x/np.sqrt(r2)

char_length = np.linspace(0.01, 1, 100)

plt.plot(char_length, d1(char_length), label='d1', color ='blue')
plt.plot(char_length, d2(char_length), label='d2', color ='green')
plt.plot(char_length, d99(char_length), label='d99', color ='red')

plt.plot(char_length, d1_local(char_length), label='d1_local', color = 'blue', linestyle='dashed')
plt.plot(char_length, d2_local(char_length), label='d2_local', color = 'green', linestyle='dashed')
plt.plot(char_length, d99_local(char_length), label='d99_local', color = 'red', linestyle='dashed')

plt.xlabel('Characteristic Length')
plt.ylabel('Boundary Layer Thickness')
plt.legend()
plt.show()