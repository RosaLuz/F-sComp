
# coding: utf-8

# In[58]:

file = open('pressuredata.txt', 'r+')

with open('pressuredata.txt', 'r') as f:
    data = f.readlines()

    for line in data:
        columns = line.split(",")
        print columns
        
from scipy.optimize import curve_fit        
import matplotlib.pyplot as plt
import numpy as np

datos = np.loadtxt('pressuredata.txt')
x=datos[:,0]
y=datos[:,1]
print x
print y

#Escribiendo con la forma de y=a*e^(-bx)+c
def func(x, A, B, C):
    return A * np.exp(-B * x) + C

#Generando estimacion base
Y = y + 0.2*np.random.normal(size=len(x))

#Optimizando la curva
popt, pcov = curve_fit(func, x, Y)

#Para la grafica
plt.figure()
plt.plot(x, Y, 'yo', label="Datos")
plt.plot(x, func(x, *popt), 'g-', label="Curva ajustada")

plt.grid()
plt.legend()
plt.title("Presion atmosferica vs. Altitud")
plt.xlabel("Altitud")
plt.ylabel("Presion")

plt.show()

        
        


# In[59]:

from scipy import optimize
import matplotlib.pyplot as plt
import numpy as np
datos = np.loadtxt('temperaturedata.txt')
x=datos[:,0]
y=datos[:,1]
print x
print y
plt.plot(x,y,'yo')

fitfunc = lambda p, x: p[0]*x + p[1]

errfunc = lambda p, x, y: fitfunc(p, x) - y 

p0 = [10, 5] 

p1, success = optimize.leastsq(errfunc, p0[:], args=(x, y))

time = np.linspace(x.min(), x.max(), 100)
plt.plot(x, y, "co", label="Datos") 
plt.plot(time, fitfunc(p1, time), "m-", label="Curva ajustada")

plt.title("Temperatura de invierno en Nueva York (1900-1999)")
plt.grid()
plt.legend()
plt.xlabel("Anio")
plt.ylabel("Temperatura")


# In[ ]:



