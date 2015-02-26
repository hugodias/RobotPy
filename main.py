# coding=utf-8
from robo import Robo

# Faz a leitura do arquivo
with open('regras.txt') as f:
    helper = f.readlines()

# Faz a instancia do robô
p = Robo(helper)

while p.hasQuestions():
  r = "zero"
  perg = p.question()

  while not r.isdigit():
    if r is not "zero":
      print "Você deve responder com um numero!"

    # Recupera a resposta do usuario
    r = raw_input("%s ? (0 ou 1): " % perg['pergunta']) 
  
  # Responde a questao  
  p.answer(perg, r)

print p.getWinner()
