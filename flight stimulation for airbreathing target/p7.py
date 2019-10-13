import matplotlib.pyplot as plt
import numpy as np
theta=int(input())
x=np.arange(0,(2*(np.pi))/theta,0.1)
y=np.sin(x)
plt.plot(x,y)
plt.show()
