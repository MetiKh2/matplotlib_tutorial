import matplotlib.pyplot as plt
import numpy as np

y=np.array([35,25,25,15])
labels=['Apples','Bananas','Cherries','Dates']
explode=[0.2,0,0,0]
colors=['black','hotpink','b','#4caf50']
plt.pie(y,labels=labels,startangle=90,explode=explode,shadow=True,colors=colors)
plt.legend(title='Four Fruits : ')
plt.show()
