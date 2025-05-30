# -*- coding: utf-8 -*-
"""Projeto 02 - Joao Pedro Sassi

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1eyczbNYHsVSAz6Gb-KOEQ7lhYM5dE89G

# Projeto 02 - Estatística descritiva aplicada em um corpus
"""

import nltk
from nltk.corpus import machado

nltk.download('machado')

"""## Verificando o conteúdo do Corpus "Machado" e extraindo"""

import zipfile

caminho_do_zip = '/root/nltk_data/corpora/machado.zip'

arquivo_zip = zipfile.ZipFile(caminho_do_zip, 'r')

arquivo_zip.printdir()

import os

pasta_destino = '/root/nltk_data/corpora'

os.makedirs(pasta_destino, exist_ok=True)

arquivo_zip.extractall(pasta_destino)
print(f"Arquivo {caminho_do_zip} extraído com sucesso na pasta {pasta_destino}.")

"""## Passo 2 - Etiquetação morfológica (POS Tagging)"""

!pip install spacy
!python -m spacy download pt_core_news_sm

# Etiquetagem morfológica
import spacy

nlp = spacy.load("pt_core_news_sm")

doc = nlp("Vamos estudar processamento de linguagem natural!")
etiq = [(x.orth_, x.pos_) for x in doc]

print(etiq)

# Funcao para leitura dos arquivos a serem utilizados

def ler(nome_arquivo):
  arquivo = open(nome_arquivo,'r', encoding='ISO-8859-1')
  conteudo_arq = arquivo.read()
  arquivo.close()
  return conteudo_arq

#Obtendo arquivos para análise
obras = []

for i in range(1, 6):
  obras.append('/root/nltk_data/corpora/machado/romance/marm0' + str(i) + '.txt')

for i in range(1, 6):
  obras.append('/root/nltk_data/corpora/machado/cronica/macr0' + str(i) + '.txt')

obras

import statistics as stat

cont_adv = []

for obra in obras:
  print(obra)
  s = ler(obra)

  doc = nlp(s)
  etiq = [(x.orth_, x.pos_) for x in doc]
  adv = [(ort, pos) for (ort, pos) in etiq if pos == "ADV"]
  cont_adv.append(len(adv)/len(etiq))

rom_m = stat.mean(cont_adv[:4])
rom_dp = stat.stdev(cont_adv[:4])
cron_m = stat.mean(cont_adv[5:])
cron_dp = stat.stdev(cont_adv[5:])

"""## Passo 3 - Geração de gráfico para demonstração de resultados"""

import matplotlib.pyplot as plt

tipo_obra = ["Romance", "Cronicas"]

x = [0, 1]
y = [rom_m, cron_m]
dp = [rom_dp, cron_dp]

plt.bar(x, y, yerr = dp)
plt.xticks(x, tipo_obra)
plt.ylabel("Percentual médio de adbérbio (%)")
plt.title("Advérbios nas obras de M.de Assis")

plt.show()

"""## Passo 4 - Análise de classes gramaticais"""

# Limpeza
lixo = ['PUNCT', 'SPACE', 'X', 'SYM', 'NUM']
pos2 = [pos for (pal, pos) in etiq if pos not in lixo]

from collections import defaultdict

cont = defaultdict(int)
for p in pos2:
  cont[p] += 1

nomes = cont.keys()
ocorrencias = cont.values()

plt.pie(ocorrencias, labels=nomes, autopct="%1.1f%%")
plt.axis('equal')

plt.show()