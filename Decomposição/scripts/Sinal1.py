from SignalDecomposition import *
import numpy as np
# # Teste 1 - Sinal ímpar
# 
# ### Sinal 1: $x[n] = \sin \left(\dfrac{n\pi}{2}\right)$

# %%


n = np.arange(-5,6)
x = np.sin((n * np.pi)/2) #Função definida entre -5 e 5

#Intervalo inicial
n0 = n[0]
dominio, original_expandido, par, impar = decompor_sinal(x, n0)
grafico_dividido(dominio, original_expandido, par, impar)

#Pode ser plotado separadamente 
# grafico_original(dominio, original_expandido)
# grafico_par(dominio, par)
# grafico_impar(dominio, impar)
# grafico_soma(dominio, par+impar)