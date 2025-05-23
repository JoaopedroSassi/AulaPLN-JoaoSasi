# -*- coding: utf-8 -*-
"""Aula 05 - 14/03.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1Go_PlJz3Y_RZ4wSXtBWurZ4Z7tUfsd-n

# Aula 5

## 1 - Desenvolvimento conceitual - Corporas

### Inicio do processamento do corpus
"""

def ler(nome_arquivo):
  arquivo = open(nome_arquivo, 'r', encoding='utf-8')
  conteudo_arquivo = arquivo.read()
  arquivo.close()
  return conteudo_arquivo

texto = ler('/content/drive/MyDrive/FatecMaua/6_Sem/ProcessamentoLinguagemNatural/2025.05 Ubirajara.txt')
print(len(texto))

"""### Buscador de palavras"""

def buscador(alvo, texto):
  texto = texto.replace('\n', ' ')
  texto = texto.replace('\t', ' ')

  ocorrencias = []
  encontrado_aqui = texto.find(alvo, 0)

  while encontrado_aqui > 0:
    pos_inicial = encontrado_aqui - (40 - len(alvo))
    trecho = texto[pos_inicial: pos_inicial + 80]

    ocorrencias.append(trecho)

    encontrado_aqui = texto.find(alvo, encontrado_aqui + 1)

  return ocorrencias

resultados = buscador(' peito ', texto)
for trecho in resultados:
  print(trecho)

"""### Limpeza dos corpus"""

palavras = texto.split()

def limpar(lista):
  lixo = '.,:;?!"`()[]{}/\|@#$%"&*-'
  quase_limpo = [x.strip(lixo).lower() for x in lista]
  return [x for x in quase_limpo if x.isalpha() or '-' not in x]

teste = "Corre-se atras do carro, corre se o carro for embora."
word = teste.split()

print(word)
print(limpar(word))

print(len(palavras) )
palavras = limpar(palavras)
print(len(palavras) )

"""## 2 -Demonstração de Estruturas Funcionais

### EX 1 - POS Tagging com Spacy
"""

#!pip install spacy
#!python -m spacy download pt_core_news_sm

import spacy
nlp = spacy.load("pt_core_news_sm")

frase = input("Insira uma frase, gramaticalmente correta: ")
doc = nlp(frase)

for token in doc:
  print(f"{token.text} -> {token.pos_}")

"""### EX 2 - POS Tagging com NLTK (EN)"""

#!pip install nltk
#nltk.download("averaged_perceptron_tagger_eng")
#nltk.download('punkt_tab')

import nltk

frase = input("Insira uma frase, coerente: ")
tokens = nltk.word_tokenize(frase)

pos_tags = nltk. pos_tag(tokens)

for palavra, classe in pos_tags:
  print(f'{palavra}->{classe}')

"""### EX 3 - Parsing de Dependência com spacy"""

import spacy

nlp = spacy. load('pt_core_news_sm' )

frase = "0 gato preto dorme na cadeira"
doc = nlp(frase)

for token in doc:
  print(f"{token.text} -> {token.dep_} -> {token.head.text}")

"""### EX 4 - Análise de Dependências com Spacy"""

import spacy
from spacy import displacy

nlp = spacy.load('pt_core_news_sm' )

frase = "O gato preto dorme na cadeira."
doc = nlp(frase)

displacy.render(doc, style='dep', jupyter=True)

"""### EX 5 - Análise de Constituência com NLTK"""

import nltk
from nltk import Tree

sintaxe = Tree('S', [
  Tree('NP', [Tree('DET', ['O']), Tree('N', ['gato'])]),
  Tree('VP', [Tree('V', ['dorme']),
              Tree('PP', [Tree('P',['na']), Tree('NP',[Tree('N', ['cadeira'])])])])
])

sintaxe.pretty_print()