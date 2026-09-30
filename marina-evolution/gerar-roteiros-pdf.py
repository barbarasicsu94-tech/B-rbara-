# -*- coding: utf-8 -*-
import os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from honey_template import montar

RAIZ = os.path.dirname(os.path.abspath(__file__))
CLIENTE = u"Marina Evolution"
OFF_INTERFONE = u"Off masculino com aquele efeito de interfone:"

PAGINAS = [
 (u"REELS 01 — PATRIMÔNIO NÁUTICO PROTEGIDO", u"Vertical | até 45s", CLIENTE, [
  ("01", u"ABERTURA",
   u"Imagens externas da Marina + jets e embarcações.",
   [(u"OFF:", u"“Seu jet ou sua lancha é muito mais do que uma embarcação. É um patrimônio.”")]),
  ("02", u"ESTRUTURA",
   u"Mostrar chegada da embarcação, acesso e estrutura da Marina.",
   [(u"OFF:", u"“E para cuidar desse patrimônio, você precisa de um lugar preparado para isso.”")]),
  ("03", u"CUIDADOS E SEGURANÇA",
   u"Mostrar detalhes da estrutura, armazenamento, limpeza, equipe e demais diferenciais disponíveis.",
   [(u"OFF:", u"“Na Marina Evolution, sua embarcação conta com estrutura, tecnologia e segurança "
              u"para estar sempre bem cuidada e pronta para o próximo passeio.”")]),
  ("04", u"FECHAMENTO",
   u"Embarcação saindo da Marina + imagens da água.",
   [(u"OFF:", u"“Porque quando sua embarcação está em boas mãos, você só precisa se preocupar "
              u"com uma coisa: aproveitar a próxima aventura.”"),
    (u"TEXTO NA TELA:", u"MARINA EVOLUTION\nSeu porto seguro. ⚓\U0001F30A")]),
 ]),

 (u"REELS 02", u"Horizontal | até 30s", CLIENTE, [
  ("01", u"",
   u"Imagem da Marina horizontal com estilo de edição vintage.",
   [(u"Texto em tela:", u"Sexta - feira, 17:42")]),
  ("02", u"",
   u"Transiciona a edição para algo mais moderno. Cortes de um jet descendo ou cenas do estacionamento delas.",
   [(OFF_INTERFONE, u"Hora de navegar")]),
  ("03", u"",
   u"Cortes de cenas de jet na água, passeio e cenas respiros da natureza ali próximo do Rio Branco. "
   u"Por exemplo (árvores, mirante, pássaros).",
   [(OFF_INTERFONE, u"contemplar a natureza")]),
  ("04", u"",
   u"Cena do pôr do sol próximo a ponte do Rio Branco ou próximo da Marina.\nFinaliza com assinatura.",
   [(OFF_INTERFONE, u"E ver quele pôr do sol…\nIsso só é possível na Marina Evolution")]),
 ]),
]

montar(PAGINAS, u"Roteiro de Gravação — Marina Evolution",
       os.path.join(RAIZ, "03-roteiros-marina-evolution.html"))
