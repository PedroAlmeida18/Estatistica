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

#Distribuição de Frequências para variaveis qualitativas
#Obs: Foram considerados somente os regristros das pessoas de referência de cada domicílio, 0 para Masc e 1 para Fem
dados['Sexo'].value_counts()

#Colocar em percentual
dados['Sexo'].value_counts(normalize=True) *100

frequencia = dados['Sexo'].value_counts()
percentual = dados['Sexo'].value_counts(normalize=True) *100
#CRIAÇÃO DE UMA TABELA PARA MOSTRARA MEHLOR ESSES DADOS
dis_freq_qualitativas = pd.DataFrame({'Frequência ' : frequencia, 'Porcentagem (%)' : percentual})
dis_freq_qualitativas

#Renomear para saber Masculino e Feminino
dis_freq_qualitativas.rename(index={0:'Masculino ', 1:'Feminino'}, inplace=True ) # Salvar essa alteração
dis_freq_qualitativas.rename_axis('Sexo', axis='columns', inplace = True)
dis_freq_qualitativas

#Método 2 para tabela de frequencia
sexo = { 0 : 'Masculino',
         1: 'Feminino'}
cor = { 0 : 'Indígena',
        2: 'Branca',
        4: 'Preta',
        6: 'Amarela',
        8:'Parda',
        9 : 'Sem declaração'}

frequencia = pd.crosstab(dados.Sexo,dados.Cor)
frequencia.rename(index=sexo,inplace=True)  #Modificar a linha
frequencia.rename(columns=cor, inplace=True) #Modificar o nome das colunas
frequencia

percentual_2= pd.crosstab(dados.Sexo,dados.Cor, normalize=True) *100 #DEIXAR EM PORCENTAGEM
percentual_2.rename(index=sexo,inplace=True)  #Modificar a linha
percentual_2.rename(columns=cor, inplace=True) #Modificar o nome das colunas
percentual_2

#Calcular a renda média das pessoas por sexo e cor,  Conseguir dados de maneira especifica
percentual_3 =pd.crosstab(dados.Sexo,dados.Cor,aggfunc='mean' , values = dados.Renda)
percentual_3.rename(index=sexo,inplace=True)  #Modificar a linha
percentual_3.rename(columns=cor, inplace=True) #Modificar o nome das colunas
percentual_3

#Distribuição de freq para variaveis quantitativas (classes personalizadas)
#Forma de classificar elas, classificar as rendas das pessoas em classes de acordo com dataste de 2015
dados.Renda.min()
dados.Renda.max()

dados.head() #IMPRIMIR OS 5 PRIMEIROS

classes=[0,1576,3152,7880,15760,200000]
labels = ['E','D','C','B','A']

#Criação da tabela de frequencias
pd.cut(x = dados.Renda, bins=classes,labels=labels,include_lowest=True )

frequencia_Renda = pd.value_counts(
    pd.cut(x = dados.Renda, bins=classes,labels=labels,include_lowest=True )
    ) # Valores absolutos que tem de cada pessoa em cada categoria
frequencia_Renda

# Percentual da Renda
percentual_Renda = pd.value_counts(
    pd.cut(x = dados.Renda, bins=classes,labels=labels,include_lowest=True ), normalize=True
    ) *100
percentual_Renda

dist_freq_quantitativas = pd.DataFrame({'Frequência': frequencia_Renda, 'Porcentagem (%)' : percentual_Renda })
dist_freq_quantitativas.sort_index(ascending=False)

#Distribuuiçao de frequencias para variaveis quantitativas(classe de amplitude fixa)
#Regra de Sturges - Definir o número de classes
n = dados.shape[0]
print(n)
k = 1+(10/3)*np.log10(n)
print(k) #Número de classes ideal para esses dados
k = int(k.round(0))
print(k)



# Criar a tabela de Frequencias, bins ´é o número de classes
frequencia_renda2 = pd.value_counts(
    pd.cut(
        x = dados.Renda, bins=17,include_lowest=True
    ),sort = False
)
frequencia_renda2

percentual_renda2 = pd.value_counts(
    pd.cut(
        x = dados.Renda, bins=17 ,include_lowest=True
    ), normalize = True, sort = False
)
percentual_renda2

dist_quantitativas_amplitudeFixa= pd.DataFrame({'Frequência': frequencia_renda2,
                                                'Porcentagem ($)': percentual_renda2})
dist_quantitativas_amplitudeFixa