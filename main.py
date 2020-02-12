import pyxel

mapa = [
  [1,1,1,1,1,1,1,1,1,1],
  [1,0,0,0,0,0,0,0,0,1],
  [1,0,0,0,0,0,0,0,0,1],
  [1,0,0,0,0,0,0,0,0,1],
  [1,0,0,0,0,0,0,0,0,1],
  [1,0,0,0,0,0,0,0,0,1],
  [1,0,0,0,0,0,0,0,0,1],
  [1,0,0,0,0,0,0,0,0,1],
  [1,0,0,0,0,0,0,0,0,1],
  [1,1,1,1,1,1,1,1,1,1]
  ]

def gerarMapa(mapa):
  altura = 0
  for x in mapa:
    largura = 0
    for y in x:
      if (y == 1):
        pyxel.rect(largura+20, altura+20, largura, altura, 7)
      if (y == 0):
        pyxel.rect(largura+20, altura+20, largura, altura, 0)
      largura += 20
    altura += 20

class Jogo:
    def __init__(self):
        pyxel.init(200, 200, caption="Gerador de mapa")
        pyxel.run(self.atualizar, self.desenhar)

    def atualizar(self):
      pass

    def desenhar(self):
      gerarMapa(mapa)
Jogo()