# coding=utf-8
from collections import Counter

class Robo:
  def __init__(self, x):
    self.perguntas = []
    self.respostas = []
    self.vencedores = []

    self.mount(x)

  def __iter__(self):
      return self

  def mount(self, x):
    bloco = 1
    lastquestion = None

    for index, y in enumerate(x):
      q = y.replace("SE ", "").split("ENTÃO ")
      j = {}
      j['sentenca'] = y
      j['pergunta'] = q[0]
      j['resposta'] = q[1]
      j['show'] = True

      # Verifica se a ultima pergunta e igual a atual
      # se for atual o bloco permanece o mesmo
      # se alterar o bloco sera incrementado
      if lastquestion:
        if j['pergunta'] != lastquestion:
          bloco += 1
      
      # Seta o bloco
      j['bloco'] = bloco

      # Guarda a ultima pergunta para comparar e montar o bloco
      lastquestion = j['pergunta']

      # Adiciona pergunta na lista
      self.perguntas.insert(0, j)


  # Verifica se existem perguntas a serem feitas
  def hasQuestions(self):  
    for x in self.perguntas:
      if x['show'] == True:
        return True

    return False

  # Faz uma que esteja disponivel para o usuario
  def question(self):
    for idx, x in enumerate(self.perguntas):
      if x['show'] is True:
        return x
        break

  def answer(self, pergunta, resposta):
    # Caso tenha respondido 1
    if int(resposta) is 1:
      # Adiciona resposta na lista de respostas
      self.respostas.insert(0, pergunta['resposta'])

    # Desativa todas as perguntas de um determinado bloco
    self.destativaBloco(pergunta['bloco'])

  def destativaBloco(self, bloco):
    for idx, x in enumerate(self.perguntas):
      if int(x['bloco']) is int(bloco):
        self.perguntas[idx]['show'] = False
        
  def getWinner(self):
    return Counter(self.respostas)
