# autores:
# Maria Eduarda Lopes Parnaíba
# Livia Alencar de Souza
# Matheus Alessander Cartaxo Pereira
# Ryan Manuel de Sousa
# Maria Eduarda Leite Trajano


#1. O software deverá armazenar uma lista de candidatos, onde cada candidato possuí um nome, um partido político e um número;
#2. Não se pode adicionar candidatos com mesmo número, pode até ter nomes iguais, mesmo partido, mas não mesmo número;

class Candidato:
 listaNumero = []
 listaCandidato = []
  
 def __init__(self):
   pass
   
 def listas(self, nome, partido, numero):
   self.nome = nome
   self.partido = partido
   self.numero = numero
   self.listaNumero.append(self.numero)
   a = self.listaNumero.count(self.numero)

   if a == 1:
    self.listaCandidato.append(self.nome)
    self.listaCandidato.append(self.partido)
    self.listaCandidato.append(self.numero)
    print("Sua candidatura foi registrada com sucesso")

   else:
     print("Esse número já está sendo utilizado por outro candidato, por favor escolher outro número.")

 def lCandidatos(self):
   return self.listaCandidato