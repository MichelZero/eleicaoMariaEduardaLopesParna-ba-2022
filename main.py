# autores:
# Maria Eduarda Lopes Parnaíba
# Livia Alencar de Souza
# Matheus Alessander Cartaxo Pereira
# Ryan Manuel de Sousa
# Maria Eduarda Leite Trajano


#Crie um menu do software no main.py
from candidato import Candidato as C
from voto import Voto as V
from eleicao import Eleicao as E

c1 = C()
v1 = V()
e1 = E()

while True:
 
 print('\n - Para se candidatar digite 1'
 '\n - Para acessar a lista de candidatos digite 2'
 '\n - Para votar digite 3'
 '\n - Para visualizar o andamento da eleição digite 4'
 '\n - Para sair digite 5')
        
 m = int(input("O que deseja fazer: "))

 if m == 1:
   n = input("Informe seu nome: ")
   o = input("Informe seu partido: ")
   p = int(input("Informe seu número: "))
   print("Verificando dados...")
   c1.listas(n, o, p)
   
 elif m == 2:
   print(c1.lCandidatos())

 elif m == 3:
   q = int(input("Informe o número do candidato, que você deseja votar:  "))
   r = str(input("Informe o número do seu CPF: "))
   print("Verificando dados...")
   v1.votar(q, r)

 elif m == 4:
  e1.contagem()
   
 elif m == 5: 
   print("saindo do sistema...")
   break

 else:
   print("Caractere informado não valido, por favor digitar um numero de acordo com as intruções acima.")