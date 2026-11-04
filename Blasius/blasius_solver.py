import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp
from scipy.optimize import root_scalar

# f''' + 0.5ff'' = 0
# f(0) = 0, f'(0) = 0, f'(inf) = 1 (set n to a large number for inf)

def blasius_ode(eta, y):
    f, fp, fpp = y
    fppp = -0.5 * f * fpp
    return [fp, fpp, fppp]

eta_max = 10
eta = np.linspace(0, eta_max, 100)

def blasius_shooting(s):
    y = [0, 0, s]
    sol = solve_ivp(
        blasius_ode, 
        [0, eta_max], 
        y, 
        t_eval=eta, 
        rtol=1e-9,
        atol=1e-11
    )
    return sol.y[1, -1] - 1

result = root_scalar(
    blasius_shooting,
    bracket=[0.3, 0.4],
    method='brentq',
    xtol=1e-12
)

s = result.root
y0 = [0, 0, s]

sol = solve_ivp(
    blasius_ode,
    [0, eta_max],
    y0,
    t_eval=eta,
    rtol=1e-9,
    atol=1e-11
)

f = sol.y[0]
fp = sol.y[1]
fpp = sol.y[2]


# Plot results
plt.figure(figsize=(8, 5))

plt.plot(eta, fp, label="f'(eta)")
plt.plot(eta, fpp, label="f''(eta)")
plt.plot(eta, f, label="f(eta)")

plt.xlabel("Similarity variable, eta")
plt.ylabel("Blasius functions")
plt.title("Blasius Boundary Layer Solution")
plt.grid()
plt.legend()
plt.show()



