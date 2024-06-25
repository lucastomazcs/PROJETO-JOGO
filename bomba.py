class Bomba:
    
    def __init__(self, posicaobomba, tempo, raiodeexplosao):
        self.__posicaobomba = posicaobomba
        self.__tempo = tempo
        self.__raiodeexplosao = raiodeexplosao

    @property
    def posicaoBomba(self):
        return self.__posicaobomba
    @property
    def tempo(self):
        return self.__tempo
    @property
    def raio(self):
        return self.__raiodeexplosao
    

