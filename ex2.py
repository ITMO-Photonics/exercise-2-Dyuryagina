import matplotlib.pyplot as plt # Pyplot is used for visualization
import numpy as np # np will be used as its short name for NumPy

print("hello, this is ex 2")

fig, ax = plt.subplots()
x=np.linspace(0.,10.,100) # 100 discrete points between 0. and 10.
y1=np.sin(x)

ax.plot(x,y1,color='black')

plt.show()

