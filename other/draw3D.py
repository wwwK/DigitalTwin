from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
import numpy as np
import random

plt.rcParams["font.family"] = "simsun"
fig = plt.figure()

ax = fig.add_subplot(111, projection='3d')


for i in range(15):
    xs = random.uniform(0,0.2)
    ys = random.uniform(0,0.2)
    zs = random.uniform(0,0.2)
    ax.scatter(xs, ys, zs, c=1, marker="o",linewidths=(xs+ys+zs)*20)

ax.scatter(0.2, 0.15, 0.3, c=1, marker="o",linewidths=(xs+ys+zs)*20)

ax.set_xlabel('   电流大小')
ax.set_ylabel('   电压大小')
ax.set_zlabel('   焊丝直径')

plt.show()








# def randrange(n, vmin, vmax):
#     '''
#     Helper function to make an array of random numbers having shape (n, )
#     with each number distributed Uniform(vmin, vmax).
#     '''
#     return (vmax - vmin) * np.random.rand(n) + vmin
#
#
# fig = plt.figure()
# ax = fig.add_subplot(111, projection='3d')
#
# n = 100
#
# # For each set of style and range settings, plot n random points in the box
# # defined by x in [23, 32], y in [0, 100], z in [zlow, zhigh].
# for c, m, zlow, zhigh in [('r', 'o', -50, -25), ('b', '^', -30, -5)]:
#     xs = randrange(n, 23, 32)
#     ys = randrange(n, 0, 100)
#     zs = randrange(n, zlow, zhigh)
#     ax.scatter(xs, ys, zs, c=(0.1,0.2,0.3), marker="o")
#
# ax.set_xlabel('X Label')
# ax.set_ylabel('Y Label')
# ax.set_zlabel('Z Label')
#
# plt.show()