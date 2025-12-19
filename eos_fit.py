import numpy as np
import pandas as pd

# Birch Murnaghan Equation of State
def eos(V, a, b, c, d):
    return a + b*V**(-2/3) + c*V**(-4/3) + d*V**(-6/3)

# Read from csv data
df = pd.read_csv("eos.csv")

V = df["Volume (A^3/atom)"].values
E = df["Energy (eV/atom)"].values

# Fit Energy Vs Volume
from scipy.optimize import curve_fit
initial_guess = [-2.58, 1, 1, 1]
out = curve_fit(eos, V, E, p0=initial_guess)
params = out[0]
a = params[0]
b = params[1]
c = params[2]
d = params[3]
print(a, b, c, d)

# Curve for energy vs volume plotting
V_plot = np.linspace(min(V), max(V), 200)
E_plot = eos(V_plot, a, b, c, d)

# Find Equilibrium Volume
V_eqlbrm = V_plot[np.argmin(E_plot)]
print("Equilibrium Volume =", V_eqlbrm)

# Plot
import matplotlib.pyplot as plt
plt.scatter(V, E, label="DFT data")
plt.plot(V_plot, E_plot, label="EOS fit")
plt.xlabel("Volume (A^3/atom)")
plt.ylabel("Energy (eV/atom)")
plt.legend()
plt.show()
