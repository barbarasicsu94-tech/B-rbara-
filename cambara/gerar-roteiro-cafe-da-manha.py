# -*- coding: utf-8 -*-
import os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from honey_template import montar

RAIZ = os.path.dirname(os.path.abspath(__file__))
CLIENTE = u"Cambará Materiais de Construção"

PAGINAS = [
 (u"ROTEIRO — CAFÉ DA MANHÃ | ANIVERSÁRIO CAMBARÁ",
  u"Vertical | até 30s", CLIENTE, [

  ("01", u"",
   u"Personagem em uma mesa decorada, com balões dos dois lados, segurando uma xícara "
   u"de café.",
   [(u"ON:", u"Pra fechar o mês de aniversário da Cambará do jeito certo, a gente "
             u"preparou um momento especial pra você!"),
    (u"LETTERING:", u"CAFÉ DA MANHÃ CAMBARÁ")]),

  ("02", u"",
   u"Cortes rápidos das imagens já captadas: café, mesa, comidas e detalhes do "
   u"café da manhã.",
   [(u"OFF:", u"Dia 31 de outubro, das 9h ao meio-dia, vem tomar um café da manhã com a "
              u"gente e celebrar mais um ano dessa história."),
    (u"LETTERING:", u"31 DE OUTUBRO\n9H ÀS 12H")]),

  ("03", u"",
   u"Personagem caminhando pelos corredores da Cambará, apontando para produtos e "
   u"prateleiras.",
   [(u"ON:", u"E tem mais: esse também será o último dia pra aproveitar 15% de "
             u"desconto nos pagamentos em dinheiro ou Pix."),
    (u"LETTERING:", u"ÚLTIMO DIA!\n15% OFF NO DINHEIRO OU PIX")]),

  ("04", u"",
   u"Personagem retorna para a mesa do café ou fica em um ponto bonito da loja com os "
   u"balões ao fundo.",
   [(u"ON:", u"Então já marca aí: dia 31, a partir das 9h. Vem celebrar com a "
             u"Cambará, tomar um café com a gente e aproveitar as últimas ofertas "
             u"do mês!"),
    (u"LETTERING FINAL:", u"31/10 | 9H ÀS 12H\nSÁBADO")]),
 ]),
]

montar(PAGINAS, u"Roteiro de Gravação — Cambará | Café da Manhã",
       os.path.join(RAIZ, "roteiro-cafe-da-manha.html"))
