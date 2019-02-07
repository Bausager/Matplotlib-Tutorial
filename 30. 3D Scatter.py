from mpl_toolkits.mplot3d import axes3d
import matplotlib.pyplot as plt
from matplotlib import style

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
ax1.scatter(x1 ,y1 ,z1) 
ax1.scatter(x2 ,y2 ,z2)

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
