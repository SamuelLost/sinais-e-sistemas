from Convolution import *

#Sinal de entrada
def entrada(n):
    return 0.5*impulso(n) + 2*impulso(n-1)

#Resposta ao impulso h[n]
def h(n):
    return impulso(n) + impulso(n-1) + impulso(n-2)

n = np.arange(-2, 5) # Intervalo -2 <= n < 5

# Resposta da convolução
y = entrada(0)*h(n) + entrada(1)*h(n-1)

x = entrada(n)
resp_imp = h(n)
delta = impulso(n)
grafico_divido(n, delta, x, resp_imp, y)
# grafico_impulso(n, delta)
# grafico_entrada(n, x)
# grafico_respImp(n, resp_imp)
# grafico_sinalConv(n, y)


