import os

def Tablear():
    X0 = 0
    Y0 = 0
    XF = 2
    YF = 3.5

    XINCREMENTS = 100
    YINCREMENTS = 20

    os.chdir('SuperFish_Archivos')

    DIR = "C:\LANL"
    
    f = open(f"Iman.IN7", "w")
    f.write(f"Grid\n")
    f.write(f"{X0} {Y0} {XF} {YF}\n")
    f.write(f"{XINCREMENTS} {YINCREMENTS}\n")
    f.write(f"End")
    f.close()

    os.system(f'{DIR}\AUTOMESH.EXE Iman.am')
    os.system(f'{DIR}\PANDIRA.EXE IMAN.T35')
    os.system(f'{DIR}\SF7.EXE IMAN.IN7 IMAN.T35')

