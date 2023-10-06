from ponto import Ponto

"""
Coordenada da matriz em (x, y)
"""
coordenada = tuple[int, int]

"""
Matriz do problema
"""
matriz = list[list[int]]


class ManipuladorListas:
    lista_aberta: list[Ponto]
    lista_fechada: list[Ponto]
    origem: coordenada
    destino: coordenada
    plano: matriz


    def __init__(self, plano: matriz, origem: coordenada, destino: coordenada):
        self.plano = plano
        self.lista_aberta=[]
        self.lista_fechada=[]
        self.origem = origem
        self.destino = destino
        ponto_inicial=Ponto(origem, plano)
        ponto_inicial.predecessor=None
        self.lista_aberta.append(ponto_inicial)
        self.adicionar_pontos_adjacentes(self.lista_aberta[0])

    def ordenar(self) -> None:
        self.lista_aberta.sort(key=lambda ponto: ponto.calcular_f(self.origem, self.destino))

    def mandar_para_lista_fechada(self, coordenada_ponto: coordenada):
        elemento = list(filter(lambda elemento: elemento.coordenadas == coordenada_ponto, self.lista_aberta))[0]
        self.lista_aberta.remove(elemento)
        self.lista_fechada.append(elemento)
    
    def adicionar_pontos_adjacentes(self, ponto: Ponto):
        self.lista_aberta.extend(ponto.rastrear_pontos_proximos(self.plano))
        self.mandar_para_lista_fechada(ponto.coordenadas)
        self.ordenar()

    def destino_esta_na_lista_fechada(self) -> bool:
        return self.destino not in list(map(lambda ponto: ponto.coordenadas, self.lista_fechada)) 
