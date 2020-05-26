#!/usr/local/bin/python3

import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit


def amdahl(ncpu, p):
    return 1/(1-p+p/ncpu)


def gustafson(ncpu, p):
    return ncpu-(1-p)*(ncpu-1)


data = np.loadtxt('weak_scaling.csv', delimiter=',')
ind = np.argsort(data, axis=0)
data = data[ind[:, 0], :]
ncpu = data[:, 0]
ta = np.zeros(len(ncpu))
tg = np.zeros(len(ncpu))

# Determine average computation time on 1 CPU
t1 = 0
c1 = 0
for x, y in data:
    if x == 1:
        t1 += y
        c1 += 1
    else:
        break
t1 /= c1

speedup = t1/data[:, 1]
plt.plot(ncpu, speedup, 'ok')

popt, pcov = curve_fit(amdahl, ncpu, speedup)

# Create optimized curve
for i, n in enumerate(ncpu):
    ta[i] = amdahl(n, popt)

legend = []
legend.append("measured")
legend.append("s = " '{:.2f}'.format(float(1-popt)))
print(legend)
print("Serial fraction =", 1-popt)
plt.plot(ncpu, ta, '--k')
plt.title("Weak Scaling")
plt.ylabel("Speed Up")
plt.xlabel("Number of CPUs")
plt.legend(legend)
plt.grid(True)
plt.show()
