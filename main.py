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
  
  while not r.isdigit():
    print "Você deve responder com um numero!"
    
    r = raw_input("%s ? (0 ou 1): " % perg['pergunta']) 
  
  # Responde a questao  
  p.answer(perg, r)

print p.getWinner()
