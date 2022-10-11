#Além dos dados dos candidatos, o software deverá permitir que os eleitores votem em um determinado candidato. Para isso, deverá ser criado um método "votar", que irá receber o número do candidato e o CPF do eleitor. 
#O método deverá validar se o número do candidato existe e se o CPF já votou, caso não exista o número do candidato, esse voto deverá ser contabilizado como voto nulo, se o CPF já tenha votado, não contabilizar o voto e informar que ele já votou. O software deverá armazenar cada voto em uma lista de votos, onde cada voto deverá conter o dado do candidato que foi votado, o cpf do eleitor;
from candidato import Candidato as C

class Voto(C):
  listaVnulo = []
  listaCPF = []
  listaV = []
  def __init__(self):
    pass

  def votar(self, nCandidato, CPF):
    self.nCandidato = nCandidato
    self.CPF = CPF
    self.listaCPF.append(self.CPF)
    c = self.listaCPF.count(self.CPF)
    
    if c == 1:
      print("Em analise...")
    else:
      print("Esse CPF já votou, não e permitido votar duas vezes.")

    self.listaNumero.append(self.nCandidato)
    b = self.listaNumero.count(self.nCandidato)

    if b == 1:
      self.listaVnulo.append(self.CPF)
      print("O número informado não existe, seu voto foi registrado como nulo.")
      
    elif b != 1 and c != 1:
      print("Voto invalido")
    
    else:
      self.listaV.append(self.nCandidato)
      self.listaV.append(self.CPF)
      print("Seu voto foi registrado.")