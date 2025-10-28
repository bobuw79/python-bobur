import numpy as np
import matplotlib.pyplot as plt

def mandelbrot(c, max_iter):
    z = 0
    for n in range(max_iter):
        z = z*z + c
        if abs(z) > 2:
            return n
    return max_iter

def mandelbrot_set(xmin,xmax,ymin,ymax,width,height,max_iter):
    r1 = np.linspace(xmin, xmax, width)
    r2 = np.linspace(ymin, ymax, height)
    result = np.empty((width, height))
    for i in range(width):
        for j in range(height):
            result[i,j] = mandelbrot(r1[i] + 1j*r2[j], max_iter)
    return result

# Parametrlar
xmin, xmax, ymin, ymax = -2.0, 1.0, -1.5, 1.5
width, height = 800, 600
max_iter = 256

# Fraktal to'plamni hisoblash
mandelbrot_image = mandelbrot_set(xmin, xmax, ymin, ymax, width, height, max_iter)

# Rasmni chizish
plt.imshow(mandelbrot_image.T, extent=[xmin, xmax, ymin, ymax], cmap='hot')
plt.xlabel('Re')
plt.ylabel('Im')
plt.title('Mandelbrot Set')
plt.show()
