import numpy as np
import matplotlib.animation as animation
import matplotlib.pyplot as plt
import mpl_toolkits.mplot3d.axes3d as p3


def animate_scatters(frame, total_frames, data, points):

    amplitude = 0.5
    sigma = 1.5
    wave_pos = (np.min(x) - 3) + (frame/total_frames) * (np.max(x) - np.min(x) + 6)

    x_shifted = data[0] + amplitude * np.exp(-np.power((wave_pos - x)/sigma, 2))

    points._offsets3d = (x_shifted, data[1], data[2])

    return points


save = True

nx = 10
ny = 2
nz = 2
dimensions = [nx, ny, nz]

spacing_x = 1
spacing_y = 1
spacing_z = 1

x_lim = nx * spacing_x
y_lim = ny * spacing_y
z_lim = nz * spacing_z

x_list = []
y_list = []
z_list = []

for x in range(nx+1):
    x_list += [x * spacing_x - x_lim/2] * (ny+1) * (nz+1)

    for y in range(ny+1):
        for z in range(nz+1):
            y_list += [y * spacing_y - y_lim/2]
            z_list += [z * spacing_z - z_lim/2]

x = np.array(x_list)
y = np.array(y_list)
z = np.array(z_list)

# Attaching 3D axis to the figure
fig = plt.figure(figsize=[12, 8])
ax = p3.Axes3D(fig)

# Initialize scatters
scatters = ax.scatter(x, y, z, c=x, s=40)

# Number of iterations
iterations = 80

spacing_x = 1
spacing_y = 1
spacing_z = 1

x_lim = dimensions[0] * spacing_x
y_lim = dimensions[1] * spacing_y
z_lim = dimensions[2] * spacing_z
lim = max([x_lim, y_lim, z_lim])
zoom = 3

# Setting the axes properties
ax.set_xlim3d((-lim/zoom, lim/zoom))
ax.set_xlabel('X')

ax.set_ylim3d((-lim/zoom, lim/zoom))
ax.set_ylabel('Y')

ax.set_zlim3d((-lim/zoom, lim/zoom))
ax.set_zlabel('Z')

ax.set_title('3D Animated Scatter Example')
ax.axis('off')

# Provide starting angle for the view.
ax.view_init(25, 60)

ani = animation.FuncAnimation(
    fig,
    animate_scatters,
    iterations,
    fargs=(iterations, [x, y, z], scatters),
    interval=50,
    blit=False,
    repeat=True
)

if save:
    print('Writing animation file.')
    Writer = animation.writers['ffmpeg']
    writer = Writer(fps=30, metadata=dict(artist='Me'), bitrate=1800, extra_args=['-vcodec', 'libx264'])
    ani.save('animations/matplotlib/3d-scatter-animated.mp4', writer=writer)

plt.show()
