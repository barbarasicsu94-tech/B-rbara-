# -*- coding: utf-8 -*-
import os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from honey_template import montar

RAIZ = os.path.dirname(os.path.abspath(__file__))
CLIENTE = u"Evolution Power Sports"
NOTA = u"NOTA:"

PAGINAS = [
 (u"DIRECIONAMENTO | TROCA DE BONÉS",
  u"Vertical (9:16) | sem locução", CLIENTE, [

  ("01", u"",
   u"Enquadramento base. Pessoa de frente, centralizada, plano médio ou close, fundo limpo. "
   u"Tripé travado e marcação de fita no chão para os pés.",
   [(NOTA, u"Câmera, luz e posição não podem mudar entre um boné e outro. "
           u"É o que faz a troca parecer mágica no corte.")]),

  ("02", u"",
   u"Movimento base. A pessoa vira a cabeça para um lado e volta ao centro; depois para o "
   u"outro lado e volta. Movimento solto, mas sempre começando e terminando no mesmo ponto.",
   [(NOTA, u"Gravar o mesmo movimento no mesmo ritmo em todos os takes. O corte acontece no "
           u"meio da virada, quando o rosto sai de quadro.")]),

  ("03", u"",
   u"Repetição com cada boné. Mesmo enquadramento, mesma luz, mesma roupa, mesma "
   u"posição. Só muda a cor do boné a cada take.",
   [(NOTA, u"Gravar pelo menos 3 takes de cada cor. Vale alternar a ordem das cores depois, "
           u"na edição.")]),

  ("04", u"",
   u"Detalhes. Closes do boné: aba, logo bordado, costura, regulagem e a cartela de cores "
   u"lado a lado.",
   [(NOTA, u"Material de apoio para intercalar entre as trocas e segurar o ritmo do vídeo.")]),

  ("05", u"",
   u"Fechamento. Último boné, a pessoa pára de frente, olha para a câmera e sorri. "
   u"Entrada da logo.",
   [(NOTA, u"Deixar o último plano respirar 2 segundos para a assinatura entrar.")]),
 ]),
]

montar(PAGINAS, u"Direcionamento de Gravação — Evolution Power Sports | Bonés",
       os.path.join(RAIZ, "direcionamento-bones.html"))
