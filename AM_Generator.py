# Generador de códigos AutoMesh (am) para SuperFish#
#
# Perfil cilíndrico de un imán circular con poste interior
# como polo positivo y anillo exterior como polo negativo.
import os
import numpy as np
from matplotlib import pyplot as plt

os.system('mkdir SuperFish_Archivos')
os.chdir('SuperFish_Archivos')

#----- Precisión del mallado -----#
dx = .05

#----- Distancia entre los centros de los imanes -----#
L = 2

#----- Altura (TY) y Ancho (TX) de los imanes -----#
TX = 1
TY = 0.5

#----- Ancho de la placa -----#
D = 0.03

#----- Separación del iman exterior a las paredes de la región de simulación -----#
SP = 0.5

#----- Separación de la placa al techo de la simulación -----#
A1 = 2.5
A2 = 0.5

#----- Ancho (REG1) y Altura (REG2) de la región de simulación -----#
REG1 = L + TX/2 + SP
REG2 = A2 + TY  + A1

#----- Distancia entre las paredes de los imanes -----#
SI = L - 2*TX

#----- Intensidad de BCEPT y HCEPT -----#
BCEPT = 300
HCEPT = -10000


x = 0.0
y = -TY -A2

f = open(f"Iman.am", "w")

f.write(f"pole Magnet Problem \nHarmonic analysis using 11 points at Rint = 1.86 cm \nbetween 0 and 45 degrees shows relatively poor field \npurity (i.e., large values of higher-order coefficients). \n[Originally appeared in 1987 Reference Manual B.12.1] \n; Copyright 1987, by the University of California.  \n; Unauthorized commercial use is prohibited.\n")
f.write(f"\n&reg kprob=0,           ; Poisson or Pandira problem \nmode=0                  ; Some materials have variable permeability \ndx={dx}, \nnbsup=0, \nnbslo=1,  \nnbsrt=0,  \nnbslf=0, \nmat = 1, \nyreg1=0.75, \nyreg2=1.75 &\n")
f.write("\n")

f.write(f"&po x={x}, y={y} &\n")
f.write(f"&po x={REG1}, y={y} &\n")
f.write(f"&po x={REG1}, y={REG2} &\n")
f.write(f"&po x={x}, y={REG2} &\n")
f.write(f"&po x={x}, y={y} &\n")
f.write(f"\n")



x = 0.0
y = -TY - D
f.write(f"&reg mat = 6, mshape=1, mtid=1 &\n")
f.write(f"&po x={x}, y={y} &\n")
f.write(f"&po x={x+TX/2}, y={y} &\n")
f.write(f"&po x={x+TX/2}, y={-D} &\n")
f.write(f"&po x={x}, y={-D} &\n")
f.write(f"&po x={x}, y={y} &\n")
f.write(f"\n")



x = L - TX/2
y = -TY - D
f.write(f"&reg mat = 7, mshape=1, mtid=2 &\n")
f.write(f"&po x={x}, y={y} &\n")
f.write(f"&po x={x+TX}, y={y} &\n")
f.write(f"&po x={x+TX}, y={-D} &\n")
f.write(f"&po x={x}, y={-D} &\n")
f.write(f"&po x={x}, y={y} &\n")
f.write(f"\n")



x = 0.0
y = -D
f.write(f"&reg mat = 1 &\n")
f.write(f"&po x={x}, y={y} &\n")
f.write(f"&po x={x+L+TX/2}, y={y} &\n")
f.write(f"&po x={x+L+TX/2}, y={0.0} &\n")
f.write(f"&po x={x}, y={0.0} &\n")
f.write(f"&po x={x}, y={y} &\n")
f.write(f"\n")


f.write(f"&mt mtid=1 \naeasy=90, gamper=1 \nhcept={HCEPT}, bcept={BCEPT} &\n")
f.write(f"\n&mt mtid=2 \naeasy=-90, gamper=1 \nhcept={HCEPT}, bcept={BCEPT} &\n")

f.close()

os.chdir('..')
from Tableador import Tablear
Tablear()
