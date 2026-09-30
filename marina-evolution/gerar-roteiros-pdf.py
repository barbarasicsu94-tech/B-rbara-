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

 (u"REELS 03", u"Vertical | 30\u201340s", CLIENTE, [
  ("01", u"GANCHO",
   u"Pessoa caminhando pela Marina e falando diretamente para a c\u00e2mera.",
   [(u"FALA:", u"N\u00e3o venha pra Marina Evolution hoje. E eu tenho 3 motivos pra isso."),
    (u"LETTERING:", u"3 MOTIVOS PARA N\u00c3O IR \u00c0 MARINA EVOLUTION")]),

  ("02", u"",
   u"Pessoa pr\u00f3xima ao jet. Cortes da rotina da Marina e embarca\u00e7\u00e3o indo para a "
   u"\u00e1gua.\nMostra o jet pronto para sair.",
   [(u"FALA:", u"Primeiro: se voc\u00ea gosta daquele trabalh\u00e3o todo antes de conseguir "
               u"aproveitar seu jet\u2026 melhor continuar fazendo do jeito dif\u00edcil."),
    (u"FALA:", u"Porque aqui a ideia \u00e9 justamente facilitar a sua vida.")]),

  ("03", u"",
   u"Pessoa andando pela \u00e1rea onde ficam as embarca\u00e7\u00f5es.\nPausa curta.",
   [(u"FALA:", u"Segundo: sabe aquela preocupa\u00e7\u00e3o de sair de casa e ficar pensando: "
               u"ser\u00e1 que t\u00e1 tudo bem com meu jet?"),
    (u"FALA:", u"Pois \u00e9\u2026 aqui voc\u00ea n\u00e3o vai ter essa preocupa\u00e7\u00e3o.")]),

  ("04", u"",
   u"Imagens bonitas do Rio Branco, jet navegando, amigos e momentos na Marina.\n"
   u"Olha para a c\u00e2mera.",
   [(u"FALA:", u"E terceiro: se o seu neg\u00f3cio n\u00e3o \u00e9 rio, sol e um final de semana "
               u"bem aproveitado\u2026"),
    (u"FALA:", u"Realmente, aqui n\u00e3o \u00e9 o seu lugar.")]),

  ("05", u"",
   u"Melhores imagens da Marina e do jet no Rio Branco.\nFinaliza com a sua assinatura.",
   [(u"FALA:", u"Agora\u2026 se voc\u00ea gosta de tudo isso, acho que eu acabei de te dar 3 "
               u"motivos pra conhecer a Marina Evolution.")]),
 ]),
]

montar(PAGINAS, u"Roteiro de Gravação — Marina Evolution",
       os.path.join(RAIZ, "03-roteiros-marina-evolution.html"))
