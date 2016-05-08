#Lorenz, Edward N., and Kerry A. Emanuel. "Optimal sites for supplementary weather observations: Simulation with a small model." Journal of the Atmospheric Sciences 55.3 (1998): 399-414.

import numpy as np
import matplotlib.pyplot as plt #2d plot
import csv 

#define setting
dt = 0.005
step = 20000

#define parameters
const = 8.000
d=40

#define matrix
time = np.zeros(step)
xt = np.zeros((d, step))
xu = np.zeros(d)

f=open('data.csv','w')
writer = csv.writer(f,lineterminator='\n')

#define initial
xt[:,0] = 8.0
xt[20,0]=8.008
time[0]=0.0

# Forward time step
for i in range(step-1):
        time[i+1]=time[i]+dt
        xt[d-1,i+1]= xt[d-1,i]+dt*((xt[0,i]-xt[d-3,i])*xt[d-2,i]-xt[d-1,i]+const)  
        xt[0,i+1] = xt[0,i]+dt*((xt[1,i]-xt[d-2,i])*xt[d-1,i]-xt[0,i]+const)       
        xt[1,i+1] = xt[1,i]+dt*((xt[2,i]-xt[d-1,i])*xt[0,i]-xt[1,i]+const)  

        xu[d-1]=xt[d-1,i]
        xu[0]=xt[0,i]
        xu[1]=xt[1,i]
        
        for j in range(2,d-1):       
            xt[j,i+1]=xt[j,i]+dt*((xt[j+1,i]-xt[j-2,i])*xt[j-1,i]-xt[j,i]+const)
            xu[j]=xt[j,i]
        writer.writerow(xu)
f.close()
#2dplot
plt.figure(figsize=(18, 6), dpi=200)
plt.subplot(131)
plt.xlabel( 'Time' )  #x name
plt.ylabel( 'x1' )  #y name
plt.xlim(0.0, dt*step) #x limit
plt.ylim(-20.0, 20.0) #y limit
plt.plot(time[:],xt[1,:], color="black", linewidth=0.5)

plt.subplot(132)
plt.xlabel( 'Time' )  #x name
plt.ylabel( 'x2' )  #y name
plt.xlim(0.0, dt*step) #x limit
plt.ylim(-20.0, 20.0) #y limit
plt.plot(time[:],xt[2,:], color="black", linewidth=0.5)

plt.subplot(133)
plt.xlabel( 'Time' )  #x name
plt.ylabel( 'x3' )  #y name
plt.xlim(0.0, dt*step) #x limit
plt.ylim(-20.0, 20.0) #y limit
plt.plot(time[:],xt[3,:], color="black", linewidth=0.5)
plt.savefig("output1.png", dpi=200)
plt.show()

#counter
plt.figure(figsize=(18, 6), dpi=200)
plt.subplot(111)
x = np.arange(0,dt*(step),dt)
y = np.arange(d)
X, Y = np.meshgrid(x, y)
interval = np.arange(-20,20,1) #colorbar
plt.xlabel( 'Time' )  #x name
plt.ylabel( 'Number' )  #y name
plt.contourf(X,Y,xt,interval)
plt.colorbar()
plt.show()