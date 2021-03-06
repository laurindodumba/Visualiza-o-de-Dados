# -*- coding: utf-8 -*-
"""Visualização De Dados.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/gist/laurindodumba/c4762f035719be7465ea5a3e3493d7ac/visualiza-o-de-dados.ipynb
"""

pip install matplotlib

import matplotlib.pyplot as plt

x1 = [1,2, 3, 4, 15]
y1 = [2,3, 6, 7, 11]

x2 = [3,5, 7,9,8]
y2 = [4,6,8,9,3,]
titulo = "Gráfico de barras"
eixox = "Eixo X"
eixoy = "Eixo Y"

#Legendas
plt.title("Scatter: gráfico")
plt.xlabel(eixox)
plt.ylabel(eixoy)

#Eixos
plt.xlabel("Eixo X")
plt.ylabel("Eixo Y")


plt.scatter(x,y, label="Meus pontos",  color = "r", marker="*", s=100)
plt.plot(x,y)
plt.show()



