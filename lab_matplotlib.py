import numpy as np
import matplotlib.pyplot as plt

# шкалы по x и y
xlist = np.linspace(-3.0, 3.0, 100)
ylist = np.linspace(-3.0, 3.0, 100)

# прямоугольные массивы типа meshgrid из шкал осей OX и OY
X, Y = np.meshgrid(xlist, ylist)

# двумерный Z на основе двумерных матриц X и Y
Z = np.sqrt(X**2 + Y**2)

fig,ax=plt.subplots(1,1)
cp = ax.contourf(X, Y, Z)
fig.colorbar(cp) # Add a colorbar to a plot
ax.set_title('Filled Contours Plot')
plt.show()