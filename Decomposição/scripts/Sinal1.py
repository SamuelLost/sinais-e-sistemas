from SignalDecomposition import *


n = np.arange(-5,6)
x = np.cos(n * np.pi) #Função definida entre -5 e 5

#Intervalo inicial
n0 = n[0]
dominio, original_expandido, par, impar = decompor_sinal(x, n0)
grafico_dividido(dominio, original_expandido, par, impar)

#Pode ser plotado separadamente 
# grafico_original(dominio, original_expandido)
# grafico_par(dominio, par)
# grafico_impar(dominio, impar)
# grafico_soma(dominio, par+impar)