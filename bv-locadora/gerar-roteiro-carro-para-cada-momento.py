# -*- coding: utf-8 -*-
import os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from honey_template import montar

RAIZ = os.path.dirname(os.path.abspath(__file__))
CLIENTE = u"BV Locadora"

PAGINAS = [
 (u"ROTEIRO — BV LOCADORA | O CARRO PARA CADA MOMENTO",
  u"Reels vertical (9:16) | 30 a 40 segundos", CLIENTE, [

  ("01", u"",
   u"Personagem na BV Locadora, em frente aos veículos, falando diretamente para a "
   u"câmera.",
   [(u"(ON):", u"Você sabia que existe um carro ideal para cada momento da sua rotina? "
               u"E aqui na BV Locadora você encontra várias opções!")]),

  ("02", u"",
   u"Personagem ao lado de um carro compacto. Intercalar a apresentação com imagens em "
   u"OFF dos detalhes do veículo.",
   [(u"(ON/OFF):", u"Pra quem vive na correria do dia a dia, um carro compacto é a escolha "
                   u"certa! Prático, econômico e ideal pra se movimentar pela cidade."),
    (u"LETTERING:", u"Praticidade para sua rotina.")]),

  ("03", u"",
   u"Personagem apresenta um veículo maior, como um SUV, e em seguida uma picape. "
   u"Intercalar com imagens em OFF dos veículos.",
   [(u"(ON/OFF):", u"Agora, se você precisa de mais espaço e conforto, temos "
                   u"opções maiores. E pra quem precisa de força e capacidade de "
                   u"transporte, uma picape pode ser a escolha ideal!"),
    (u"LETTERING:", u"Mais espaço. Mais possibilidades.")]),

  ("04", u"",
   u"Personagem posicionada em frente à fachada da BV Locadora, com veículos ao fundo.",
   [(u"(ON):", u"Seja qual for o seu momento, a BV Locadora tem uma opção pra você! "
               u"Entre em contato, conheça nossa frota e alugue o carro ideal para sua "
               u"rotina!"),
    (u"ENCERRAMENTO:", u"Logo BV Locadora")]),
 ], False, (u"Personagem", u"Apresentadora feminina")),
]

montar(PAGINAS, u"Roteiro de Gravação — BV Locadora | O Carro para Cada Momento",
       os.path.join(RAIZ, "roteiro-carro-para-cada-momento.html"))
