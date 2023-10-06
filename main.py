from listas import ManipuladorListas
from ponto import Ponto


matriz=[
    [1, 1, 1, 1, 1, 1],
    [1, 1, 0, 1, 1, 1],
    [1, 1, 0, 0, 1, 1],
    [1, 1, 1, 1, 1, 1]
]

handler=ManipuladorListas(matriz, (1, 0), (5, 3))

while handler.destino_esta_na_lista_fechada():
    handler.adicionar_pontos_adjacentes(handler.lista_aberta[0])

caminho: list[Ponto]=[]

ponto_atual=handler.lista_fechada[-1]

while ponto_atual.predecessor != None:
    caminho.append(ponto_atual)
    ponto_atual = ponto_atual.predecessor

caminho.reverse()

print(f'Caminho: ')
for ponto in caminho:
    print(f'(x: {ponto.coordenadas[0]}, y: {ponto.coordenadas[1]})')

print(f'Distancia (Manhattan): {len(caminho)}')