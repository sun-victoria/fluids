import numpy as np
import matplotlib.pyplot as plt
from scipy.special import erfc

U = 1.0          # Velocity of the plate (m/s)
nu = 0.01        # Kinematic viscosity (m^2/s)
y_max = 0.5      # Maximum spatial distance from the plate (m)
num_y = 500      # Spatial grid resolution

y = np.linspace(0, y_max, num_y)

time_snapshots = [0.1, 0.5, 1.0, 2.0, 5.0]

colors = plt.cm.viridis(np.linspace(0.2, 0.9, len(time_snapshots)))

fig, ax1 = plt.subplots(figsize=(9, 6))

ax_inset = fig.add_axes([0.60, 0.42, 0.35, 0.35])

for t, color in zip(time_snapshots, colors):
    # Analytical Similarity Solution: u/U = erfc( y / sqrt(4 * nu * t) )
    similarity_denominator = np.sqrt(4 * nu * t)
    eta_y = y / similarity_denominator
    u = U * erfc(eta_y)
    
    ax1.plot(u, y, label=f't = {t:.1f} s', color=color, linewidth=2.2)
    
    ax_inset.plot(u / U, eta_y, color=color, linestyle='--', linewidth=1.5)


ax1.set_title("Stokes' First Problem: Impulsively Started Flat Plate", fontsize=13, pad=15)
ax1.set_xlabel('Fluid Velocity $u(y, t)$ [m/s]', fontsize=11)
ax1.set_ylabel('Distance from Plate $y$ [m]', fontsize=11)
ax1.set_xlim(-0.05, U + 0.05)
ax1.set_ylim(0, y_max)
ax1.grid(True, linestyle=':', alpha=0.6)


ax1.axvline(x=U, color='red', linestyle=':', alpha=0.5, label='Plate Velocity')
ax1.legend(loc='lower left', frameon=True, shadow=False)

ax_inset.set_title(r'Similarity Profile Collapse', fontsize=10, pad=8)
ax_inset.set_xlabel(r'$u/U$', fontsize=9)
ax_inset.set_ylabel(r'$\eta = \frac{y}{\sqrt{4\nu t}}$', fontsize=10)
ax_inset.set_xlim(-0.05, 1.05)
ax_inset.set_ylim(0, 3.0)  # erfc drops below 0.0003 past eta = 2.5
ax_inset.grid(True, linestyle=':', alpha=0.4)


plt.tight_layout()
plt.show()
