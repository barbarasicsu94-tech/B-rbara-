# -*- coding: utf-8 -*-
import os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from honey_template import montar

RAIZ = os.path.dirname(os.path.abspath(__file__))
CLIENTE = u"Cambará Materiais de Construção"

PAGINAS = [
 (u"VT CAMBARÁ — 15 SEGUNDOS", u"15 segundos", CLIENTE, [
  ("01", u"",
   u"Funcionários juntos, animados, com balões e confetes.\n"
   u"\U0001F389 Confete estoura → corte para os cartelados.",
   [(u"TODOS:", u"“Mês de celebrar com ofertas especiais na Cambará!”"),
    (u"OFF:", u"“O aniversário é da Cambará, mas o presente é seu: "
              u"compre e parcele em até 15 vezes sem juros no cartão!”")]),
  ("", u"",
   u"[ASSINATURA CAMBARÁ — 3 a 4s]",
   []),
 ]),
]

montar(PAGINAS, u"Roteiro de Gravação — VT Cambará",
       os.path.join(RAIZ, "vt-cambara.html"))
