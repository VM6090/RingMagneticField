import os
import numpy as np
from matplotlib import pyplot as plt
import pickle

n = 50 # Number of particles

m = 1  # Mass in kg
q = -0.5  # Charge in Coulombs
L = 2  # Length in meters

# Initial positions
x0 = np.random.uniform(-L/2, L/2, n)
y0 = np.random.uniform(-L/2, L/2, n)
z0 = np.zeros(n)  # Assuming starting at z = 0

# Initialize velocities
vx = np.random.rand(n)  # Random initial velocities
vy = np.random.rand(n)
vz = np.random.rand(n)


t = 0       # Tiempo inicial
dt = 1e-3   # Time step in seconds
tf = 20     # Final time

# Lists to store positions for plotting
pxplot = [[] for _ in range(n)]
pyplot = [[] for _ in range(n)]
pzplot = [[] for _ in range(n)]

# Initial positions stored for plotting
for i in range(n):
    pxplot[i].append(x0[i])
    pyplot[i].append(y0[i])
    pzplot[i].append(z0[i])

os.chdir('SuperFish_Archivos')

# Encontrar los incrementos en X y Y de la cuadricula
data = np.loadtxt('OUTSF7.txt', skiprows=30, usecols = (4,5), dtype="U")
nticks = int(data[0, 0])
mticks = int(data[0, 1])


# Función para encontrar el índice del número más cercano a "value" en una lista "array"
def find_nearest(array, value):
    array = np.asarray(array)
    idx = (np.abs(array - value)).argmin()
    return idx
    

# Lectura de datos para el campo magnético
data = np.loadtxt('OUTSF7.txt', skiprows=34, usecols = (0,1,2,3))

# Inicializa listas para almacenar los datos
x_values = data[:, 0]
y_values = data[:, 1]
bx_values = data[:, 2]
by_values = data[:, 3]


# Relación de posiciones Y con la tabla de SuperFish
y_ticks = []                        # Lista para posiciones Y
x_ticks = np.zeros(nticks + 1)      # Lista para posiciones X
for j in range(mticks+1):
    y_ticks.append(y_values[j*(nticks+1)])



# Simulación
while t < tf:
    for i in range(n):

        # Relación de posiciones X con la tabla de SuperFish
        rho = np.sqrt(((x0[i])**2 + (y0[i])**2)**2)
        y_idx = find_nearest(y_ticks, z0[i])

        for j in range(nticks+1):
            x_ticks[j] = x_values[y_idx*(nticks+1) + j]

        x_idx = find_nearest(x_ticks, rho) + y_idx*(nticks+1)


        # Magnetic field components based on position
        Bx = bx_values[x_idx] * x0[i] / rho
        By = bx_values[x_idx] * y0[i] / rho
        Bz = by_values[x_idx]

        
        # Update velocities based on Lorentz force
        vx[i] += (dt / m) * (q * (vy[i] * Bz - vz[i] * By))
        vy[i] += (dt / m) * (q * (vz[i] * Bx - vx[i] * Bz))
        vz[i] += (dt / m) * (q * (vx[i] * By - vy[i] * Bx))

        # Update positions
        x0[i] += vx[i] * dt
        y0[i] += vy[i] * dt
        z0[i] += vz[i] * dt

        # Condición para detener partícula
        if z0[i] < 0 or x0[i]**2 + y0[i]**2 > L**2:
            continue

        # Store positions for plotting
        pxplot[i].append(x0[i])
        pyplot[i].append(y0[i])
        pzplot[i].append(z0[i])
        
    print(int((t/tf)*100), '%', end='\r', flush=True) 
    t += dt


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
    ax.plot(pxplot[i], pyplot[i], pzplot[i])

#Ploteando las referencias
ax.plot(u, v, w, color='red')
ax.plot(uc, vc, wc, color='red')
    
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')

# Guardado de la figura interactiva 3D
os.chdir('..')

def fig_filename(base_name, extension):
    # Start with a counter
    counter = 0
    # Generate the initial file name
    file_name = f"{base_name}({counter}).{extension}"

    # Loop until an available file name is found
    while os.path.exists(file_name):
        counter += 1
        file_name = f"{base_name}({counter}).{extension}"
    return file_name

#pickle.dump(fig, open(f'FigureObject.fig.pickle', 'wb'))
pickle.dump(fig, open(f'{fig_filename('Figura3D_', 'fig.pickle')}', 'wb'))
plt.show()

input()
