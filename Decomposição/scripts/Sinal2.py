from SignalDecomposition import *


n = np.arange(-5,6)
x = np.exp(np.cos(n * np.pi))

n0 = n[0]

dominio, original_expandido, par, impar = decompor_sinal(x, n0)
grafico_dividido(dominio, original_expandido, par, impar)

#Pode ser plotado separadamente 
# grafico_orginal(dominio, original_expandido)
# grafico_par(dominio, par)
# grafico_impar(dominio, impar)
# grafico_soma(dominio, par+impar)