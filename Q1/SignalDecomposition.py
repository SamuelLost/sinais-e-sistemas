# %%
import numpy as np
import matplotlib.pyplot as plt
from math  import *
from numpy import *
from pylab import *

def expand(dom_y, n0, yn):
    # Domínio original do sinal de entrada.
    domino = range(n0, n0 + len(yn))

    y_expanded = np.zeros(len(dom_y))

    # Para cada novo elemento  do contra-domínio extendido, temos que verificar
    # se este elemento existe no domínio original. Se existir, devemos mapeá-lo
    # à saída original, caso contrário, a saída permanecerá zero.
    for i, n in enumerate(dom_y):
        try:
            y_expanded[i] = yn[domino.index(n)]
        except ValueError:
            pass

    return y_expanded

def grafico_soma(dominio, sinal):
    fig = figure(1)
    #fig.set_size_inches((8., 8.))

    # Cria as funções a serem plotadas.
    # Plotando o sinal par + ímpar.
    a =  fig.add_subplot()
    a.stem(dominio, sinal, "k-", "ko", "k-")
    #a.set_xlim([-4., 4.])
    #a.set_ylim([-4, 4])
    a.set_xlabel('n')
    a.set_title("$x_{par}[n] + x_{ímpar}[n]$ ")
    a.set_xticks(dominio)
    plt.show()

def grafico_impar(dominio, sinal):
    fig = plt.figure(1)
    #fig.set_size_inches((8., 8.))

    # Cria as funções a serem plotadas.
    # Plotando o sinal par + ímpar.
    b =  fig.add_subplot()
    b.stem(dominio, sinal, "k-", "ko", "k-")
    #a.set_xlim([-4., 4.])
    #b.set_ylim([-1, 1])
    b.set_xlabel('n')
    b.set_title("$x_{ímpar}[n]$ ")
    b.set_xticks(dominio)
    plt.show()

def grafico_par(dominio, sinal):
    fig = plt.figure(1)
    #fig.set_size_inches((8., 8.))

    # Cria as funções a serem plotadas.
    # Plotando o sinal par + ímpar.
    b =  fig.add_subplot()
    b.stem(dominio, sinal, "k-", "ko", "k-")
    #a.set_xlim([-4., 4.])
    #a.set_ylim([-4, 4])
    b.set_xlabel('n')
    b.set_title("$x_{par}[n]$ ")
    b.set_xticks(dominio)
    plt.show()

def grafico_orginal(dominio, sinal):
    fig = plt.figure(1)
    #fig.set_size_inches((8., 8.))

    # Cria as funções a serem plotadas.
    # Plotando o sinal par + ímpar.
    b =  fig.add_subplot()
    b.stem(dominio, sinal, "k-", "ko", "k-")
    #a.set_xlim([-4., 4.])
    #a.set_ylim([-4, 4])
    b.set_xlabel('n')
    b.set_title("$x[n]$")
    b.set_xticks(dominio)
    plt.show()

def graph(domino, orig, even, odd):
    

    # Divide a janela de plotagem em quatro regiões.
    fig, ((ax1,ax2),(ax3,ax4)) = plt.subplots(2, 2, num=10)

    ax1.stem(domino, orig, "k-", "ko", "k-")
    ax1.set_title('Sinal de Entrada')
    
    ax2.stem(domino, even, "k-", "ko", "k-")
    ax2.set_title('Parte Par')

    ax3.stem(domino, odd, "k-", "ko", "k-")
    ax3.set_title('Parte Impar')

    ax4.stem(domino, (odd + even), "k-", "ko", "k-")
    ax4.set_title('Soma das Partes')
    plt.subplots_adjust(hspace=0.5)

    plt.show()

def decompose(yn, n0):
    #dom_y = np.arange(n0, (n0 + 5))
    raio = max(abs(n0), abs(n0 + len(yn) - 1))
    dom_y = np.arange(-raio, raio+1)
    y_input = expand(dom_y, n0, yn)
    y_negativo = y_input[::-1]

    y_par = 0.5 * (y_input + y_negativo)
    y_impar = 0.5 * (y_input - y_negativo)

    return (dom_y, y_input, y_par, y_impar)



