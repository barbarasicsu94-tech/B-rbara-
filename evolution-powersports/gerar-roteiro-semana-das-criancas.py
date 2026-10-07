# -*- coding: utf-8 -*-
import os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from honey_template import montar

RAIZ = os.path.dirname(os.path.abspath(__file__))
CLIENTE = u"Evolution Power Sports"

PAGINAS = [
 (u"ROTEIRO REELS | EVOLUTION POWER SPORTS",
  u"Vertical (9:16) | Até 40 segundos", CLIENTE, [

  ("01", u"",
   u"Apresentador(a) ao lado de um dos quadriciclos infantis, olhando diretamente para a "
   u"câmera.",
   [(u"ON:", u"A Semana das Crianças chegou! E que tal transformar essa data em uma aventura "
             u"inesquecível?")]),

  ("02", u"",
   u"Takes dos quadriciclos seminovos disponíveis, mostrando diferentes ângulos e "
   u"modelos.",
   [(u"OFF:", u"Aqui na Evolution Power Sports você encontra quadriciclos infantis seminovos, "
              u"perfeitos para quem quer começar a viver novas aventuras!")]),

  ("03", u"",
   u"Close nos pneus, guidão, banco e acabamento dos quadriciclos, valorizando os detalhes.",
   [(u"OFF:", u"São opções para quem busca diversão e momentos especiais sobre "
              u"quatro rodas!")]),

  ("04", u"",
   u"Apresentador(a) retorna em cena, próximo aos quadriciclos.",
   [(u"ON:", u"E o melhor: eles estão disponíveis aqui na loja, esperando por você!")]),

  ("05", u"",
   u"Apresentador(a) olhando diretamente para a câmera. No encerramento, cortes rápidos "
   u"dos quadriciclos e entrada da logo.",
   [(u"ON:", u"Aqui na Evolution Power Sports, a aventura não tem idade! Chame um dos nossos "
             u"vendedores no direct e garanta já o seu quadriciclo!")]),
 ], False, u"Semana das Crianças – Quadriciclos Infantis Seminovos"),
]

montar(PAGINAS, u"Roteiro de Gravação — Evolution Power Sports | Semana das Crianças",
       os.path.join(RAIZ, "roteiro-semana-das-criancas.html"))
