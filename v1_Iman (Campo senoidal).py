import numpy as np
from matplotlib import pyplot as plt

n = 1  # Number of particles

m = 1  # Mass in kg
q = -1  # Charge in Coulombs
L = 1  # Length in meters

# Initial positions
x0 = np.random.uniform(-L/2, L/2, n)
y0 = np.random.uniform(-L/2, L/2, n)
z0 = np.zeros(n)  # Assuming starting at z = 0

# Initialize velocities
vx = np.random.rand(n)*2  # Random initial velocities
vy = np.random.rand(n)*2
vz = np.random.rand(n)*2

B = 30  # Magnetic field strength in Gauss (30 G = 3e-2 T)

dt = 1e-3  # Time step in seconds
tf = 100  # Final time

# Lists to store positions for plotting
pxplot = [[] for _ in range(n)]
pyplot = [[] for _ in range(n)]
pzplot = [[] for _ in range(n)]

# Initial positions stored for plotting
for i in range(n):
    pxplot[i].append(x0[i])
    pyplot[i].append(y0[i])
    pzplot[i].append(z0[i])

t = 0

while t < tf:
    for i in range(n):
        
        # Magnetic field components based on position
        Bx = x0[i] * B * np.sin(np.pi * np.sqrt(x0[i]**2 + y0[i]**2) / L)
        By = y0[i] * B * np.sin(np.pi * np.sqrt(x0[i]**2 + y0[i]**2) / L)
        Bz = B * np.cos(np.pi * np.sqrt(x0[i]**2 + y0[i]**2) / L)

        # Update velocities based on Lorentz force
        vx[i] += (dt / m) * (q * (vy[i] * Bz - vz[i] * By))
        vy[i] += (dt / m) * (q * (vz[i] * Bx - vx[i] * Bz))
        vz[i] += (dt / m) * (q * (vx[i] * By - vy[i] * Bx))

#        vx[i], vy[i], vz[i] = vx[i] + (dt / m) * (q * (vy[i] * Bz - vz[i] * By)), vy[i] + (dt / m) * (q * (vz[i] * Bx - vx[i] * Bz)), vz[i] + (dt / m) * (q * (vx[i] * By - vy[i] * Bx))

        # Update positions
        x0[i] += vx[i] * dt
        y0[i] += vy[i] * dt
        z0[i] += vz[i] * dt

        if z0[i] < 0.0 or x0[i]**2 + y0[i]**2 > L**2:
            continue

        # Store positions for plotting
        pxplot[i].append(x0[i])
        pyplot[i].append(y0[i])
        pzplot[i].append(z0[i])
        
        
    t += dt

#Debug
print(pxplot[0][0], pyplot[0][0], pzplot[0][0])
print(pxplot[0][-1], pyplot[0][-1], pzplot[0][-1])


# Linea central para referencia
u = np.zeros(10)
v = np.zeros(10)
w = np.linspace(0, L, 10)

# Círculo de radio L para referencia
theta = np.linspace(0, 2*np.pi, 20)
uc = L*np.cos(theta)
vc = L*np.sin(theta)
wc = 0*theta

# Plotting
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
for i in range(n):
    #ax.plot(pxplot[i], pyplot[i], pzplot[i], label=f'Particle {i+1}')
    ax.plot(pxplot[i], pyplot[i], pzplot[i])


#Ploteando las referencias
ax.plot(u, v, w, color='red')
ax.plot(uc, vc, wc, color='red')
    
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
#ax.legend()

plt.show()
