"""
buscar_tabs.py
==============
Abre la app y muestra en tiempo real la posicion del mouse.
Mueve el mouse sobre cada pestaña y anota los valores.

Ejecutar:  python buscar_tabs.py
"""
import sys, subprocess, time

def _i(p,i=None):
    try: __import__(i or p)
    except: subprocess.check_call([sys.executable,"-m","pip","install",p],
                                   stdout=subprocess.DEVNULL,stderr=subprocess.DEVNULL)
_i("pyautogui"); _i("pygetwindow")

import pyautogui, pygetwindow as gw

EXE = r"C:\Users\Ashleidy\Desktop\TechniSupport2\TechniSupport.exe"

print("Iniciando app...")
p = subprocess.Popen([EXE])
time.sleep(5)

# Cerrar popup
wins = gw.getWindowsWithTitle("Conexión exitosa")
if wins:
    wins[0].activate(); time.sleep(0.3)
    pyautogui.press("enter"); time.sleep(0.8)

# Mostrar ventana info
wins = gw.getWindowsWithTitle("BASES DE DATOS")
if wins:
    v = wins[0]
    print(f"\nVentana: left={v.left} top={v.top} w={v.width} h={v.height}")
    print(f"  Y absoluto de la barra de tabs estimado: {v.top + 32}")

print("\n" + "="*50)
print("MUEVE EL MOUSE SOBRE CADA PESTAÑA Y ANOTA x,y")
print("Mostrando posicion cada 0.5s durante 60 segundos")
print("="*50)

for _ in range(120):
    x, y = pyautogui.position()
    wins2 = gw.getWindowsWithTitle("BASES DE DATOS")
    if wins2:
        v = wins2[0]
        print(f"  abs=({x:4d},{y:4d})  rel=({x-v.left:3d},{y-v.top:3d})", end="\r")
    time.sleep(0.5)

print("\n\nCerrando...")
p.terminate()