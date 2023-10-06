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
       
        pontos_proximos.extend(self.__buscar_pontos_em_y(matriz))
        pontos_proximos.extend(self.__buscar_pontos_em_x(matriz))
        for ponto in pontos_proximos:
            ponto.predecessor=self
        return pontos_proximos
    
    def __buscar_pontos_em_x(self, matriz:list[list[int]]) -> list[Ponto]:
        pontos_proximos=[]
        coordenada_x=self.coordenadas[0]
        coordenada_y=self.coordenadas[1]
        tamanho_linha_matriz=len(matriz[0])
        # Procurando para a direita
        if coordenada_x < tamanho_linha_matriz - 1:
             coordenadas_ponto_a_direita=(coordenada_x + 1, coordenada_y)
             valor_ponto=matriz[coordenadas_ponto_a_direita[1]][coordenadas_ponto_a_direita[0]]
             if valor_ponto == 1:
                  pontos_proximos.append(Ponto(coordenadas_ponto_a_direita, matriz))

        # Procurando a esquerda        
        if coordenada_x > 0:
             coordenadas_ponto_a_esquerda=(coordenada_x - 1, coordenada_y)
             valor_ponto=matriz[coordenadas_ponto_a_esquerda[1]][coordenadas_ponto_a_esquerda[0]]
             if valor_ponto == 1:
                  pontos_proximos.append(Ponto(coordenadas_ponto_a_esquerda, matriz))
        return pontos_proximos
    
    def __buscar_pontos_em_y(self, matriz:list[list[int]]) -> list[Ponto]:
        pontos_proximos=[]
        coordenada_x=self.coordenadas[0]
        coordenada_y=self.coordenadas[1]
        numero_linhas_matriz=len(matriz)
        # Procurando para cima
        if coordenada_y > 0:
                coordenadas_ponto_superior=(coordenada_x, coordenada_y - 1)
                valor_ponto=matriz[coordenadas_ponto_superior[1]][coordenadas_ponto_superior[0]]
                if valor_ponto == 1:
                    pontos_proximos.append(Ponto(coordenadas_ponto_superior, matriz))
        
        # Procurando para baixo
        if coordenada_y < numero_linhas_matriz - 1:
                coordenadas_ponto_inferior=(coordenada_x, coordenada_y + 1)
                valor_ponto=matriz[coordenadas_ponto_inferior[1]][coordenadas_ponto_inferior[0]]
                if valor_ponto == 1:
                    pontos_proximos.append(Ponto(coordenadas_ponto_inferior, matriz))
        return pontos_proximos
    
    def calcular_distancia_ponto(self, coordenadas: tuple[int, int]) -> int:
        distancia_x=abs(self.coordenadas[0] - coordenadas[0])
        distancia_y=abs(self.coordenadas[1] - coordenadas[1])
        return distancia_x+distancia_y

    def calcular_f(self, coordenada_origem: tuple[int, int], coordenada_destino: tuple[int, int]) -> int:
        return self.calcular_distancia_ponto(coordenada_origem)+self.calcular_distancia_ponto(coordenada_destino)