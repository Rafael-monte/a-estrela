class Ponto:
    pass

class Ponto:
    coordenadas: tuple[int, int]
    valor: int
    predecessor: Ponto
    def __init__(self, coordenadas: tuple[int, int], matriz: list[list[int]]):
        self.coordenadas=coordenadas
        self.valor=matriz[coordenadas[1]][coordenadas[0]]

    def rastrear_pontos_proximos(self, matriz: list[list[int]]) -> list[Ponto]:
        pontos_proximos=[]
        pontos_proximos.extend(self.__buscar_pontos_em_x(matriz))
        pontos_proximos.extend(self.__buscar_pontos_em_y(matriz))
        for ponto in pontos_proximos:
            ponto.predecessor=self
        return pontos_proximos
    
    def __buscar_pontos_em_x(self, matriz:list[list[int]]) -> list[Ponto]:
        pontos_proximos=[]
        if self.coordenadas[0] > 0:
            coord = (self.coordenadas[0] - 1, self.coordenadas[1])
            valor= matriz[self.coordenadas[0] - 1][self.coordenadas[1]]
            if valor == 1:
                pontos_proximos.append(Ponto(coord, valor))
        if self.coordenadas[0] < len(matriz[self.coordenadas[1]]) - 1:
            coord = (self.coordenadas[0] + 1, self.coordenadas[1])
            valor= matriz[self.coordenadas[1]][self.coordenadas[0]+1]
            if valor == 1:
                pontos_proximos.append(Ponto(coord, valor))
        return pontos_proximos
    
    def __buscar_pontos_em_y(self, matriz:list[list[int]]) -> list[Ponto]:
        pontos_proximos=[]
        if self.coordenadas[1] > 0:
            coord = (self.coordenadas[0], self.coordenadas[1] - 1)
            valor= matriz[self.coordenadas[1]][self.coordenadas[0] - 1]
            if valor == 1:
                pontos_proximos.append(Ponto(coord, valor))
        if self.coordenadas[1] < len(matriz[self.coordenadas[1]]) - 1:
            coord = (self.coordenadas[0], self.coordenadas[1] + 1)
            valor= matriz[self.coordenadas[1]][self.coordenadas[0] + 1]
            if valor == 1:
                pontos_proximos.append(Ponto(coord, valor))
        return pontos_proximos
    
    def calcular_distancia_ponto(self, coordenadas: tuple[int, int]) -> int:
        distancia_x=abs(self.coordenadas[0] - coordenadas[0])
        distancia_y=abs(self.coordenadas[1] - coordenadas[1])
        return distancia_x+distancia_y

    def calcular_f(self, coordenada_origem: tuple[int, int], coordenada_destino: tuple[int, int]) -> int:
        return self.calcular_distancia_ponto(coordenada_origem)+self.calcular_distancia_ponto(coordenada_destino)