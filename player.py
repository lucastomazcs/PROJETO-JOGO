from bomba import Bomba

class Player(Bomba):
   def __init__(self, posicaobomba, tempo, raiodeexplosao, posicao, vida, velocidade, range_bomba) -> None:
      super().__init__(posicaobomba, tempo, raiodeexplosao)
      self.__posicao = posicao
      self.__vida = vida
      self.__velocidade = velocidade
      self.__range_bomba = range_bomba
    
    
   @property
   def posicao(self):
        return self.__posicao
   @property
   def vida(self):
        return self.__vida
   @property
   def velocidade(self):
        return self.__velocidade
   @property
   def raio(self):
        return self.__range_bomba
