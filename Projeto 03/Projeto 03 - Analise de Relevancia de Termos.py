# -*- coding: utf-8 -*-
"""Projeto 03 - Joao Pedro Sassi.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1zHq4b7r70yH-0bEeMc4DKEoDHngU5Xcx

# Projeto 03 - Análise de Relevância de Termos

## 01. Carregamento do arquivo
"""

import zipfile
import os
import nltk
from nltk.corpus import machado

nltk.download('machado')

caminho_do_zip = '/root/nltk_data/corpora/machado.zip'
pasta_destino = '/root/nltk_data/corpora'
os.makedirs(pasta_destino, exist_ok=True)

arquivo_zip = zipfile.ZipFile(caminho_do_zip, 'r')
arquivo_zip.extractall(pasta_destino)

print(f"Arquivo {caminho_do_zip} extraído com sucesso na pasta {pasta_destino}.")

"""## 02. Limpeza e Preparação do arquivo"""

def ler(nome_arquivo):
  arquivo = open(nome_arquivo,'r', encoding='ISO-8859-1')
  conteudo_arq = arquivo.read()
  arquivo.close()
  return conteudo_arq

def limpar(lista):
  lixo = '.,:;?!"`()[]{}/\|@#$%"&*-'
  quase_limpo = [x.strip(lixo).lower() for x in lista]
  return [x for x in quase_limpo if x.isalpha() or '-' not in x]

obras = []

for i in range(1, 10):
  obras.append('/root/nltk_data/corpora/machado/romance/marm0' + str(i) + '.txt')

colecao = []

for obra in obras:
  print(obra)
  texto = ler(obra)
  palavras = limpar(texto.lower().split())
  colecao.append(palavras)

"""## 03. Criação dos cálculos"""

import math

def tf(termo, doc):
  return colecao[doc].count(termo)

def df (termo):
  return len([d for d in colecao if termo in d])

def idf(termo):
  return math.log10(len(colecao) / df(termo))

def tf_idf(termo, doc):
  return tf(termo, doc) * idf(termo)

"""## 04. Experimentação dos cálculos"""

df('luva')

tf_idf('luva', 2)

def relevantes(doc):
  lista_total = [(tf_idf(p, doc), p) for p in set(colecao[doc])]

  return sorted(lista_total, reverse=True)[:10]

mr = relevantes(1)

mr