import os
import numpy as np
import matplotlib.pyplot as plt

difusion = np.loadtxt("difusion.dat")

plt.figure(figsize=(8,4))

x = proyectil[:,0]
y = proyectil[:,1]

plt.plot(x,y,c='g')

plt.grid()

plt.xlabel('X(m)')
plt.ylabel('Y(m)')
plt.title("DIFUSION")

plt.savefig("difusion.png")