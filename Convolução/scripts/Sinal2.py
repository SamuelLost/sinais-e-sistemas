from Convolution import *
#Sinal de entrada
def entrada(n):
    return 1.5*impulso(n+1) + 0.5*impulso(n) + impulso(n-1)

#Resposta ao impulso h[n]
def h(n):
    return 0.5*impulso(n+1) + impulso(n) + 1.5*impulso(n-1)

n = np.arange(-3, 6) # Intervalo -1 <= n < 6

# Resposta da convolução
y = 2*h(n-2) + 2*h(n-1) + h(n) + h(n-1) + h(n-2)

x = entrada(n)
resp_imp = h(n)
delta = impulso(n)
grafico_divido(n, delta, x, resp_imp, y)
# grafico_impulso(n, delta)
# grafico_entrada(n, x)
# grafico_respImp(n, resp_imp)
# grafico_sinalConv(n, y)


