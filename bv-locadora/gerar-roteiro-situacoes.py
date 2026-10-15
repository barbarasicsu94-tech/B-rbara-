# -*- coding: utf-8 -*-
import os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from honey_template import montar

RAIZ = os.path.dirname(os.path.abspath(__file__))
CLIENTE = u"BV Locadora"

PAGINAS = [
 (u"ROTEIRO — BV LOCADORA | SITUAÇÕES DO DIA A DIA",
  u"Reels vertical (9:16) | 30 a 40 segundos", CLIENTE, [

  ("01", u"",
   u"Personagem no escritório da BV Locadora, falando diretamente para a câmera. "
   u"Apoio: carro parado com o capô aberto e alguém saindo a pé para o trabalho, "
   u"de manhã cedo.",
   [(u"(ON):", u"Seu carro resolve dar pane logo no início da semana e você precisa ir "
               u"trabalhar?")]),

  ("02", u"",
   u"Personagem segue no escritório. Apoio: chuva caindo, moto parada coberta e a entrada "
   u"do shopping.",
   [(u"(ON/OFF):", u"Você quer ir pro shopping, está chovendo e você só tem "
                   u"moto?")]),

  ("03", u"",
   u"Personagem no escritório. Apoio: mala sendo fechada, bagageiro do carro e estrada "
   u"aberta.",
   [(u"(ON/OFF):", u"Você precisa viajar e necessita de um veículo?")]),

  ("04", u"",
   u"Personagem no escritório. Apoio: família chegando e cumprimentos, depois pontos "
   u"conhecidos da cidade vistos de dentro do carro.",
   [(u"(ON/OFF):", u"Sua família veio te visitar e você quer turistar na cidade?")]),

  ("05", u"",
   u"Personagem no escritório. Apoio: alguém no celular comparando preços, "
   u"demonstrando cansaço e desistência.",
   [(u"(ON/OFF):", u"Você passou por todas as situações e ainda não achou um "
                   u"local rápido e com preços acessíveis que cabem no seu bolso?")]),

  ("06", u"",
   u"Personagem no escritório, agora em tom de solução. Apoio: fachada da BV "
   u"Locadora, frota e a chave sendo entregue. Encerra com a logo.",
   [(u"(ON):", u"Calma, aqui na BV Locadora você encontra tudo isso.")]),
 ], 1, (u"Personagem", u"Apresentadora, no escritório da BV Locadora")),
]

montar(PAGINAS, u"Roteiro de Gravação — BV Locadora | Situações do Dia a Dia",
       os.path.join(RAIZ, "roteiro-situacoes.html"))
