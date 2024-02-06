import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

x=[0,1,2,3,4]
y=[0,3,6,9,12]

plt.figure(figsize=(5,3), dpi=150)

# plt.plot(x,y,label='3x',color='red',linewidth=2,marker='.',markersize=10,markeredgecolor='black',linestyle='--')
plt.plot(x,y,'b^--',label='3x')

x2 = np.arange(0,4.5,0.5)
plt.plot(x2[:7],x2[:7]**2,'r',label='x^2')
plt.plot(x2[6:],x2[6:]**2,'r--',label='x^2')

plt.title('Test Graph', fontdict={'fontname': 'Comic Sans MS', 'fontsize': 20})
plt.xlabel('X Axis')
plt.ylabel('Y Axis')

plt.xticks([0,1,2,3,4])
# plt.yticks([3,6,9,12])

plt.legend()

plt.savefig('testgraph.png', dpi=300)

plt.show()