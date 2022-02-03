from SignalDecomposition import *
import numpy as np
# ## Teste 3 - Sinal misto
# 
# ### Sinal 3: $x[n] = \sin \left(\dfrac{n\pi}{2}\right) + e^{\cos(n\pi)}$

# %%
n = np.arange(-5,6)
x = np.sin((n * np.pi)/2) + np.exp(np.cos(n * np.pi))

n0 = n[0]

dominio, original_expandido, par, impar = decompor_sinal(x, n0)
grafico_dividido(dominio, original_expandido, par, impar)

#Pode ser plotado separadamente 
# grafico_original(dominio, original_expandido)
# grafico_par(dominio, par)
# grafico_impar(dominio, impar)
# grafico_soma(dominio, par+impar)