
# coding: utf-8

# In[20]:

import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import interp1d

x00 = np.random.random (10)
x0 = x00*3
y0 = sin (2*x0)

plt.plot(x0, y0, 'o', label='Data')

x=np.linspace(min(x0), max(x0), 101)

options = ('linear', 'quadratic', 'cubic')

for o in options:
    f = interp1d(x0, y0, kind=o)    
    plt.plot(x, f(x), label=o), 
plt.legend(loc='best')
plt.show()


# In[22]:

import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import interp1d

x00 = np.random.random (10)
x0 = ((x00*20)-10)
y0 = sin (2*x0)/x0

plt.plot(x0, y0, 'o', label='Data')

x=np.linspace(min(x0), max(x0), 101)

options = ('linear', 'quadratic', 'cubic')

for o in options:
    f = interp1d(x0, y0, kind=o)    
    plt.plot(x, f(x), label=o)      

plt.legend('loc=best')
plt.show()


# In[24]:

import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import interp1d

x00 = np.random.random (16)
x0 = ((x00*6)-3)
y0 = (x0**2)*(sin(2*x0))

plt.plot(x0, y0, 'o', label='Data')

x=np.linspace(min(x0), max(x0), 101)

options = ('linear', 'quadratic', 'cubic')

for o in options:
    f = interp1d(x0, y0, kind=o)    
    plt.plot(x, f(x), label=o)      

plt.legend('loc=best')
plt.show()


# In[40]:

import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import interp1d

x00 = np.random.random (12)
x0 = ((x00*4)-2)
y0 = (x0**3)*(sin(3*x0))

plt.plot(x0, y0, 'o', label='Data')

x=np.linspace(min(x0), max(x0), 101)

options = ('linear', 'quadratic', 'cubic')

for o in options:
    f = interp1d(x0, y0, kind=o)    
    plt.plot(x, f(x), label=o)      

plt.legend('loc=best')
plt.show()


# In[ ]:



