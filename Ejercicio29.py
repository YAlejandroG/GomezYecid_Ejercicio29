import os
import numpy as np
import matplotlib.pyplot as plt

difusion = np.loadtxt("difusion.dat")

plt.figure(figsize=(8,4))

plt.subplot(1,2,1)

time = difusion[:,0]
Psi1 = difusion[:,6]

plt.plot(time,Psi1,c='g')
plt.grid()
plt.xlabel('Time (s)')
plt.ylabel('$\Psi$ ($m^2/s$)')
plt.title("DIFUSION, x = 0m")

plt.subplot(1,2,2)

x = difusion[101,:]
Psi2 = difusion[100,:]

plt.plot(x,Psi2,c='g')
plt.grid()
plt.xlabel('X (m)')
plt.ylabel('$\Psi$ ($m^2/s$)')
plt.title("DIFUSION, t = 1s")

plt.savefig("difusion.png")