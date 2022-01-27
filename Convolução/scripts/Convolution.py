# %%
import numpy as np
from pylab import *

def impulso(n):
    #return 1 if n==0 else 0
    return np.where(n==0, 1, 0)

###########################################

def grafico_divido(dominio, impulso, entrada, resp_impulso, sinal_conv):
    fig, ((g1,g2),(g3,g4)) = plt.subplots(2, 2, num=10)
    
    g1.stem(dominio, impulso, "k-", "ko", "k-")
    g1.set_title("$\delta[n]$")
    g1.set_xlabel('n')

    g2.stem(dominio, entrada, "k-", "ko", "k-")
    g2.set_title("$x[n]$")
    g2.set_xlabel('n')

    g3.stem(dominio, resp_impulso, "k-", "ko", "k-")
    g3.set_title("$h[n]$")
    g3.set_xlabel('n')

    g4.stem(dominio, sinal_conv, "k-", "ko", "k-")
    g4.set_title("$y[n]$")
    g4.set_xlabel('n')

    subplots_adjust(top=1.2,hspace=0.5)
    show()   

def grafico_impulso(dominio, impulso):
    fig, g1 = plt.subplots(1,1)
    g1.stem(dominio, impulso, "k-", "ko", "k-")
    g1.set_title("$\delta[n]$")
    g1.set_xlabel('n')
    show()

def grafico_entrada(dominio, entrada):
    fig, g1 = plt.subplots(1,1)
    g1.stem(dominio, entrada, "k-", "ko", "k-")
    g1.set_title("$x[n]$")
    g1.set_xlabel('n')
    show()

def grafico_respImp(dominio, respImp):
    fig, g1 = plt.subplots(1,1)
    g1.stem(dominio, respImp, "k-", "ko", "k-")
    g1.set_title("$h[n]$")
    g1.set_xlabel('n')
    show()

def grafico_sinalConv(dominio, sinalConv):
    fig, g1 = plt.subplots(1,1)
    g1.stem(dominio, sinalConv, "k-", "ko", "k-")
    g1.set_title("$y[n]$")
    g1.set_xlabel('n')
    show()
