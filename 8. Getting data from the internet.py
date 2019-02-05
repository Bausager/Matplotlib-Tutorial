import matplotlib.pyplot as plt
import numpy as np







x, y = np.loadtxt("7. Loading data from Files.txt",
                  delimiter=',', #What seperates the data in the .txt
                  unpack=True) #It unpacks it

plt.plot(x,y, label="Loaded from file")


plt.xlabel("x")
plt.ylabel("y")

plt.title('Intresting Graph\nCheck it out!')
plt.legend()
plt.show()




















