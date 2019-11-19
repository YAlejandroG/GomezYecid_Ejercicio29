import os
import numpy as np
import matplotlib.pyplot as plt

difusion = np.loadtxt("difusion.dat")

plt.figure(figsize=(15,4))

plt.subplot(1,2,1)

time = difusion[:,0]
time = np.delete(time,-1)
Psi1 = difusion[:,16]
Psi1 = np.delete(Psi1,-1)

plt.plot(time,Psi1,c='g')
plt.grid()
plt.xlabel('Time (s)')
plt.ylabel('$\Psi$ ($m^2/s$)')
plt.title("DIFUSION, x = 0m")

plt.subplot(1,2,2)

x = difusion[1001,:]
x = np.delete(x,0)
Psi2 = difusion[1000,:]
Psi2 = np.delete(Psi2,0)

plt.plot(x,Psi2,c='g')
plt.grid()
plt.xlabel('X (m)')
plt.ylabel('$\Psi$ ($m^2/s$)')
plt.title("DIFUSION, t = 1s")

plt.savefig("difusion.png")