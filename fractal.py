# !/usr/bin/env python3

import matplotlib.pyplot as plt

# establecer el valor de x, y, l, n
x = 0.0
y = 0.0
l = 1.0  # longitud del perímetro de cada lado
n = 3  # número de iteraciones

# establecer las coordenadas de los puntos
p_0 = (x, y)
p_1 = (x + l, y)
p_2 = (x + l, y + l)
p_3 = (x, y + l)


# crear la función fractal

def fractal(n, x, y, l):
    # crear el cuadrado principal
    p_0 = (x, y)
    p_1 = (x + l, y)
    p_2 = (x + l, y + l)
    p_3 = (x, y + l)
    ax.plot([p_0[0], p_1[0], p_2[0], p_3[0], p_0[0]],
            [p_0[1], p_1[1], p_2[1], p_3[1], p_0[1]])
    # crear cuadrados posteriores
    if n > 0:
        x_1 = x + l
        y_1 = y + l / 3
        fractal(n - 1, x_1, y_1, l / 3)
        x_2 = x + l / 3
        y_2 = y - l / 3
        fractal(n - 1, x_2, y_2, l / 3)
        x_3 = x - l / 3
        y_3 = y + l / 3
        fractal(n - 1, x_3, y_3, l / 3)
        x_4 = x + l / 3
        y_4 = y + l
        fractal(n - 1, x_4, y_4, l / 3)


fig, ax = plt.subplots()
ax.set_aspect(1)
fractal(n, x, y, l)
plt.savefig("fractal.png")
plt.show()


