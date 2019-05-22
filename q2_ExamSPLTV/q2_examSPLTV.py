'''
=============================================================
Question 2 - SPLTV
=============================================================
'''

import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import axes3d

persamaan = np.array([
    [1,-2,1],
    [3,1,-2],
    [7,-6,-1]
])

hasil = np.array([6,4,10])

result = np.linalg.solve(persamaan,hasil)

x = result[0]
y = round(result[1])
z = result[2]

# Plot Equation
x1 = np.array([[persamaan[0][0]*x,0,0]])
y1 = np.array([[0,persamaan[0][1]*y,0]])
z1 = np.array([[0,0,persamaan[0][2]*z]])

x2 = np.array([[persamaan[1][0]*x,0,0]])
y2 = np.array([[0,persamaan[1][1]*y,0]])
z2 = np.array([[0,0,persamaan[1][2]*z]])

x3 = np.array([[persamaan[2][0]*x,0,0]])
y3 = np.array([[0,persamaan[2][1]*y,0]])
z3 = np.array([[0,0,persamaan[2][2]*z]])

# Plotting the graph
fig = plt.figure('Plot Result', figsize=(15,6))

# Plot 1
plot1 = plt.subplot(131, projection='3d')
plot1.scatter(x1,y1,z1, color='blue')
plot1.plot_wireframe(x1,y1,z1, facecolors='red', alpha=0.3)
plot1.set_title('x  - 2y +  z =  6')
plot1.set_xlabel('x-value')
plot1.set_ylabel('y-value')
plot1.set_zlabel('z-value')

# Plot 2
plot2 = plt.subplot(132, projection='3d')
plot2.scatter(x2,y2,z2, color='orange')
plot2.plot_wireframe(x2,y2,z2, facecolors='yellow', alpha=0.3)
plot2.set_title('3x +  y - 2z =  4')
plot2.set_xlabel('x-value')
plot2.set_ylabel('y-value')
plot2.set_zlabel('z-value')

# Plot 3
plot3 = plt.subplot(133, projection='3d')
plot3.scatter(x3,y3,z3, color='blue')
plot3.plot_wireframe(x3,y3,z3, facecolors='purple', alpha=0.3)
plot3.set_title('7x - 6y -  z = 10')
plot3.set_xlabel('x-value')
plot3.set_ylabel('y-value')
plot3.set_zlabel('z-value')

plt.tight_layout()

plt.show()