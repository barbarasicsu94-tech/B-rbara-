# -*- coding: utf-8 -*-
import os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from honey_template import montar

RAIZ = os.path.dirname(os.path.abspath(__file__))
CLIENTE = u"BV Locadora"

PAGINAS = [
 (u"ROTEIRO — ANIVERSÁRIO DE RORAIMA | BV LOCADORA",
  u"até 30 segundos | 4 cenas", CLIENTE, [
  ("01", u"0s a 7s",
   u"Imagem: Banco de imagens de Roraima, com destaque para a Ponte do Macuxi ao pôr do sol, "
   u"intercalando com outros recortes da cidade/estado.",
   [(u"OFF:", u"Roraima é feito de caminhos, histórias e de gente que segue sempre em frente.")]),
  ("02", u"7s a 14s",
   u"Imagem: Carro da BV Locadora percorrendo uma avenida ou trecho urbano de Boa Vista. "
   u"Takes em movimento, acompanhando o veículo.",
   [(u"OFF:", u"É daqui que partem sonhos, encontros, conquistas e novos destinos todos os dias.")]),
  ("03", u"14s a 22s",
   u"Imagem: Pessoa dirigindo normalmente pela cidade. Takes internos: mãos no volante, olhar "
   u"para a via, detalhes do carro e movimento urbano pelas janelas.",
   [(u"OFF:", u"E para a BV Locadora, é uma alegria fazer parte de tantas jornadas que "
              u"acontecem por aqui.")]),
  ("04", u"22s a 30s",
   u"Imagem: O carro segue pela estrada ou avenida em movimento. Take traseiro ou acompanhamento "
   u"lateral, até o veículo seguir seu caminho. Entra a logo da BV Locadora no encerramento.",
   [(u"OFF:", u"Parabéns, Roraima, por mais um ano de histórias e caminhos para viver. "
              u"BV Locadora, orgulho de fazer parte dessa terra.")]),
 ]),
]

montar(PAGINAS, u"Roteiro de Gravação — BV Locadora",
       os.path.join(RAIZ, "roteiro-bv-locadora.html"))
