# -*- coding: utf-8 -*-
import os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from honey_template import montar

RAIZ = os.path.dirname(os.path.abspath(__file__))
CLIENTE = u"Campeão Express"

PAGINAS = [
 (u"ROTEIRO | CAMPEÃO EXPRESS", u"Vertical | 20–30s | 3 cenas", CLIENTE, [

  ("01", u"",
   u"Personagem entrando ou caminhando pela Campeão Express. Enquanto fala, intercalar "
   u"detalhes de coletes, óculos, acessórios e produtos da conveniência.",
   [(u"ON:", u"Vai aproveitar o dia na Marina? Então passa primeiro na Campeão Express. "
             u"Aqui você encontra acessórios, bebidas, petiscos e aquele básico que "
             u"sempre faz falta na hora de curtir."),
    (u"LETTERING:", u"ANTES DE CURTIR, PASSA NA EXPRESS.")]),

  ("02", u"",
   u"Imagens mais fechadas: carne indo para a brasa, churrasco sendo servido, cerveja gelada, "
   u"amigos reunidos.",
   [(u"OFF:", u"E se a ideia é ficar por aqui, já sabe: churrasco na brasa, cerveja "
              u"gelada e tudo pronto pra aproveitar com a galera."),
    (u"LETTERING:", u"CHURRASCO + CERVEJA GELADA")]),

  ("03", u"",
   u"Personagem novamente em tela. Intercalar com TV transmitindo futebol, pessoas reunidas e "
   u"detalhes da Campeão Express.",
   [(u"ON:", u"E ainda dá pra reunir os amigos, acompanhar aquele jogo e aproveitar o clima "
             u"da Marina. Então já sabe: veio pra Marina Evolution, passa na Campeão "
             u"Express."),
    (u"LETTERING FINAL:", u"CAMPEÃO EXPRESS\nNa Marina Evolution.")]),
 ]),
]

montar(PAGINAS, u"Roteiro de Gravação — Campeão Express",
       os.path.join(RAIZ, "roteiro-campeao-express.html"))
