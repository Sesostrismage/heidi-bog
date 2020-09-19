import matplotlib.pyplot as plt
import pandas as pd

from mpl_toolkits.mplot3d import Axes3D
from matplotlib.colors import cnames
from matplotlib import animation
from scipy import integrate

spacing_x = 1
spacing_y = 1
spacing_z = 1

n_x = 5
n_y = 5
n_z = 20

x_lim = n_x * spacing_x
y_lim = n_y * spacing_y
z_lim = n_z * spacing_z
lim = max([x_lim, y_lim, z_lim])
zoom = 3

amplitude = 0.2
speed = 0.1

x_list = []
y_list = []
z_list = []

for x in range(n_x+1):
    for y in range(n_y+1):
        for z in range(n_z+1):
            x_list.append([x * spacing_x - x_lim/2])
            y_list.append([y * spacing_y - y_lim/2])
            z_list.append([z * spacing_z - z_lim/2])

# Set up figure & 3D axis for animation
fig = plt.figure()
ax = fig.add_axes([0, 0, 1, 1], projection='3d')

ax.axis('off')
ax.set_xlim3d((-lim/zoom, lim/zoom))
ax.set_ylim3d((-lim/zoom, lim/zoom))
ax.set_zlim3d((-lim/zoom, lim/zoom))

ax.scatter(x_list, y_list, z_list)
plt.show()