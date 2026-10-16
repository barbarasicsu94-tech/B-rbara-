# -*- coding: utf-8 -*-
import os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from honey_template import montar

RAIZ = os.path.dirname(os.path.abspath(__file__))
CLIENTE = u"Marina Evolution"

BLOCOS = [
 (u"OBJETIVO",
  u"Apresentar a Marina Evolution como uma solução prática para quem possui jet ou "
  u"lancha, destacando a estrutura de guarda, a organização e o cuidado com o "
  u"patrimônio náutico."),
]

PAGINAS = [
 (u"ROTEIRO | VÍDEO 03 — SEU PATRIMÔNIO SEGURO",
  u"Reels | Vertical 9:16 | 30 a 40 segundos", CLIENTE, [

  ("01", u"",
   u"Personagem posicionada próxima a um jet ou lancha, olhando diretamente para a "
   u"câmera. Manter o enquadramento na personagem durante toda a fala, sem cortes de apoio.",
   [(u"ON:", u"Cansado de ficar carregando o seu jet ou sua lancha pra lá e pra cá? "
             u"Eu sei, dá trabalho, toma tempo e acaba virando uma "
             u"preocupação, né?")]),

  ("02", u"",
   u"Personagem na área de guarda da Marina, apresentando o espaço. Intercalar com "
   u"imagens das embarcações organizadas e da estrutura.",
   [(u"ON:", u"Aqui na Marina Evolution, você tem um lugar para guardar seu jet ou sua "
             u"lancha com muito mais praticidade!")]),

  ("03", u"",
   u"Imagens de apoio da estrutura interna, jets e lanchas guardados, movimentação da "
   u"equipe e detalhes da organização do espaço.",
   [(u"OFF:", u"Um espaço dedicado à guarda de embarcações, com estrutura, "
              u"organização e cuidado para você ter mais tranquilidade no dia a "
              u"dia."),
    (u"LETTERING:", u"Estrutura • Organização • Cuidado")]),

  ("04", u"",
   u"Personagem posicionada na área de guarda da Marina, com as embarcações ao "
   u"fundo, falando diretamente para a câmera.",
   [(u"ON:", u"O seu tempo é para aproveitar o passeio no Rio, não para se preocupar "
             u"com toda essa logística. Entre em contato agora mesmo e conheça nossos "
             u"planos!")]),
 ], 1, (u"Estilo", u"Comercial, humanizado e institucional."), BLOCOS),
]

montar(PAGINAS, u"Roteiro de Gravação — Marina Evolution | Seu Patrimônio Seguro",
       os.path.join(RAIZ, "roteiro-patrimonio-seguro.html"))
