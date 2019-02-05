import matplotlib.pyplot as plt

x = [2,4,6,8,10]
y = [6,7,8,2,4]

x2 = [1,3,5,9,11]
y2 = [2,5,6,8,12]

population_ages = [23,54,67,32,65,23,65,34,23,65,23,76,23,76,23,12,65,73,13,78,32,35,23,76,43,87,93,20,74,39,20,56,20]

bins = [0,10,20,30,40,50,60,70,80,90,100]

plt.hist(population_ages, bins, histtype="bar", rwidth=0.8) #Finds the larges age groups

#plt.bar(x, y, label="Bar V.1.0")#, color="blue") #You can use Hex colors or look it up. It works well without deffining!!!!!!!!
#plt.bar(x2, y2, label="Bar V.2.0")#, color="red")

plt.xlabel("x")
plt.ylabel("y")

plt.title('Intresting Graph\nCheck it out!')
plt.legend()
plt.show()
