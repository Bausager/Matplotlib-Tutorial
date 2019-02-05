import matplotlib.pyplot as plt
import numpy as np

                    #Part 1
'''
import csv

x = []
y = []



with open("07. Loading data from Files.txt", 'r') as csvfile:
    plots = csv.reader(csvfile, delimiter=",")
    for row in plots:
        x.append(int(row[0]))
        y.append(int(row[1]))


plt.plot(x,y,
         label="Loaded from file")


plt.xlabel("x")
plt.ylabel("y")

plt.title('Intresting Graph\nCheck it out!')
plt.legend()
plt.show()
'''


                    #Part 2
                    
x, y = np.loadtxt("07. Loading data from Files.txt",
                  delimiter=',', #What seperates the data in the .txt
                  unpack=True) #It unpacks it

plt.plot(x,y, label="Loaded from file")


plt.xlabel("x")
plt.ylabel("y")

plt.title('Intresting Graph\nCheck it out!')
plt.legend()
plt.show()




















