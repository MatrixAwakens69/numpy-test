import matplotlib.pyplot as plt
import numpy as numpy
import pandas as pd

x=[1,2,3,4]
y=[3,6,9,12]
plt.plot(x,y,label='3x',color='red',linewidth=2,marker='.',markersize=10,markeredgecolor='black',linestyle='--')

plt.title('Test Graph', fontdict={'fontname': 'Comic Sans MS', 'fontsize': 20})
plt.xlabel('X Axis')
plt.ylabel('Y Axis')

plt.xticks([1,2,3,4])
plt.yticks([3,6,9,12])

plt.legend()

plt.show()