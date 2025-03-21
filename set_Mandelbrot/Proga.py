import numpy as np
import matplotlib.pyplot as plt
from squariki import upgrade_range, C, square_complex

Zn = []

Z1 = 0 + 0j

for x in upgrade_range(-4, 4, 0.1):
    for y in upgrade_range(-4, 4, 0.1):
        Z1 = square_complex(x, y)
        Zn.append(Z1)
Zn = np.array(Zn)

x = Zn.real
y = Zn.imag

plt.plot(x, y, 'g*')

plt.ylabel('Imaginary')
plt.xlabel('Real')
plt.show()




