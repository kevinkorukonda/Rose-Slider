import matplotlib.pyplot as plt
from matplotlib.widgets import Slider
import numpy as np

# set default values of n and d
n, d = 2, 1
# calculate value of k (frequency)
k = n / d
theta = np.linspace(0, 16 * k * np.pi, 1000)

r = np.cos(k * theta)

x = r * np.cos(theta)

y = r * np.sin(theta)

# create subplot
fig, ax = plt.subplots()

(line,) = plt.plot(x, y)

plt.subplots_adjust(left=0.25, bottom=0.25)

ax_n = plt.axes([0.25, 0.1, 0.65, 0.03])

ax_d = plt.axes([0.25, 0.15, 0.65, 0.03])

n_slider = Slider(
    ax=ax_n,
    label="n value",
    valmin=1,
    valmax=7,
    valinit=n,
    valstep=0.5
    )

d_slider = Slider(
    ax=ax_d,
    label="d value",
    valmin=1,
    valmax=9,
    valinit=n,
    valstep=0.5
    )

def update(val):
    d = d_slider.val
    n = n_slider.val
    k = (n / d)
    r = np.cos(k * theta)
    x = r * np.cos(theta)
    y = r * np.sin(theta)
    line.set_xdata(x)
    line.set_ydata(y)
    fig.canvas.draw_idle()
    return val

n_slider.on_changed(update)
d_slider.on_changed(update)

ax.axis("off")
plt.show()
