#3- O software também deverá possuir um método que realize a contagem dos votos, ao final da votação um resumo de quantos votos cada candidato e quantos votos nulos ocorreram.
from candidato import Candidato as C
from voto import Voto as V

class Eleicao(V):

 def __init__(self):
   pass

 def contagem(self):
   self.listaNV = []
   self.listaNC = []
   d = len(self.listaVnulo)
   
   for dado in self.listaV:
     if type(dado) == int:
       self.listaNV.append(dado)

   for i in self.listaCandidato:
     if type(i) == int:
       self.listaNC.append(i)

   for politico in self.listaNC:
     print(f'Número do candidato : {politico} recebeu: {self.listaNV.count(politico)} voto(s);')

   print(f'Votos nulos: {d}')