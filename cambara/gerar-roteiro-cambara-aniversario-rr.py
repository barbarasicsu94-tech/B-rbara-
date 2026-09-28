# -*- coding: utf-8 -*-
import os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from honey_template import montar

RAIZ = os.path.dirname(os.path.abspath(__file__))
CLIENTE = u"Cambará Materiais de Construção"

PAGINAS = [
 (u"ROTEIRO — ANIVERSÁRIO DE RORAIMA | CAMBARÁ",
  u"Horizontal | 30s aprox.", CLIENTE, [

  ("01", u"",
   u"Imagens de Roraima: natureza, cidade, paisagens e elementos regionais.",
   [(u"OFF:", u"Há 38 anos, Roraima escreve oficialmente uma história feita de coragem, "
              u"crescimento e gente que acredita nessa terra."),
    (u"Lettering:", u"Roraima, 38 anos")]),

  ("02", u"VENDEDOR 01 | CROMA",
   u"Primeiro colaborador em cena. Ao fundo, uma paisagem marcante de Roraima.\n"
   u"Corte rápido para imagens do estado.",
   [(u"ON:", u"Tenho orgulho de viver em um estado que cresce sem esquecer as suas raízes.")]),

  ("03", u"VENDEDOR 02 | CROMA",
   u"Segundo colaborador. Fundo muda para outra imagem de Roraima.",
   [(u"FALA:", u"Orgulho de fazer parte de uma terra onde tanta gente trabalha todos os dias "
               u"para construir um futuro melhor."),
    (u"OFF complementa:", u"E cada nova história, cada casa e cada conquista ajudam a "
                          u"construir o Roraima de amanhã.")]),

  ("04", u"VENDEDOR 03 | CROMA",
   u"Terceiro colaborador. Pode ter ao fundo Boa Vista ou alguma paisagem mais urbana.\n"
   u"Aqui já começa a entrar discretamente a identidade da Cambará.",
   [(u"ON:", u"Porque construir Roraima também é cuidar de quem faz essa terra "
             u"acontecer.")]),

  ("05", u"",
   u"Cortes rápidos dos três, intercalados com imagens de Roraima e da Cambará.\n"
   u"Encerramento com assinatura da Cambará.",
   [(u"OFF:", u"Neste 5 de outubro, a Cambará celebra os 38 anos de Roraima e o orgulho de "
              u"fazer parte dessa história."),
    (u"Lettering NA TELA:", u"Parabéns, Roraima!")]),
 ], False, u"Orgulho de fazer parte dessa história"),
]

montar(PAGINAS, u"Roteiro de Gravação — Cambará | Aniversário de Roraima",
       os.path.join(RAIZ, "roteiro-cambara-aniversario-rr.html"))
