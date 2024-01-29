# -*- coding: utf-8 -*-
"""App.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1TLYXWFfqeOZldPdYwC73xVJt9hygFQPf
"""

import pandas as pd
import numpy as np
import seaborn
import scipy

dados = pd.read_csv('dados.csv') # Leitura dos dados
type(dados)
dados.head() #Mostrar os primeiros dados

#Variáveius qualitativas ordinais
sorted(dados['Anos de Estudo'].unique()) #Pegar apenas os valores e sort para deixar ordenados

#Variáveis qualitativas nominais
sorted(dados['UF'].unique())

#Variáveis qualitativas nominais
sorted(dados['Sexo'].unique())

#Variáveis qualitativas nominais
sorted(dados['Cor'].unique())

#Variáveis quantitativas discretas
sorted(dados['Idade'].unique())
print('De %s até %s anos ' % (dados.Idade.min(), dados.Idade.max()))

#Variáveis quantitativas continuas
print('De %s até %s metros' % (dados.Altura.min(), dados.Altura.max()))