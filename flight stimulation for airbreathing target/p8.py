import matplotlib.pyplot as plt
from matplotlib.patches import Arc

m=[0,-0.5]
n=[-0.5,0]

R = 1.0
x, y = 0.0, 0.0
a, b = R, R

fig_width, fig_height = 1,1
fig = plt.figure(figsize=(fig_width, fig_height), frameon=False)
ax = fig.add_axes([0.0, 0.0, 1.0, 1.0], aspect='equal')
ax.set_xlim(-R, R)
ax.set_ylim(-R, R)


ax.axhline(0.0)
ax.axvline(0.0)

print("give the theta1")
z = float(input())
ax.add_patch(Arc((x, y), a, b, theta1=0.0, theta2=360.0, edgecolor='w'))
print("give the theta2")
p = float(input())
q=z
r=p
ax.add_patch(Arc((x, y), a, b,theta1=q, theta2=r, edgecolor='b', lw=1.5))
plt.plot(x,y,m,n)
plt.show()

