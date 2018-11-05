import numpy as np
import matplotlib.pyplot as plt

func = np.poly1d(np.array([1,2,3,4]).astype(float))
func1 = func.deriv(1)
x = np.linspace(-10,10,30)
y = func(x)
y1 = func1(x)
plt.plot(x,y,':r', label='y=f(x)')
plt.plot(x,y1,'-g', label=r"y=f'(x)")
plt.legend()
plt.show()