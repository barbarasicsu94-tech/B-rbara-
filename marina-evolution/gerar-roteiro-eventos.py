# -*- coding: utf-8 -*-
import os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from honey_template import montar

RAIZ = os.path.dirname(os.path.abspath(__file__))
CLIENTE = u"Marina Evolution"

BLOCOS = [
 (u"OBJETIVO",
  u"Apresentar a Marina Evolution como um espaço para realização de eventos, "
  u"destacando sua estrutura, ambiente e localização privilegiada às margens do "
  u"Rio Branco."),
]

PAGINAS = [
 (u"ROTEIRO | VÍDEO 02 — MARINA: O SEU LOCAL IDEAL PARA EVENTOS",
  u"Reels | Vertical 9:16 | 30 a 40 segundos", CLIENTE, [

  ("01", u"",
   u"Personagem em enquadramento fechado, com o Rio Branco ao fundo. Enquanto faz a pergunta, "
   u"a câmera se afasta gradualmente, revelando o ambiente da Marina.",
   [(u"ON:", u"Já imaginou realizar seu próximo evento com esse cenário aqui?"),
    (u"LETTERING:", u"Seu próximo evento pode ser aqui!")]),

  ("02", u"",
   u"Imagens de apoio de eventos já realizados na Marina Evolution.",
   [(u"OFF:", u"Aqui na Marina Evolution, você encontra um ambiente diferente para reunir "
              u"pessoas, comemorar momentos especiais e sair do tradicional."),
    (u"LETTERING:", u"Um espaço para momentos especiais.")]),

  ("03", u"",
   u"Personagem caminhando pelo espaço, com imagens de drone intercaladas, mostrando a "
   u"estrutura da Marina, o Rio Branco e a paisagem ao redor.",
   [(u"ON:", u"E o melhor é que tudo isso fica em um dos cenários mais bonitos de Boa "
             u"Vista: o nosso Rio Branco!"),
    (u"LETTERING:", u"O Rio Branco como cenário.")]),

  ("04", u"",
   u"Personagem posicionada na escadaria da Marina, com o Rio Branco ao fundo, em um "
   u"enquadramento aberto que valorize a paisagem.",
   [(u"ON:", u"Seja uma confraternização, aniversário ou um encontro especial, a "
             u"Marina Evolution pode ser o lugar do seu próximo evento. Entre em contato e "
             u"consulte nossa disponibilidade!")]),
 ], 1, (u"Estilo", u"Comercial, lifestyle e humanizado."), BLOCOS),
]

montar(PAGINAS, u"Roteiro de Gravação — Marina Evolution | Eventos",
       os.path.join(RAIZ, "roteiro-eventos.html"))
