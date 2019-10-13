import matplotlib.pyplot as plt
import numpy as np
x=[-1,0]
y=[-2,0]
plt.plot(x,y)
plt.xlabel('x-axis')
plt.ylabel('y-axis')
plt.title('my plot')
theta=1
a=np.arange(0,(2*(np.pi))/theta,0.1)
b=np.sin(a)
plt.plot(a,b)
plt.axes()
#circle=plt.Circle((-2,-3),1)
#plt.gca().add_patch(circle)
plt.axis('scaled')
plt.show()

