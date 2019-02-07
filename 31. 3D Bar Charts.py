from mpl_toolkits.mplot3d import axes3d
import matplotlib.pyplot as plt
import numpy as np


from matplotlib import style
print(plt.style.available) #Deffient styles in matplot.
style.use('fivethirtyeight')



fig = plt.figure()
ax1 = fig.add_subplot(111, projection='3d')


x1 = [1,2,3,4,5,6,7,8,9,10]
y1 = [5,6,7,8,2,5,6,3,7,2]
z1 = [1,2,6,3,2,7,3,3,7,2]




x2 = [-1,-2,-3,-4,-5,-6,-7,-8,-9,-10]
y2 = [-5,-6,-7,-8,-2,-5,-6,-3,-7,-2]
z2 = [1,2,6,3,2,7,3,3,7,2]



###3d line plot
#ax1.plot(x1,y1,z1)


###3d scatter plot
#ax1.scatter(x1 ,y1 ,z1) 
#ax1.scatter(x2 ,y2 ,z2)'



###3d bar charts
x3 = [1,2,3,4,5,6,7,8,9,10]
y3 = [5,6,7,8,2,5,6,3,7,2]
z3 = np.zeros(10)

dx = np.ones(10)
dy = np.ones(10)
dz = x3 #Starting point for the bars

ax1.bar3d(x3, y3, z3, dx, dy, dz)







'''
For changing color;

###3d scatter plot
ax1.scatter(x1 ,y1 ,z1, c='k') 
ax1.scatter(x2 ,y2 ,z2, c='r')

'''

ax1.set_xlabel('x axis')
ax1.set_ylabel('y axis')
ax1.set_zlabel('z axis')

plt.show()
