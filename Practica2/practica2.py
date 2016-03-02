
# coding: utf-8

# In[1]:

from math import sqrt
h= float(input("Proporciona la altura de la torre: "))
t=sqrt((2*h)/9.81)
print("El tiempo que la pelota tarda en caer es", t, "segundos.")


# In[2]:

from math import pi
G=6.67e-11
M=5.97e24
R=6371000
t= float(input("Proporciona el periodo del satélite:"))
T= t*60
a=(G*M*T*T) / (4*pi*pi)
b=a**(1./3.)
h=b-R
print ("La altura del satélite es", h, "metros.")


# In[3]:

from math import atan, sqrt
x = float(input("Ingresa la coordenada x: "))
y = float(input("Ingresa la coordenada y: "))
z = float(input("Ingresa la coordenada z: "))
r = sqrt((x*x)+(y*y)+(z*z))
theta = atan((sqrt((x*x)+(y*y)))/z)
phi = atan (y/x)$

print("r =",r," theta =",theta," phi =",phi,)


# In[4]:

print("Escriba dos enteros, uno para y unoimpar")
m = int(input("Escriba el primer entero: "))
n = int(input("Escriba el segundo entero: "))
while (m+n)%2==0:
    print("Uno debe ser para y el otro impar.")
    m = int(input("Escriba el primer entero: "))
    n = int(input("Escriba el segundo entero: "))
print("Los números que elegiste son",m,"y",n)


# In[5]:

C1=1
C2=1
n=0
while C2<10000:
    print (C2)
    C2 = C1*(4*n+2)/(n+2)
    C1=C2
    n=n+1


# In[ ]:



