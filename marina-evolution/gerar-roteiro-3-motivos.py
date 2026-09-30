# -*- coding: utf-8 -*-
import os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from honey_template import montar

RAIZ = os.path.dirname(os.path.abspath(__file__))
CLIENTE = u"Marina Evolution"

PAGINAS = [
 (u"ROTEIRO | 3 MOTIVOS PARA NÃO IR À MARINA EVOLUTION",
  u"Vertical | 30–40s", CLIENTE, [

  ("01", u"GANCHO",
   u"Pessoa caminhando pela Marina e falando diretamente para a câmera.",
   [(u"FALA:", u"Não venha pra Marina Evolution hoje. E eu tenho 3 motivos pra isso."),
    (u"LETTERING:", u"3 MOTIVOS PARA NÃO IR À MARINA EVOLUTION")]),

  ("02", u"",
   u"Pessoa próxima ao jet. Cortes da rotina da Marina e embarcação indo para a "
   u"água.\nMostra o jet pronto para sair.",
   [(u"FALA:", u"Primeiro: se você gosta daquele trabalhão todo antes de conseguir "
               u"aproveitar seu jet… melhor continuar fazendo do jeito difícil."),
    (u"FALA:", u"Porque aqui a ideia é justamente facilitar a sua vida.")]),

  ("03", u"",
   u"Pessoa andando pela área onde ficam as embarcações.\nPausa curta.",
   [(u"FALA:", u"Segundo: sabe aquela preocupação de sair de casa e ficar pensando: "
               u"será que tá tudo bem com meu jet?"),
    (u"FALA:", u"Pois é… aqui você não vai ter essa preocupação.")]),

  ("04", u"",
   u"Imagens bonitas do Rio Branco, jet navegando, amigos e momentos na Marina.\n"
   u"Olha para a câmera.",
   [(u"FALA:", u"E terceiro: se o seu negócio não é rio, sol e um final de semana "
               u"bem aproveitado…"),
    (u"FALA:", u"Realmente, aqui não é o seu lugar.")]),

  ("05", u"",
   u"Melhores imagens da Marina e do jet no Rio Branco.\nFinaliza com a sua assinatura.",
   [(u"FALA:", u"Agora… se você gosta de tudo isso, acho que eu acabei de te dar 3 "
               u"motivos pra conhecer a Marina Evolution.")]),
 ]),
]

montar(PAGINAS, u"Roteiro de Gravação — Marina Evolution | 3 Motivos",
       os.path.join(RAIZ, "roteiro-3-motivos.html"))
