import time
import matplotlib.pyplot as plt
import random

#Initialize figure
fig = plt.figure()
ax = fig.add_subplot(111)
fig.show()
fig.suptitle('Real time view',fontsize=20)
plt.ylabel('MQ values in volts',fontsize=14)
plt.xlabel('Iterations',fontsize=12)
plt.xticks(rotation=45)
sensors = ['MQ2', 'MQ3', 'MQ4', 'MQ6', 'MQ7', 'MQ8', 'MQ135']
x,y = [],[]
a,b = [],[]

for val in range(1000):
    x.append(val)
    y.append(random.randint(0,9))
    ax.plot(x,y,color='b')
    a.append(val)
    b.append(random.randint(0,9))
    ax.plot(a,b,color='r')
    
    fig.canvas.draw()
    plt.pause(.5)

#fig.savefig('test.png')