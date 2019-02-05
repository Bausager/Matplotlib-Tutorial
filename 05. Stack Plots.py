import matplotlib.pyplot as plt


days = [1,2,3,4,5]

sleeping =[7,8,6,11,7]
eating =   [2,3,4,3,2]
working = [7,8,7,2,2]
playning =[8,5,7,8,13]

plt.stackplot(days,  sleeping, eating, working, playning, 
              colors=["m","c","r","k"])

#Since we can't make labels for stackplots, well get around it by making another plot
plt.plot([],[], color="m", label="Sleeping", linewidth=5)
plt.plot([],[], color="c", label="Eating", linewidth=5)
plt.plot([],[], color="r", label="Working", linewidth=5)
plt.plot([],[], color="k", label="Playing", linewidth=5)

plt.xlabel("x")
plt.ylabel("y")

plt.title('Intresting Graph\nCheck it out!')
plt.legend()
plt.show()
