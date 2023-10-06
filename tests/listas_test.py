import unittest
from listas import ManipuladorListas

class ListasTest(unittest.TestCase):
    def setUp(self) -> None:
        self.matriz=[
            [1, 1, 1, 1, 1, 1],
            [1, 1, 1, 0, 1, 1],
            [1, 0, 1, 1, 1, 1]
        ]
        self.coordenadas_origem=(2, 1)
        self.coordenadas_destino=(5, 1)
        return super().setUp()

    def test_ao_informar_origem_e_destino_deve_mostrar_pontos_proximos_da_origem(self):
        handler= ManipuladorListas(self.matriz, self.coordenadas_origem, self.coordenadas_destino)
        self.assertEqual(
            [(2, 0), (2, 2), (1, 1)],
            list(map(lambda ponto: ponto.coordenadas, handler.lista_aberta))
        )