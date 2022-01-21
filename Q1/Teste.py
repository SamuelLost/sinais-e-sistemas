from SignalDecomposition import *
import numpy as np

x = np.cos(np.pi * np.arange(-3,3))
n0 = -3
dominio, y_input, par, impar = decompose(x, n0)
graph(dominio, y_input, par, impar)