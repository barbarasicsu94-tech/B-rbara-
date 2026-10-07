# -*- coding: utf-8 -*-
import os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from honey_template import montar

RAIZ = os.path.dirname(os.path.abspath(__file__))
CLIENTE = u"Evolution Boutique"
NOTA = u"NOTA:"

BLOCOS = [
 (u"IDEIA",
  u"Produzir um vídeo dinâmico para apresentar os diferentes modelos de bonés "
  u"disponíveis na Evolution Boutique. A pessoa permanece no mesmo enquadramento e, "
  u"através de movimentos de cabeça e cortes rápidos, os bonés vão sendo "
  u"trocados, criando um efeito visual semelhante a um stop motion. A proposta é explorar "
  u"mais a boutique e mostrar que a Evolution também possui acessórios ligados ao "
  u"lifestyle esportivo e de aventura."),
 (u"OBJETIVO",
  u"Dar visibilidade à Evolution Boutique, apresentar a variedade de bonés "
  u"disponíveis e fortalecer a associação da marca com lifestyle, indo "
  u"além dos veículos."),
]

PAGINAS = [
 (u"DIRECIONAMENTO | BONÉS EVOLUTION BOUTIQUE",
  u"Vertical (9:16) | sem locução", CLIENTE, [

  ("01", u"",
   u"Enquadramento base. Pessoa de frente, centralizada, plano médio ou close, com a "
   u"boutique ao fundo. Tripé travado e marcação de fita no chão para os "
   u"pés.",
   [(NOTA, u"Câmera, luz e posição não podem mudar entre um boné e "
           u"outro. É o que faz a troca parecer mágica no corte.")]),

  ("02", u"",
   u"Movimento base. A pessoa vira a cabeça para um lado e volta ao centro; depois para o "
   u"outro lado e volta. Sempre começando e terminando no mesmo ponto.",
   [(NOTA, u"Mesmo movimento, mesmo ritmo em todos os takes. O corte acontece no meio da "
           u"virada, quando o rosto sai de quadro — é ali que o boné troca.")]),

  ("03", u"",
   u"Repetição com cada boné. Mesmo enquadramento, mesma luz, mesma roupa, mesma "
   u"posição. Só muda a cor e o modelo a cada take.",
   [(NOTA, u"Gravar ao menos 3 takes de cada boné. Quanto mais modelos, mais forte o efeito "
           u"de stop motion na montagem.")]),

  ("04", u"",
   u"A boutique. Planos do espaço: araras e prateleiras, bonés expostos lado a lado, "
   u"óculos, luvas e demais acessórios. Closes de aba, logo bordado e costura.",
   [(NOTA, u"É o material que mostra que a Evolution também é lifestyle, não "
           u"só veículos. Intercalar entre as trocas para segurar o ritmo.")]),

  ("05", u"",
   u"Fechamento. Último boné, a pessoa pára de frente, olha para a câmera e "
   u"sorri. Entrada da logo da Evolution Boutique.",
   [(NOTA, u"Deixar o último plano respirar 2 segundos para a assinatura entrar.")]),
 ], 1, None, BLOCOS),
]

montar(PAGINAS, u"Direcionamento de Gravação — Evolution Boutique | Bonés",
       os.path.join(RAIZ, "direcionamento-bones.html"))
