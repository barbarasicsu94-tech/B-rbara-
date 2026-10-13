# -*- coding: utf-8 -*-
import os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from honey_template import montar

RAIZ = os.path.dirname(os.path.abspath(__file__))
CLIENTE = u"BV Locadora"

PAGINAS = [
 (u"ROTEIRO — BV LOCADORA | PLANO B",
  u"Reels vertical (9:16) | 30 a 40 segundos", CLIENTE, [

  ("01", u"",
   u"Personagem caminhando sob o sol, demonstrando cansaço. Ela olha para o celular, como "
   u"se estivesse verificando o preço de uma corrida por aplicativo.",
   [(u"NARRAÇÃO (OFF) — VOZ DA PERSONAGEM:",
     u"Cansada de andar a pé, depender de aplicativo e gastar dinheiro toda vez que precisa "
     u"sair?")]),

  ("02", u"",
   u"A personagem olha diretamente para a câmera. Em seguida, faz uma transição "
   u"dinâmica para a fachada da BV Locadora.",
   [(u"(ON):", u"Então, se o Plano A tá complicado, tá na hora de partir pro "
               u"Plano B!"),
    (u"LETTERING:", u"PLANO B?")]),

  ("03", u"",
   u"Personagem na BV Locadora, caminhando entre os veículos. Intercalar sua fala com "
   u"imagens em OFF dos carros disponíveis.",
   [(u"(ON/OFF):", u"B de BV Locadora! Aqui você encontra diferentes opções de "
                   u"veículos e planos de locação que combinam com a sua rotina."),
    (u"LETTERING:", u"B de BV Locadora!")]),

  ("04", u"",
   u"Personagem ao lado de um veículo da BV, segurando a chave e falando diretamente para a "
   u"câmera.",
   [(u"(ON):", u"Não complica a sua rotina! Coloca o Plano B em ação. Chama a BV "
               u"Locadora e escolha seu próximo carro!"),
    (u"ENCERRAMENTO:", u"Logo BV Locadora")]),
 ], False, (u"Personagem", u"Apresentadora feminina")),
]

montar(PAGINAS, u"Roteiro de Gravação — BV Locadora | Plano B",
       os.path.join(RAIZ, "roteiro-plano-b.html"))
