# -*- coding: utf-8 -*-
#   For plotting a diagram of the sinc function
#   Brian Magill
#   3/29/2015
#
#
import numpy as np
import matplotlib.pyplot as plt
#from func_defs import sinc
x = np.linspace(-5., 5., 100)
y = np.sinc(x)

plt.fill(x, y, 'c')
plt.vlines(x, [0], y)
plt.grid(True)
plt.savefig("SincPlot.png")


