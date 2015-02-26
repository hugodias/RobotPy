# coding=utf-8
from robo import Robo

# Faz a leitura do arquivo
with open('regras.txt') as f:
    helper = f.readlines()

# Faz a instancia do robô
p = Robo(helper)

while p.hasQuestions():
  perg = p.question()

  # Faz a pergunta
  r = raw_input("%s ? (0 ou 1): " % perg['pergunta']) 
  
  if r.isdigit():
    p.answer(perg, r)
  else:
    print "Você deve responder com um numero"
  pass

print p.getWinner()
