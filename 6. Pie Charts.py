import matplotlib.pyplot as plt


days = [1,2,3,4,5]

sleeping =[7,8,6,11,7]
eating =   [2,3,4,3,2]
working = [7,8,7,2,2]
playning =[8,5,7,8,13]

slices = [7,2,2,13]
activities = ["sleeping","eating","working","playing"]
color=["m","c","r","b"]

plt.pie(slices,
        labels=activities, #Pieace of the pie
        colors=color, #Predefined colors
        startangle=90,#Starting angle
        shadow=True, #Creats a shadow behind the pie
        explode=(0,0,0.1,0), #Make a piace of the pie come out (deffined by activities)
        autopct="%1.1f%%") #Displays the procentage on the pie (Don't ask)

#plt.xlabel("x")
#plt.ylabel("y")

plt.title('Intresting Graph\nCheck it out!')
#plt.legend()
plt.show()
