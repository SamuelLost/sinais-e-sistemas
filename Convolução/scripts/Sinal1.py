from Convolution import *
#Sinal de entrada
def entrada(n):
    return impulso(n+2) + impulso(n+1) + impulso(n) + impulso(n-1) + impulso(n-2)

#Resposta ao impulso h[n]
def h(n):
    return 3*impulso(n+1) + 2*impulso(n) + impulso(n-1)

n = np.arange(-5,7) # Intervalo -5 <= n < 7

# Resposta da convolução
y = h(n) + h(n-1) + h(n-2)+ h(n-3)

x = entrada(n)
resp_imp = h(n)
delta = impulso(n)
grafico_divido(n, delta, x, resp_imp, y)
# grafico_impulso(n, delta)
# grafico_entrada(n, x)
# grafico_respImp(n, resp_imp)
# grafico_sinalConv(n, y)