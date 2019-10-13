import matplotlib.pyplot as plt
import numpy as np
plt.axes()
circle=plt.Circle((0,0),5)
plt.gca().add_patch(circle)
plt.axis('scaled')
plt.show()
